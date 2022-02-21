from django.test import TestCase
from selenium import webdriver

from .forms import HashForm

# class FunctionalTestCase(TestCase):

#     def setUp(self):
#         self.browser = webdriver.Chrome()

#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('install', self.browser.page_source)

#     def tearDown(self):
#         self.browser.quit()
    
class UnitTestCase(TestCase):
    
    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data={'text':'hello'})
        self.assertTrue(form.is_valid())