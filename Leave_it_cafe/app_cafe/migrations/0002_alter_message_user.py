# Generated by Django 4.1.3 on 2022-12-11 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0001_initial'),
        ('app_cafe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_home.profile'),
        ),
    ]
