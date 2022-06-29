from django.urls import path
from .views import NumServer, WaitingProbability
from django.views.decorators.csrf import csrf_exempt

app_name = "erlangc"

urlpatterns = [
    path('waiting-probability', WaitingProbability.as_view()),
    path("number-server", NumServer.as_view()),
]