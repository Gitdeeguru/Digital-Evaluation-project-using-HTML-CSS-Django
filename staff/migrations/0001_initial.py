# Generated by Django 4.1 on 2023-03-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_id', models.IntegerField()),
                ('staff_branch', models.CharField(max_length=50)),
                ('staff_gender', models.CharField(max_length=10)),
                ('staff_password', models.CharField(max_length=50)),
            ],
        ),
    ]
