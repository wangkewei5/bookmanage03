from django.urls import path

from . import views
from .views import SetSession

urlpatterns = [
    path('setsession/', SetSession.as_view()),
]
