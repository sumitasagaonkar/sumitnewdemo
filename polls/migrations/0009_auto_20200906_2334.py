# Generated by Django 3.1.1 on 2020-09-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200906_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='Last_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='frist_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='status',
            field=models.CharField(choices=[('Arrange Program', 'Arrange Program'), ('Appointment', 'Appointment'), ('Other Reason ', 'Other Reason')], max_length=200, null=True),
        ),
    ]
