# Generated by Django 3.2.13 on 2022-09-19 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0006_algorithm_event_type'),
        ('interface', '0003_auto_20220919_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benzhisubscription',
            name='algorithm',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='algorithm.algorithm'),
        ),
    ]