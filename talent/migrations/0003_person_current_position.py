# Generated by Django 4.2.2 on 2023-08-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("talent", "0002_person_linkedin_link_person_twitter_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="current_position",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
