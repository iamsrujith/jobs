# Generated by Django 3.1.7 on 2021-04-16 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210411_1207'),
        ('jobs_app', '0009_auto_20210416_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='usertype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.usertype'),
        ),
    ]