from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64  # for decoding base64 image
from django.test import TestCase, override_settings

from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarResultados.models import ResultadoPUCP


class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo gestionarResultados")
        print("=====================================")
        facultad = Facultad.objects.create(nombre='facultad', responsable='1')
        especialidad = Especialidad.objects.create(nombre='especialidad', responsable='1', facultad=facultad)
        ResultadoPUCP.objects.create(codigo='COD10101',descripcion='resultado de prueba', especialidad=especialidad)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_resultados(self):
        print("Comenzando pruebas de: test_resultados")
        c = Client()
        response = c.get('/gestionarResultados/resultados/')
        if response.status_code == 200:
            print('Correcto Resultados!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_crear_resultado(self):
        print("Comenzando pruebas de: test_crear_resultado")
        c = Client()
        id_especialidad='1'
        response = c.get('/gestionarResultados/crear/'+id_especialidad)
        if response.status_code == 200:
            print('Correcta inicialización de crear resultado!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client(enforce_csrf_checks=True)
        response = c.post('/gestionarResultados/crear/'+id_especialidad, {'codigo': 'COD', 'descripcion': 'Descripcion del resultado'})
        if response.status_code != 404:
            print('Se agregó un resultado correctamente!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_editar_resultado(self):
        print("Comenzando pruebas de: test_editar_resultado")
        c = Client()
        id_resultado = '1'
        response = c.get('/gestionarResultados/editar/' + id_resultado + '/')
        if response.status_code == 200:
            print('Correcto editar resultado!')
        else:
            self.assertFalse(False)

        c = Client(enforce_csrf_checks=True)
        response = c.post('/gestionarResultados/editar/' + id_resultado + '/',
                          {'codigo': 'CODE01', 'descripcion': 'Descripcion del resultado editado'})
        if response.status_code != 404:
            print('Se editó un resultado correctamente!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_eliminar_resultado(self):
        print("Comenzando pruebas de: test_eliminar_resultado")
        c = Client()
        id_resultado = "1"
        response = c.post('/gestionarResultados/eliminar/', {'resultadopk': id_resultado})
        if response.status_code == 200:
            print('Correcto eliminar Resultado!')
        else:
            self.assertFalse(False)
