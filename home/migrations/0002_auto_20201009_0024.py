# Generated by Django 3.0.8 on 2020-10-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='ipAddress',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
