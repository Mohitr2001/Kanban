# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class Status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'status'


class Issuetype(models.Model):
    issue_type_id = models.IntegerField(primary_key=True)
    issue_type_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'issuetype'


class Priority(models.Model):
    priority_id = models.IntegerField(primary_key=True)
    priority_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'priority'


class Issues(models.Model):
    issue_id = models.IntegerField(primary_key=True)
    user_id_fk = models.ForeignKey(Users, models.DO_NOTHING, db_column='user_id_fk', blank=True, null=True)
    project_id_fk = models.ForeignKey('Project', models.DO_NOTHING, db_column='project_id_fk', blank=True, null=True)
    issue_type_id_fk = models.ForeignKey(Issuetype, models.DO_NOTHING, db_column='issue_type_id_fk', blank=True, null=True)
    status_id_fk = models.ForeignKey(Status, models.DO_NOTHING, db_column='status_id_fk', blank=True, null=True)
    assignee = models.ForeignKey(Users, models.DO_NOTHING, related_name='issues_assignee_set', blank=True, null=True)
    reporter = models.ForeignKey(Users, models.DO_NOTHING, related_name='issues_reporter_set', blank=True, null=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    priority_id_fk = models.ForeignKey(Priority, models.DO_NOTHING, db_column='priority_id_fk', blank=True, null=True)
    acceptance_criteria = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class Project(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'project'
