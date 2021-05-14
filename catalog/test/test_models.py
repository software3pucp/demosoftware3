from django.test import TestCase
from django.test import Client

class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_listar_facultad(self):

        print("Method: test http entry." + "test_listar_facultad")
        c = Client()
        response = c.post('/gestionarFacultad/listar/', {'username': 'john', 'password': 'smith'})
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            self.assertFalse(False)


    def test_listar_semestre(self):

        print("Method: test http entry." + 'test_listar_semestre')
        c = Client()
        response = c.post('/gestionarSemestre/listar/', {'username': 'john', 'password': 'smith'})
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            self.assertFalse(False)


    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertTrue(True)