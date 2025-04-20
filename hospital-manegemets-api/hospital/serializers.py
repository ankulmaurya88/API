from rest_framework import serializers
from .models import (
    Appointments, Doctors, MediflowAppointment, MediflowBilling, 
    MediflowDepartment, MediflowDoctor, MediflowMedicalrecord, 
    MediflowPatient, Patients, Staff, AuthGroup, AuthGroupPermissions, 
    AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, 
    DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession
)

# Serializers for each model

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class MediflowAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediflowAppointment
        fields = '__all__'


class MediflowBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediflowBilling
        fields = '__all__'


class MediflowDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediflowDepartment
        fields = '__all__'


class MediflowDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediflowDoctor
        fields = '__all__'


class MediflowMedicalrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediflowMedicalrecord
        fields = '__all__'


class MediflowPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediflowPatient
        fields = '__all__'


class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'


class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'


class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'


class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'


class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'


class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'


class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'


class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'


class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'
