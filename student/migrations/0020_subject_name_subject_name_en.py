# Generated by Django 5.1.4 on 2024-12-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_remove_subject_name_remove_subject_name_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
