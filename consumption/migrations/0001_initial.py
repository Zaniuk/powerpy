# Generated by Django 4.1.5 on 2023-01-17 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('powermeter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consumption', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='powermeter.powermeter', to_field='meter_id')),
            ],
        ),
    ]
