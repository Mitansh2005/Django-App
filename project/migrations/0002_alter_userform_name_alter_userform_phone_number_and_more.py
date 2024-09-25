# Generated by Django 5.0.1 on 2024-09-25 10:30

import project.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='name',
            field=models.CharField(max_length=100, validators=[project.validators.validate_no_special_characters]),
        ),
        migrations.AlterField(
            model_name='userform',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[project.validators.validate_phone_number]),
        ),
        migrations.AlterField(
            model_name='userform',
            name='surname',
            field=models.CharField(max_length=100, validators=[project.validators.validate_no_special_characters]),
        ),
    ]