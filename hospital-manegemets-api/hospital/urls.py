

from django.urls import path
from .views import (
    AppointmentListView,
    DoctorListView,
    MediflowAppointmentListView,
    MediflowBillingListView
)

urlpatterns = [
    path('appointments/', AppointmentListView.as_view(), name='appointments-list'),
    path('doctors/', DoctorListView.as_view(), name='doctors-list'),
    path('mediflow/appointments/', MediflowAppointmentListView.as_view(), name='mediflow-appointments-list'),
    path('mediflow/billing/', MediflowBillingListView.as_view(), name='mediflow-billing-list'),
]
