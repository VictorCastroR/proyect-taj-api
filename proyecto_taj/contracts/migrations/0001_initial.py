# Generated by Django 5.0 on 2023-12-29 02:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0003_schedule_unitofmeasure_alter_category_staff_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifications', models.TextField()),
                ('notes_worker', models.TextField(blank=True, null=True)),
                ('price_updated', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('evaluation', 'Evaluation'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='evaluation', max_length=20)),
                ('evaluation_notes', models.TextField(blank=True, null=True)),
                ('discount_offered', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('price_increase_reason', models.TextField(blank=True, null=True)),
                ('estimated_completion_time', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('rating_by_consumer', models.IntegerField(blank=True, null=True)),
                ('rating_by_worker', models.IntegerField(blank=True, null=True)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumer_contracts', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='services.workerservice')),
            ],
        ),
    ]
