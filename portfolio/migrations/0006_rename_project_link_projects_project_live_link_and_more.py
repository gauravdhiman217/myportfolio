# Generated by Django 4.1.6 on 2023-02-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_contact_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='Project_Link',
            new_name='Project_Live_Link',
        ),
        migrations.AddField(
            model_name='projects',
            name='Project_github_Link',
            field=models.CharField(default='', max_length=200),
        ),
    ]