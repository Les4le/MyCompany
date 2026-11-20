from django.test import TestCase
from django.urls import reverse


class NewswebPagesTests(TestCase):
    def test_all_five_sections_are_available(self):
        urls = [
            reverse('newsweb:home'),
            reverse('newsweb:events'),
            reverse('newsweb:achievements'),
            reverse('newsweb:articles'),
            reverse('newsweb:announcements'),
        ]
        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_unknown_section_returns_404(self):
        response = self.client.get('/media/unknown-section/')
        self.assertEqual(response.status_code, 404)
