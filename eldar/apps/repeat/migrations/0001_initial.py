# Generated by Django 2.2 on 2024-01-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TennisClub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('date_joined', models.DateField(auto_now=True)),
            ],
        ),
    ]
