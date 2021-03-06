# Generated by Django 3.1.1 on 2020-09-14 08:48

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('class_update_app', '0006_auto_20200914_0708'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', django_mysql.models.ListTextField(models.CharField(max_length=100), size=100)),
                ('content', django_mysql.models.ListTextField(models.CharField(max_length=100), size=100)),
                ('url', django_mysql.models.ListTextField(models.CharField(max_length=100), size=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='classmodel',
            name='classname',
        ),
        migrations.RemoveField(
            model_name='classmodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='classmodel',
            name='url',
        ),
    ]
