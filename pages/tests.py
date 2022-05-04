from django.test import SimpleTestCase
from django.urls import reverse


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Hello, world!")

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_about_page_contains_content(self):
        response = self.client.get("/about/")
        self.assertContains(response, "Hi, my name is Caleb Bituin and I am learning to become a full stack web developer.")

    def test_about_page_uses_correct_templates(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_reverse_lookup(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_about_page_reverse_lookup(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")