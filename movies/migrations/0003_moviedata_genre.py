# Generated by Django 4.1.7 on 2023-03-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_rename_ratin_moviedata_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviedata",
            name="genre",
            field=models.CharField(default="action", max_length=200),
        ),
    ]