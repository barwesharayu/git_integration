# Generated by Django 3.0.5 on 2020-08-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo_issues',
            name='label',
            field=models.IntegerField(),
        ),
    ]
