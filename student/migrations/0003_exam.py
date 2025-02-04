# Generated by Django 5.1.4 on 2024-12-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_marks_total_alter_marks_cq_alter_marks_mcq_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('title_en', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
    ]
