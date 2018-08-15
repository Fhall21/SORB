# Generated by Django 2.0 on 2018-04-14 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0007_auto_20180413_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoutdata',
            name='Adventurer_Badge',
            field=models.CharField(blank=True, choices=[(None, 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('EMergencies', 'EMergencies'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Patrol Activity', 'Patrol Activity'), ('Chord', 'Chord'), ('Target Badge', 'Target Badge')], default='None', max_length=16),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Explorer_Badge',
            field=models.CharField(blank=True, choices=[(None, 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('EMergencies', 'EMergencies'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Patrol Activity', 'Patrol Activity'), ('Chord', 'Chord'), ('Target Badge', 'Target Badge')], default='None', max_length=16),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Pioneer_Badge',
            field=models.CharField(blank=True, choices=[(None, 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('EMergencies', 'EMergencies'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Patrol Activity', 'Patrol Activity'), ('Chord', 'Chord'), ('Target Badge', 'Target Badge')], default='None', max_length=16),
        ),
    ]