# Generated by Django 3.1.7 on 2021-04-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_canreg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canreg',
            name='gender',
            field=models.CharField(default='male', max_length=10, null=True),
        ),
    ]
