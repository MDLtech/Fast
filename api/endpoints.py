  from fastapi import APIRouter
from datetime import datetime
from fastapi import HTTPException
from decimal import Decimal

from db.models import Tariff

router = APIRouter()


@router.get("/insurance_cost/")
async def calculate_insurance_cost(cost: float, tariff: str, date: str = None):
    try:
        target_date = (
            datetime.strptime(date, "%Y-%m-%d").date()
            if date
            else datetime.now().date()
        )
    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Date should be in the format 'YYYY-MM-DD'.",
        )

    closest_tariff = (
        await Tariff.filter(date__lte=target_date, cargo_type=tariff)
        .order_by("-date")
        .first()
    )

    if closest_tariff is None:
        raise HTTPException(status_code=400, detail="Tariff not found")

    return {"insurance_cost": Decimal(cost) * closest_tariff.rate}


@router.post("/update_tariffs")
async def update_tariffs(json_data: dict):
    for date_str, tariffs_list in json_data.items():
        for tariff_data in tariffs_list:
            cargo_type = tariff_data.get("cargo_type")
            rate = tariff_data.get("rate")

            # Проверка наличия необходимых полей в JSON
            if not cargo_type or not rate:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid JSON format. 'cargo_type' and 'rate' are required fields.",
                )

            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid date format. Date should be in the format 'YYYY-MM-DD'.",
                )

            tariff = await Tariff.filter(cargo_type=cargo_type, date=date).first()
            if tariff:
                tariff.rate = Decimal(rate)
                await tariff.save()
            else:
                await Tariff.create(
                    cargo_type=cargo_type, rate=Decimal(rate), date=date
                )

    return {"message": "Tariffs updated successfully."}
