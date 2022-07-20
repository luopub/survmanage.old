# Generated by Django 3.2.7 on 2022-07-20 13:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('algorithm', '0001_initial'),
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='报警时间')),
                ('img', models.CharField(max_length=256, verbose_name='报警图片')),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='algorithm.algorithm', verbose_name='算法')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel', verbose_name='报警通道')),
            ],
        ),
    ]
