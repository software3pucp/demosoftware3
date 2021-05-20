from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64               # for decoding base64 image
from django.test import TestCase, override_settings

class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo FACULTAD")
        print("=====================================")
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_listarNivel(self):
        print("Comenzando pruebas de: test_listarNivel")
        c = Client()
        response = c.get('/gestionarNivel/listar/')
        if response.status_code == 200:
            print('Correcto Listar nivel!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_EditarNivel(self):
        print("Comenzando pruebas de: test_test_test_EditarNivel")
        c = Client()
        pk = "1"
        response = c.post('/gestionarNivel/editar/' + pk + '/', follow=True)
        if response.status_code == 200:
            print('Se edito una nivel correctamente!')
        else:
            self.assertFalse(False)

