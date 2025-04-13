from django.urls import path
from sbc_app.views import login_view, dashboard_view

urlpatterns = [
    path('', login_view, name='login'),         # La URL raíz muestra el login
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
