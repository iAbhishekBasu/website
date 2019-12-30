# Generated by Django 2.2 on 2019-10-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thereg', '0004_auto_20191001_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='Mail_ID',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Department',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Institute',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='Year',
            field=models.CharField(blank=True, max_length=90),
        ),
    ]
