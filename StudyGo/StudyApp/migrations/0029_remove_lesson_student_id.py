# Generated by Django 4.1.7 on 2023-04-25 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudyApp', '0028_lesson_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='student_id',
        ),
    ]
