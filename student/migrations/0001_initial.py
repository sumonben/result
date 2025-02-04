# Generated by Django 5.1.4 on 2024-12-13 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('title_en', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=0)),
                ('roll', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('session', models.CharField(blank=True, max_length=15, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.ManyToManyField(blank=True, null=True, to='student.group')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=10)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(blank=True, max_length=20, null=True)),
                ('group', models.ManyToManyField(blank=True, null=True, to='student.group')),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField(default=0)),
                ('roll', models.CharField(max_length=10)),
                ('MCQ', models.IntegerField(default=0)),
                ('CQ', models.IntegerField(default=0)),
                ('practical', models.IntegerField(default=0)),
                ('grade', models.CharField(blank=True, max_length=150, null=True)),
                ('cpa', models.CharField(blank=True, max_length=150, null=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.subject')),
            ],
            options={
                'ordering': ['serial'],
            },
        ),
    ]
