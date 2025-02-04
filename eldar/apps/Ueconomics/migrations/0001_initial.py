# Generated by Django 2.2 on 2024-01-11 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitc2', models.PositiveIntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Source',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Source',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='YearData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.BigIntegerField(blank=True)),
                ('value', models.BigIntegerField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Ueconomics.Product')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_type', to='Ueconomics.Source')),
            ],
            options={
                'verbose_name_plural': 'Source',
                'ordering': ['id'],
            },
        ),
    ]
