# Generated by Django 2.2 on 2024-03-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
