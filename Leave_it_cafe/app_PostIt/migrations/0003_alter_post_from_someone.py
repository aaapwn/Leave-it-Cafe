# Generated by Django 4.1.3 on 2022-12-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_PostIt', '0002_post_from_someone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='from_someone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
