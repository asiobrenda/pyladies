# Generated by Django 2.2 on 2024-01-23 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repeat', '0003_author_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(blank=True, max_length=700)),
            ],
            options={
                'verbose_name_plural': 'CDistrict',
            },
        ),
        migrations.CreateModel(
            name='DistrictValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.SmallIntegerField(default=0)),
                ('district_value', models.IntegerField(null=True)),
                ('district_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='county_data', to='repeat.CDistrict')),
            ],
            options={
                'verbose_name_plural': 'DistrictValue',
            },
        ),
    ]
