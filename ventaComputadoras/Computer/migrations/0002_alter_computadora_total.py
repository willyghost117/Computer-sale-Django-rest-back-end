# Generated by Django 4.0.6 on 2022-07-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]