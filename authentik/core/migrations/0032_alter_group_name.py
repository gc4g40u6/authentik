# Generated by Django 4.1.10 on 2023-07-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_core", "0031_alter_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.TextField(verbose_name="name"),
        ),
    ]
