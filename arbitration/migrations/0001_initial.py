# Generated by Django 4.1.1 on 2022-09-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JudgingMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamNumber', models.IntegerField()),
                ('JudgType', models.IntegerField()),
                ('MarkAndQuestions', models.JSONField()),
            ],
        ),
    ]