# Generated by Django 3.0.5 on 2020-08-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='repo_issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('label', models.IntegerField(max_length=50)),
            ],
        ),
    ]
