# Generated by Django 4.1.7 on 2023-03-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudyApp', '0012_rename_student_feedback_student_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_notification',
            old_name='feedback',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='student_notification',
            name='feedback_reply',
        ),
        migrations.RemoveField(
            model_name='student_notification',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='student_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
