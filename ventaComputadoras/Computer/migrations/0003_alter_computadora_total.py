# Generated by Django 4.0.6 on 2022-07-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Computer', '0002_alter_computadora_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]