from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):
    
    def test_home_page(self):
        response = self.client.get('/')
        content = response.content.decode('utf-8')
        self.assertTrue(content.startswith('<html>'))
        self.assertIn("<title>TO-DO</title>", content)
        self.assertTrue(content.endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')
        
    def test_only_saves_items_when_neccessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)
    

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()
        
        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")
        
        
class ListViewTest(TestCase):
    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world')
        self.assertTemplateUsed(response, 'list.html')
        

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new',  data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.first().text, "A new list item")
        
    def test_redirect_after_POST(self):
        response = self.client.post('/lists/new',  data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world')
        