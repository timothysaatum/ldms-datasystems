# Generated by Django 4.2.2 on 2023-11-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_rename_conact_ward_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='sex_of_client',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
