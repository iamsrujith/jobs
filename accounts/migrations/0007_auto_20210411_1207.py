# Generated by Django 3.1.7 on 2021-04-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210411_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canreg',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
