# Generated by Django 3.2.5 on 2021-09-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210925_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
