# Generated by Django 2.1.3 on 2018-12-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='troop',
            field=models.SlugField(default='None', max_length=27),
        ),
    ]
