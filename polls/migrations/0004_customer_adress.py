# Generated by Django 3.1.1 on 2020-09-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_askqua_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='adress',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
