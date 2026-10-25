from django.db import migrations


def update_default_quote(apps, schema_editor):
    SiteProfile = apps.get_model("links", "SiteProfile")
    SiteProfile.objects.filter(quote="Stay focused. Keep building.").update(
        quote="Роби з душею — і результат говоритиме сам за себе."
    )


class Migration(migrations.Migration):
    dependencies = [
        ("links", "0002_remove_siteprofile_contact_url_and_more"),
    ]

    operations = [
        migrations.RunPython(update_default_quote, migrations.RunPython.noop),
    ]
