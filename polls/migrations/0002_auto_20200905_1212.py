# Generated by Django 3.1.1 on 2020-09-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askqua',
            name='ans',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='askqua',
            name='qua',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]