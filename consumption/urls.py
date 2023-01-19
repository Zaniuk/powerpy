from django.urls import path

from consumption.api import ConsumptionView, TotalConsumptionView, AverageConsumptionView, MinMaxConsumptionView

urlpatterns = [
    path('consumption/<str:meter_id>/', ConsumptionView.as_view(), name='consumption'),
    path('consumption/<str:meter_id>/total', TotalConsumptionView.as_view(), name='total_consumption'),
    path('consumption/<str:meter_id>/average', AverageConsumptionView.as_view(), name='average_consumption'),
    path('consumption/<str:meter_id>/minmax', MinMaxConsumptionView.as_view(), name='min_max_consumption'),
]