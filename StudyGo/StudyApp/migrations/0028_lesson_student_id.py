# Generated by Django 4.1.7 on 2023-04-25 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudyApp', '0027_remove_lesson_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='student_id',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='StudyApp.student'),
            preserve_default=False,
        ),
    ]
