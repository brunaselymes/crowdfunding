# Generated by Django 3.2.5 on 2021-09-16 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_pledge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category',
            new_name='categoryId',
        ),
    ]
