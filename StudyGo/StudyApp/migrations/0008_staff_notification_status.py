# Generated by Django 4.1.7 on 2023-03-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyApp', '0007_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]