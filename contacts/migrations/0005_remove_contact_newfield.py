# Generated by Django 2.0.4 on 2018-05-01 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_newfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='newfield',
        ),
    ]
