# Generated by Django 3.2.13 on 2022-10-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0006_auto_20221029_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='benzhireporturl',
            name='platform_name',
            field=models.CharField(default='本质', max_length=32, verbose_name='Report Platform Name'),
        ),
    ]
