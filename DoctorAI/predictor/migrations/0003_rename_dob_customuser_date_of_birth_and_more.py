# Generated by Django 5.1.4 on 2025-04-25 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(max_length=15),
        ),
    ]
