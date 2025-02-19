# Generated by Django 4.2.10 on 2024-03-10 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("publication", "0002_publication_preview_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="publication",
            name="pub_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date published"
            ),
        ),
    ]
