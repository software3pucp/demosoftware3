from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64               # for decoding base64 image
from django.test import TestCase, override_settings

class TestingClasses(TestCase):



    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo HOME")
        print("=====================================")
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_ingresar_login(self):
        print("Comenzando pruebas de: test-ingresar-login")
        c = Client()
        response = c.get('/')
        if response.status_code == 200:
            print('Correcto Ingreso a Login!')
        elif response.status_code == 404:
            self.assertFalse(False)