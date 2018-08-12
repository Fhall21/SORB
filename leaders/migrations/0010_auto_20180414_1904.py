# Generated by Django 2.0 on 2018-04-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0009_auto_20180414_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoutdata',
            name='Adventurer_Badge',
            field=models.CharField(blank=True, choices=[(None, 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('Emergencies', 'Emergencies'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Patrol Activity', 'Patrol Activity'), ('Chord', 'Chord'), ('Target Badge', 'Target Badge')], default='None', max_length=22),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Explorer_Badge',
            field=models.CharField(blank=True, choices=[(None, 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('Emergencies', 'Emergencies'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Patrol Activity', 'Patrol Activity'), ('Chord', 'Chord'), ('Target Badge', 'Target Badge')], default='None', max_length=22),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Pioneer_Badge',
            field=models.CharField(blank=True, choices=[(None, 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('Emergencies', 'Emergencies'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Patrol Activity', 'Patrol Activity'), ('Chord', 'Chord'), ('Target Badge', 'Target Badge')], default='None', max_length=22),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Proficiency_Badge',
            field=models.CharField(blank=True, default='None', max_length=20),
        ),
    ]
