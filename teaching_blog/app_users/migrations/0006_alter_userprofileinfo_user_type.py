# Generated by Django 4.1.5 on 2023-01-12 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0005_alter_userprofileinfo_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=10),
        ),
    ]
