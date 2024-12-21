# Generated by Django 5.1.4 on 2024-12-21 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_adress_branch_class_department_district_division_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fourth_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
