# Generated by Django 4.1.7 on 2023-04-28 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudyApp', '0032_student_submission'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_submission',
            old_name='feedback',
            new_name='submission_file',
        ),
        migrations.RenameField(
            model_name='student_submission',
            old_name='feedback_reply',
            new_name='submission_reply',
        ),
    ]
