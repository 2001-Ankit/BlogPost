# Generated by Django 5.0.2 on 2024-02-22 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_userprofile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
