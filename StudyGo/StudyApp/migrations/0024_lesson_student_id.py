# Generated by Django 4.1.7 on 2023-04-25 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyApp', '0023_rename_subject_lesson_subject_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='student_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='StudyApp.student'),
            preserve_default=False,
        ),
    ]