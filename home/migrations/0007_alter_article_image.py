# Generated by Django 4.1.1 on 2022-10-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(
                default="uploads/articles/noimage.png",
                null=True,
                upload_to="uploads/articles/",
            ),
        ),
    ]