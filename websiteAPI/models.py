# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class StatusEmployee(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    unemployed_id = models.CharField(max_length=32, blank=True, null=True)
    is_finish = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_employee'


class StatusFinal(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_final'


class StatusFirst(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_first'


class StatusSecond(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_second'


class StatusUnemployee(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    unemployed_id = models.CharField(max_length=32, blank=True, null=True)
    status_first_id = models.CharField(max_length=32, blank=True, null=True)
    status_second_id = models.CharField(max_length=32, blank=True, null=True)
    status_final_id = models.CharField(max_length=32, blank=True, null=True)
    material = models.IntegerField(blank=True, null=True)
    train = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_unemployee'


class Unemployed(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    work_year = models.IntegerField(blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    household_place = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    creator = models.CharField(max_length=32, blank=True, null=True)
    follower = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unemployed'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    department_id = models.CharField(max_length=32, blank=True, null=True)
    is_supervisor = models.IntegerField(blank=True, null=True)
    is_view_all = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
