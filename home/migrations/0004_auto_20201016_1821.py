# Generated by Django 3.0.8 on 2020-10-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201016_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mobile_num',
            field=models.CharField(max_length=12),
        ),
    ]
