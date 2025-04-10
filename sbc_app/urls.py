from django.urls import path
from .views import login_view, dashboard_view

urlpatterns = [
    path('', login_view, name='login'),  # Ruta para el login
    path('dashboard/', dashboard_view, name='dashboard'),  # Ruta para el dashboard
]