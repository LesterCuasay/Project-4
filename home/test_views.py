from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_index_view(self):
        """
        Tests the index view
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response='home/index.html')
