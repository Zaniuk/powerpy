from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from powermeter.serializers import PowerMeterSerializer


class PowerMeterView(APIView):
    """
    Este endpoint sirve para crear un medidor.
    Requiere los siguientes campos:
    - name: nombre del medidor
    - meter_id: id del medidor
    """
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PowerMeterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


