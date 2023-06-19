from django.test import TestCase


class HomePageTest(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        content = response.content.decode('utf-8')
        self.assertTrue(content.startswith('<html>'))
        self.assertIn("<title>TO-DO</title>", content)
        self.assertTrue(content.endswith('</html>'))
