# Generated by Django 4.2.5 on 2023-09-16 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo", "0003_book_cover_book_description_book_is_published_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="published",
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
