# Generated by Django 2.2.11 on 2020-04-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_choice_selected_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='selected_choice',
        ),
        migrations.AddField(
            model_name='question',
            name='selected_choice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]