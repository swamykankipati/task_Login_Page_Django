# Generated by Django 3.0.6 on 2020-05-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20200525_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='emailId',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
