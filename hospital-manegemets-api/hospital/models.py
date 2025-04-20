# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointments(models.Model):
    appointmentid = models.AutoField(db_column='AppointmentID', primary_key=True)  # Field name made lowercase.
    patientid = models.ForeignKey('Patients', models.DO_NOTHING, db_column='PatientID', blank=True, null=True)  # Field name made lowercase.
    doctorid = models.ForeignKey('Doctors', models.DO_NOTHING, db_column='DoctorID', blank=True, null=True)  # Field name made lowercase.
    appointmentdate = models.DateField(db_column='AppointmentDate', blank=True, null=True)  # Field name made lowercase.
    appointmenttime = models.TimeField(db_column='AppointmentTime', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Appointments'


class Doctors(models.Model):
    doctorid = models.AutoField(db_column='DoctorID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='Specialization', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    experience = models.IntegerField(db_column='Experience', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctors'


class MediflowAppointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)
    doctor = models.ForeignKey('MediflowDoctor', models.DO_NOTHING)
    patient = models.ForeignKey('MediflowPatient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MediFlow_appointment'


class MediflowBilling(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    status = models.CharField(max_length=20)
    patient = models.ForeignKey('MediflowPatient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MediFlow_billing'


class MediflowDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'MediFlow_department'


class MediflowDoctor(models.Model):
    id = models.BigAutoField(primary_key=True)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    availability = models.IntegerField()
    department = models.ForeignKey(MediflowDepartment, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MediFlow_doctor'


class MediflowMedicalrecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    diagnosis = models.TextField()
    prescription = models.TextField()
    date = models.DateTimeField()
    doctor = models.ForeignKey(MediflowDoctor, models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey('MediflowPatient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MediFlow_medicalrecord'


class MediflowPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MediFlow_patient'


class Patients(models.Model):
    patientid = models.AutoField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    medicalhistory = models.TextField(db_column='MedicalHistory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patients'


class Staff(models.Model):
    staffid = models.AutoField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=13)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    workschedule = models.TextField(db_column='WorkSchedule', blank=True, null=True)  # Field name made lowercase.
    joiningdate = models.DateField(db_column='JoiningDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staff'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
