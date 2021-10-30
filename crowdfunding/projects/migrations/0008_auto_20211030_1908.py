# Generated by Django 3.2.5 on 2021-10-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_perk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='close_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
