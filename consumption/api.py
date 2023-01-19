from django.contrib.auth.hashers import check_password
from django.db.models import Sum, Max, Min
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from consumption.ConsumptionResponses import ConsumptionResponse, NotFoundResponse
from consumption.models import Consumption
from consumption.serializers import ConsumptionSerializer
from powermeter.models import PowerMeter

class ConsumptionView(APIView):
    @swagger_auto_schema(responses={200: ConsumptionSerializer(many=True), 404: 'Not Found'})
    def get(self, request, meter_id):
        """
           Este endpoint sirve para obtener la lista de consumos de un medidor.

           El endpoint recibe un id de medidor y devuelve una lista de consumos.

           Debe devolver un error 404 si el medidor no existe. Y tanto si existe y tiene consumos como si no tiene consumos, debe devolver un 200.
        """
        try:
            meter = PowerMeter.objects.get(meter_id=meter_id)
        except PowerMeter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        consumptions = Consumption.objects.filter(meter=meter)
        serializer = ConsumptionSerializer(consumptions, many=True)
        return ConsumptionResponse(meter_id=meter_id, meter_name=meter.name, consumptions=serializer.data)

    def post(self, request, meter_id):
        """
           Este endpoint sirve para crear un consumo.

           El endpoint recibe un id de medidor y un consumo.

           Debe devolver un error 404 si el medidor no existe. Y si el medidor existe, debe devolver un 201.
        """
        try:
            meter = PowerMeter.objects.get(meter_id=meter_id)
        except PowerMeter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        consumption = Consumption(meter=meter, consumption=request.data["consumption"])
        consumption.save()
        return Response(status=status.HTTP_201_CREATED)


class TotalConsumptionView(APIView):
    """
    Este endpoint sirve para obtener el consumo total de un medidor.

    Si la request se hizo apropiadamente (el medidor existe), se devuelve un status 200 y un JSON con el consumo total.
    Si el medidor no existe, se devuelve un status 404 y un JSON con el error.
    """
    def get(self, request, meter_id):
        try:
            meter = PowerMeter.objects.get(meter_id=meter_id)
        except PowerMeter.DoesNotExist:
            return NotFoundResponse()
        total_consumption = Consumption.objects.filter(meter=meter).aggregate(Sum('consumption'))
        if total_consumption['consumption__sum'] is None:
            return ConsumptionResponse(meter_id, meter.name, total_consumption=0)
        else:
            return ConsumptionResponse(meter_id, meter.name, total_consumption['consumption__sum'])


class AverageConsumptionView(APIView):
    """
    Este endpoint sirve para obtener el consumo promedio de un medidor.

    Si la request se hizo apropiadamente (el medidor existe), se devuelve un status 200 y un JSON con el consumo promedio.
    Si el medidor no existe, se devuelve un status 404 y un JSON con el error.
    """
    def get(self, request, meter_id):
        try:
            meter = PowerMeter.objects.get(meter_id=meter_id)
        except PowerMeter.DoesNotExist:
            return NotFoundResponse()
        average_consumption = Consumption.objects.filter(meter=meter).aggregate(Sum('consumption'))
        if average_consumption['consumption__sum'] is None:
            return ConsumptionResponse(meter_id, meter.name, average_consumption=0)
        else:
            avg = average_consumption['consumption__sum'] / Consumption.objects.filter(meter=meter).count()
            return ConsumptionResponse(meter_id, meter.name, average_consumption=avg)


class MinMaxConsumptionView(APIView):
    def get(self, request, meter_id):
        """
        Este endpoint sirve para obtener el consumo mínimo y máximo de un medidor.

        Si la request se hizo apropiadamente (el medidor existe), se devuelve un status 200 y un JSON con el consumo mínimo y máximo.
        Si el medidor no existe, se devuelve un status 404 y un JSON con el error.
        """
        try:
            meter = PowerMeter.objects.get(meter_id=meter_id)
        except PowerMeter.DoesNotExist:
            return NotFoundResponse()
        min_max_consumption = Consumption.objects.filter(meter=meter).aggregate(Min('consumption'), Max('consumption'))
        if min_max_consumption['consumption__min'] is None:
            return ConsumptionResponse(meter_id, meter.name, min_consumption=0, max_consumption=0)
        else:
            return ConsumptionResponse(
                meter_id,
                meter.name,
                min_consumption=min_max_consumption['consumption__min'],
                max_consumption=min_max_consumption['consumption__max']
            )
