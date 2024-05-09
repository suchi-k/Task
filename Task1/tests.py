from django.test import TestCase,Client
class BasicTests(TestCase):
    def test_1(self):
        self.assertTrue(1==1)
        self.assertTrue(1==2)

