# Generated by Django 2.0 on 2018-04-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scout_group',
            name='Group',
            field=models.CharField(choices=[(None, 'Click here to select the group'), ('BC', 'Brisbane_Central_Scout')], default='None', max_length=27),
        ),
    ]
