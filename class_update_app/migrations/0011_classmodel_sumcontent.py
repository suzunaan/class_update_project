# Generated by Django 3.1.1 on 2020-09-18 11:24

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('class_update_app', '0010_auto_20200918_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmodel',
            name='sumcontent',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), null=True, size=100),
        ),
    ]
