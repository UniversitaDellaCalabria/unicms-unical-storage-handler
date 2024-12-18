# Generated by Django 4.2.9 on 2024-12-12 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("unicms_unical_storage_handler", "0002_alter_webpathcdscod_cds_cod"),
    ]

    operations = [
        migrations.CreateModel(
            name="CdsWebsiteHomeBlocks",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.IntegerField(blank=True, default=10, null=True)),
                (
                    "section",
                    models.CharField(
                        blank=True,
                        choices=[("", "-")],
                        help_text="Specify the container section in the template where this block would be rendered.",
                        max_length=60,
                        null=True,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "block",
                    models.ForeignKey(
                        limit_choices_to={"is_active": True},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cmstemplates.templateblock",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
