# Generated by Django 2.1.3 on 2018-12-08 05:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('troop', models.SlugField(choices=[('NA', 'Admin')], default='None', max_length=27)),
                ('role', models.CharField(choices=[('Leader', 'Leader'), ('Scout', 'Scout')], default='Scout', max_length=7)),
                ('date_of_birth', models.DateField(default=datetime.date.today, null=True)),
                ('secondary_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('scout_username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
