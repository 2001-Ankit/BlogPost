# Generated by Django 5.0.2 on 2024-02-23 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_userprofile_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='category',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='category',
            field=models.ManyToManyField(to='home.category'),
        ),
    ]
