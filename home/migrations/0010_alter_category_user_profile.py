# Generated by Django 5.0.2 on 2024-02-22 08:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_category_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile'),
        ),
    ]
