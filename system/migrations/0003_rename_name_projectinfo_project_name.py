# Generated by Django 3.2.13 on 2022-08-27 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_projectinfo_verification_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectinfo',
            old_name='name',
            new_name='project_name',
        ),
    ]