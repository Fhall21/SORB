# Generated by Django 2.1.3 on 2018-11-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=80)),
                ('subscription', models.CharField(choices=[('Basic', 'Basic'), ('Premium', 'Premium')], default='Basic', max_length=8)),
            ],
        ),
    ]
