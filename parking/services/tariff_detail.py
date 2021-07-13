from parking.models import TariffDetail, Tariff, Operation
from datetime import datetime, timezone


def get_curr_tariff_details():
    curr_tariff = Tariff.objects.filter(start_date__lte=datetime.now()).filter(end_date__gte=datetime.now())[0]
    details = TariffDetail.objects.filter(tariff=curr_tariff).order_by('hours')
    return details


def get_amount_to_pay(obj: Operation) -> int:
    """
    Calculates the amount to be paid according to the current tariff,
    which is taken from the database
    """

    # the period during which the car was parked in the parking lot
    period = (timezone.now() - obj.add_date)

    current_tariff = Tariff.objects.get(is_current=True)
    tariff_queryset = TariffDetail.objects.filter(tariff=current_tariff)

    # max duration tariff which is not lower than the time that the driver stood in the parking lot
    tariff = tariff_queryset.filter(duration__lte=period).order_by("duration").last()

    if tariff is None:
        # min duration tariff which is not lower than the time that the driver stood in the parking lot
        tariff = tariff_queryset.filter(duration__gte=period).order_by("-duration").last()

    amount_to_pay = period / tariff.duration * tariff.price
    return amount_to_pay
