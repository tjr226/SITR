# Generated by Django 2.0.4 on 2018-05-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_remove_contact_seven'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='newfield',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
