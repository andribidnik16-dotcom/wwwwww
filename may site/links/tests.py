from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ProfileLink, SiteProfile


class ProfileLinksPageTests(TestCase):
    def test_home_page_shows_profile_and_english_link_labels(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "WESTY")
        self.assertContains(response, "Роби з душею")
        for label in ("My Telegram", "TikTok", "Info", "Stars", "Telegram Premium", "Price", "Contact me"):
            with self.subTest(label=label):
                self.assertContains(response, label)

    def test_configured_urls_are_rendered_as_links(self):
        profile = SiteProfile.get_profile()
        ProfileLink.objects.create(
            profile=profile,
            title="My Telegram",
            url="https://t.me/westy",
            sort_order=20,
        )

        response = self.client.get(reverse("home"))

        self.assertContains(response, 'href="https://t.me/westy"')
        self.assertContains(response, "Price")

    def test_inactive_links_are_hidden_and_active_links_keep_admin_order(self):
        profile = SiteProfile.get_profile()
        profile.links.all().delete()
        ProfileLink.objects.create(
            profile=profile,
            title="TikTok",
            url="https://www.tiktok.com/@westy",
            sort_order=20,
            is_active=False,
        )
        ProfileLink.objects.create(
            profile=profile,
            title="My Telegram",
            url="https://t.me/westy",
            sort_order=10,
        )

        response = self.client.get(reverse("home"))

        self.assertContains(response, 'href="https://t.me/westy"')
        self.assertNotContains(response, 'href="https://www.tiktok.com/@westy"')
        self.assertNotContains(response, "TikTok")

    def test_admin_can_edit_profile_links(self):
        user = get_user_model().objects.create_superuser(
            username="profile-admin",
            email="profile@example.com",
            password="A-Long-Test-Password-984!",
        )
        self.client.force_login(user)
        response = self.client.get("/admin/links/siteprofile/1/change/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add another Page link")
