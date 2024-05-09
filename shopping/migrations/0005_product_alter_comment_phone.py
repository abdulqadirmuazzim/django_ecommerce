# Generated by Django 5.0.4 on 2024-05-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0004_alter_comment_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Pname", models.CharField(max_length=50)),
                ("image", models.URLField(max_length=500)),
                ("price", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="comment",
            name="phone",
            field=models.CharField(
                help_text="Enter phone e.g +1 123-456-7980", max_length=15
            ),
        ),
    ]
