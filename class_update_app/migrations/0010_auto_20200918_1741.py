# Generated by Django 3.1.1 on 2020-09-18 08:41

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('class_update_app', '0009_classmodel_diffclassname'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmodel',
            name='newcontent',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), null=True, size=100),
        ),
        migrations.AddField(
            model_name='classmodel',
            name='oldcontent',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), null=True, size=100),
        ),
    ]