# Generated by Django 5.1.4 on 2024-12-25 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_result_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='section',
            new_name='sect',
        ),
    ]
