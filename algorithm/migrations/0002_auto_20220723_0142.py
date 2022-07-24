# Generated by Django 3.2.7 on 2022-07-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algorithm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='name_ch',
            field=models.CharField(default='', max_length=32, verbose_name='中文名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='name',
            field=models.CharField(max_length=32, verbose_name='英文名称'),
        ),
    ]