# Generated by Django 2.2 on 2024-01-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabs', '0002_auto_20240124_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Person',
            },
        ),
    ]
