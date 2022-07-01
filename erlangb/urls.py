from django.urls import path
from .views import BlockingProbability, NumChannel, holdingTime,offeredLoad,arrivalRate,NumChannelChart
from django.views.decorators.csrf import csrf_exempt

app_name = "erlangb"

urlpatterns = [
    path('hold-time', holdingTime),
    path('offered-load', offeredLoad),
    path('arrival-rate', arrivalRate),
    path('blocking-probability', BlockingProbability.as_view()),
    path("number-channel", NumChannel.as_view()),
    path("chart", NumChannelChart.as_view()),
]