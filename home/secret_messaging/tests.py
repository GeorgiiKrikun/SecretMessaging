from django.test import TestCase
from django.test import Client
from .InvisibleSymbolBinary import make_string_invisible, make_string_visible, extract_important_symbols, i_0, i_1

# Create your tests here.

class InvisibleSymbolBinaryTestCase(TestCase):
    def test_basic_workflow(self):
        s = "Hello, World!"
        result = make_string_invisible(s)
        for c in result:
            self.assertTrue(c in [i_0, i_1])
        self.assertTrue (s == make_string_visible(result))
        
    def test_extract_important_symbols(self):
        s = "Hello, World!"
        result = make_string_invisible(s)
        result_with_stuff = "a" + result + "b"
        self.assertEqual(s, make_string_visible(extract_important_symbols(result)))

class ViewsTestCase(TestCase):        
    def test_encryption_page(self):
        c = Client()
        response = c.get('/secret_messaging/')
        self.assertEqual(response.status_code, 200)
        response = c.post('/secret_messaging/', {'message': 'Hello', 'secret': 'World'})
        secret_string = response.context['secret_string']
        self.assertEqual(make_string_visible(extract_important_symbols(secret_string)), 'World')
    
    def test_decryption_page(self):
        c = Client()
        response = c.get('/secret_messaging/reveal_secret/')
        self.assertEqual(response.status_code, 200)
        response = c.post('/secret_messaging/reveal_secret/', {'secret_string': "Hello" + make_string_invisible('World')})
        secret_string = response.context['secret_string']
        self.assertEqual(secret_string, 'World')
