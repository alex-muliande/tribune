from django.test import TestCase
from .models import Editor,Article,tags
# Create your tests here.

class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.alex=Editor(first_name ='Alex', last_name = 'Muliande', email = 'alexnad425@gmail.com')
    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.alex,Editor))

    #Testing Save Method
    def test_save_method(self):
        self.alex.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
