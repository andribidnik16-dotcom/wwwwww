from django.db import migrations, models


def create_default_profile(apps, schema_editor):
    site_profile = apps.get_model("links", "SiteProfile")
    site_profile.objects.get_or_create(pk=1)


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("display_name", models.CharField(default="WESTY", max_length=80, verbose_name="Display name")),
                ("username", models.CharField(default="@WESTY", max_length=80, verbose_name="Username")),
                ("quote", models.CharField(blank=True, default="Роби з душею — і результат говоритиме сам за себе.", max_length=180, verbose_name="Quote shown below your name")),
                ("avatar_url", models.URLField(blank=True, verbose_name="Avatar image URL")),
                ("telegram_url", models.URLField(blank=True, verbose_name="My Telegram link")),
                ("tiktok_url", models.URLField(blank=True, verbose_name="TikTok link")),
                ("info_url", models.URLField(blank=True, verbose_name="Info link")),
                ("stars_url", models.URLField(blank=True, verbose_name="Stars link")),
                ("premium_url", models.URLField(blank=True, verbose_name="Telegram Premium link")),
                ("contact_url", models.URLField(blank=True, verbose_name="Contact link")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
            ],
            options={
                "verbose_name": "Profile and links",
                "verbose_name_plural": "Profile and links",
            },
        ),
        migrations.RunPython(create_default_profile, migrations.RunPython.noop),
    ]
