# Generated by Django 3.2.3 on 2021-07-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseDist', '0003_auto_20210730_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isSessional',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
