# Generated by Django 3.0.6 on 2020-05-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=15, null=True),
        ),
    ]