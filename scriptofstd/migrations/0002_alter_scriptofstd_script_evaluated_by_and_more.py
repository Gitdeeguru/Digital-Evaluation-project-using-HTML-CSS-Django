# Generated by Django 4.1 on 2023-03-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scriptofstd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_evaluated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_evaluation_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_final_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_ist_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_pdf',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_progress',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_second_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scriptofstd',
            name='script_upload_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
