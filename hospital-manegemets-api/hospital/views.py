from django.shortcuts import render,HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("It works!")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError
from .models import (
    Appointments, Doctors, MediflowAppointment, MediflowBilling, 
    MediflowDepartment, MediflowDoctor, MediflowMedicalrecord, 
    MediflowPatient, Patients, Staff, AuthGroup, AuthGroupPermissions, 
    AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, 
    DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession
)
from .serializers import (
    AppointmentsSerializer, DoctorsSerializer, MediflowAppointmentSerializer,
    MediflowBillingSerializer, MediflowDepartmentSerializer, 
    MediflowDoctorSerializer, MediflowMedicalrecordSerializer, 
    MediflowPatientSerializer, PatientsSerializer, StaffSerializer, 
    AuthGroupSerializer, AuthGroupPermissionsSerializer, 
    AuthPermissionSerializer, AuthUserSerializer, AuthUserGroupsSerializer, 
    AuthUserUserPermissionsSerializer, DjangoAdminLogSerializer, 
    DjangoContentTypeSerializer, DjangoMigrationsSerializer, 
    DjangoSessionSerializer
)

class AppointmentListView(APIView):
    """
    API View for handling the listing and creation of Appointments.
    """
    def get(self, request):
        try:
            appointments = Appointments.objects.all()
            serializer = AppointmentsSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while retrieving appointments: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = AppointmentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while creating the appointment: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class DoctorListView(APIView):
    """
    API View for handling the listing and creation of Doctors.
    """
    def get(self, request):
        try:
            doctors = Doctors.objects.all()
            serializer = DoctorsSerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while retrieving doctors: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = DoctorsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while creating the doctor: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MediflowAppointmentListView(APIView):
    """
    API View for handling the listing and creation of MediflowAppointments.
    """
    def get(self, request):
        try:
            appointments = MediflowAppointment.objects.all()
            serializer = MediflowAppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except MediflowAppointment.DoesNotExist:
            return Response(
                {'detail': "Mediflow appointments not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while retrieving mediflow appointments: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = MediflowAppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response(
                {'detail': f"Validation error: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while creating the Mediflow appointment: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class MediflowBillingListView(APIView):
    """
    API View for handling the listing and creation of MediflowBilling.
    """
    def get(self, request):
        try:
            billing_records = MediflowBilling.objects.all()
            serializer = MediflowBillingSerializer(billing_records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while retrieving billing records: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            serializer = MediflowBillingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {'detail': f"An error occurred while creating the billing record: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# You can continue adding similar views for other models as needed.

