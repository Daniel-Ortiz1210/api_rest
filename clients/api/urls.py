from django.urls import path
from .views import ClientsView, ClientView

urlpatterns = [
    path('clients/', ClientsView.as_view()),
    path('clients/<pk>', ClientView.as_view())
]