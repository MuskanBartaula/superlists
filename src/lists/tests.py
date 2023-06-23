from django.test import TestCase


class HomePageTest(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        content = response.content.decode('utf-8')
        self.assertTrue(content.startswith('<html>'))
        self.assertIn("<title>TO-DO</title>", content)
        self.assertTrue(content.endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')
        
    def test_can_save_a_POST_request(self):
        response = self.client.post('/',  data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')