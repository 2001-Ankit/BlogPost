# Generated by Django 5.0.2 on 2024-02-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_category_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user_profile',
        ),
    ]