from rest_framework import status
from rest_framework.response import Response


class ConsumptionResponse(Response):
    def __init__(self, meter_id, meter_name, consumptions=None, total_consumption=None, average_consumption=None, min_consumption=None, max_consumption=None, status=status.HTTP_200_OK):
        data = {
            "meter_id": meter_id,
            "meter_name": meter_name,
        }
        if consumptions is not None:
            data["consumptions"] = consumptions
        if total_consumption is not None:
            data["total_consumption"] = total_consumption
        if average_consumption is not None:
            data["average_consumption"] = average_consumption
        if min_consumption is not None:
            data["min_consumption"] = min_consumption
        if max_consumption is not None:
            data["max_consumption"] = max_consumption
        super().__init__(data, status=status)


class NotFoundResponse(Response):
    def __init__(self, status=status.HTTP_404_NOT_FOUND):
        super().__init__({
            "error": "Powermeter not found",
        }, status=status)
