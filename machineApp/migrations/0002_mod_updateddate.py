# Generated by Django 3.0.2 on 2020-01-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machineApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
