from django.urls import path

from powermeter.api import PowerMeterView

urlpatterns = [
    path('powermeter/', PowerMeterView.as_view(), name='powermeter'),
]