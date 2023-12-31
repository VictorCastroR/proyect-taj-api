# Generated by Django 5.0 on 2023-12-29 02:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_category_staff_id_remove_service_category_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('monday', 'Lunes'), ('tuesday', 'Martes'), ('wednesday', 'Miercoles'), ('thursday', 'Jueves'), ('friday', 'Viernes'), ('saturday', 'Sabado'), ('sunday', 'Domingo')], max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='staff',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categories_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='service',
            name='staff',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='services_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workerservice',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='workerservice',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.schedule'),
        ),
        migrations.AlterField(
            model_name='workerservice',
            name='unit_of_measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.unitofmeasure'),
        ),
    ]
