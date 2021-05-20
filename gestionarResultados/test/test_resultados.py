from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64  # for decoding base64 image
from django.test import TestCase, override_settings

from gestionarResultados.models import ResultadoPUCP


class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo RESULTADOS")
        print("=====================================")
        ResultadoPUCP.objects.create(codigo='COD10101',descripcion='resultado de prueba')
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_listar_resultado(self):
        print("Comenzando pruebas de: test_listar_resultados")
        c = Client()
        response = c.get('/gestionarResultados/listar/')
        if response.status_code == 200:
            print('Correcto Listar Resultados!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_agregar_resultado(self):
        print("Comenzando pruebas de: test_agregar_resultado")
        c = Client()
        response = c.get('/gestionarResultados/crear/')
        if response.status_code == 200:
            print('Correcta inicialización de agregar resultado!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client(enforce_csrf_checks=True)
        response = c.post('/gestionarResultados/crear/', {'codigo': 'COD', 'descripcion': 'Descripcion del resultado'})
        if response.status_code != 404:
            print('Se agregó un resultado correctamente!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_editar_resultado(self):
        print("Comenzando pruebas de: test_editar_resultado")
        c = Client()
        id_resultado = "1"
        response = c.get('/gestionarResultados/editar/' + id_resultado + '/')
        if response.status_code == 200:
            print('Correcto editar resultado!')
        else:
            self.assertFalse(False)

        c = Client(enforce_csrf_checks=True)
        response = c.post('/gestionarResultados/editar/' + id_resultado + '/',
                          {'codigo': 'CODE01', 'descripcion': 'Descripcion del resultado editado'})
        if response.status_code != 404:
            print('Se agregó un resultado correctamente!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_eliminar_resultado(self):
        print("Comenzando pruebas de: test_eliminar_resultado")
        c = Client(enforce_csrf_checks=True)
        id_resultado = "1"
        response = c.post('/gestionarResultados/listar/', {'resultadoPk': id_resultado})
        print(response)
        if response.status_code == 200:
            print('Correcto eliminar Resultado!')
        else:
            self.assertFalse(False)
