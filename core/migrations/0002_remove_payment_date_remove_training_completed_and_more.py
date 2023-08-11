# Generated by Django 4.2.4 on 2023-08-07 07:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='training',
            name='completed',
        ),
        migrations.AddField(
            model_name='payment',
            name='dt',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='training',
            name='status',
            field=models.CharField(choices=[('A', 'отлично'), ('B', 'хорошо'), ('C', 'удовлетворительно'), ('D', 'неудовлетворительно'), ('F', 'плохо')], default='S', max_length=1, verbose_name='статус тренировки'),
        ),
    ]
