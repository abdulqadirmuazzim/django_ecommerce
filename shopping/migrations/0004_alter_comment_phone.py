# Generated by Django 5.0.4 on 2024-05-04 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0003_rename_contactform_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="phone",
            field=models.CharField(max_length=15),
        ),
    ]
