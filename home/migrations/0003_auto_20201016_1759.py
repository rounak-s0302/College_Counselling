# Generated by Django 3.0.8 on 2020-10-16 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201009_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='creat_at',
            new_name='create_at',
        ),
    ]
