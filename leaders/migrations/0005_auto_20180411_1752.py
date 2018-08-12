# Generated by Django 2.0 on 2018-04-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0004_auto_20180411_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoutdata',
            name='Adventurer_Badge',
            field=models.CharField(blank=True, choices=[('', 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Chord', 'Chord')], default='None', max_length=2),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Explorer_Badge',
            field=models.CharField(blank=True, choices=[('', 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Chord', 'Chord')], default='None', max_length=2),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Pioneer_Badge',
            field=models.CharField(blank=True, choices=[('', 'Click here to select the badge'), ('Campcraft', 'Campcraft'), ('Citizenship', 'Citizenship'), ('Air Activities', 'Air Activities'), ('Construction', 'Construction'), ('Environment', 'Environment'), ('Water Activities', 'Water Activities'), ('Water Safety', 'Water Safety'), ('Target Badge', 'Target Badge'), ('Chord', 'Chord')], default='None', max_length=2),
        ),
        migrations.AlterField(
            model_name='scoutdata',
            name='Proficiency_Badge',
            field=models.CharField(blank=True, choices=[('', 'Click here to select the badge'), ('Agriculture', 'Agriculture'), ('Animal Keeper', 'Animal Keeper'), ('Anthropology', 'Anthropology'), ('Art', 'Art'), ('Astronomy', 'Astronomy'), ('Bushcraft', 'Bushcraft'), ('Caving', 'Caving'), ('Collector', 'Collector'), ('Commerce', 'Commerce'), ('Communication', 'Communication'), ('Community', 'Community'), ('Craft', 'Craft'), ('Crime Prevention', 'Crime Prevention'), ('Entertainer', 'Entertainer'), ('Fire_Awareness', 'Fire Awareness'), ('Heritage', 'Heritage'), ('Induvidual Sportsman', 'Induvidual Sportsman'), ('IT', 'I.T.'), ('Literacy Arts', 'Literacy Arts'), ('Modeller', 'Modeller'), ('Multi-Media', 'Multi-Media'), ('Music', 'Music'), ('Outdoor', 'Outdoor'), ('Performing Arts', 'Performing Arts'), ('Rock Climbing', 'Rock Climbing'), ('Science', 'Science'), ('Team Sports', 'Team Sports'), ('Technology', 'Technology'), ('Trades', 'Trades'), ('World Scouting', 'World Scouting')], default='None', max_length=2),
        ),
    ]
