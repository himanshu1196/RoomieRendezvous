# Generated by Django 4.2 on 2023-11-21 03:35

from django.db import migrations, models
import rrapp.models


class Migration(migrations.Migration):
    dependencies = [
        ("rrapp", "0009_alter_user_profile_picture_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                default="DefaultProfile.jpg", upload_to=rrapp.models.user_directory_path
            ),
        ),
    ]