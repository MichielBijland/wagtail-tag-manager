# Generated by Django 2.1.3 on 2018-12-06 11:08

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0002_auto_20181111_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookiedeclaration',
            name='duration_period',
            field=models.CharField(blank=True, choices=[('session', 'Session'), ('seconds+', 'Second(s)'), ('minutes+', 'Minute(s)'), ('hours+', 'Hour(s)'), ('days+', 'Day(s)'), ('weeks+', 'Week(s)'), ('months+', 'Month(s)'), ('years+', 'Year(s)')], help_text='The period after which the cookie will expire.<br/><b>Session:</b> the cookie will expire when the browser is closed.', max_length=10, null=True),
        ),
    ]
