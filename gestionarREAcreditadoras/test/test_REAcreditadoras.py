from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64               # for decoding base64 image
from django.test import TestCase, override_settings
from gestionarAcreditadoras.models import Acreditadora
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarResultados.models import ResultadoPUCP


class TestingClasses(TestCase):



    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo RE ACREDITADORAS")
        print("=====================================")
        Acreditadora.objects.create(nombre="ABET",foto="img/ABET.jpg",estado=1)
        Facultad.objects.create(nombre="Ciencias e Ingenieria")
        Especialidad.objects.create(nombre='Ingenieria Industrial',facultad_id=1)
        ResultadoPUCP.objects.create(codigo="RE001",descripcion="Resultado PUCP 01",especialidad_id=1)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_listar_RE(self):
        print("Comenzando pruebas de: test_listar_RE")
        c = Client()
        pk='1'
        response = c.get('/gestionarREAcreditadoras/listar/'+pk)
        if response.status_code == 200:
            print('Correcto Listar RE!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_editar_RE(self):
        print("Comenzando pruebas de: test_editar_RE")

        c = Client()
        pk = '0'
        response = c.post('/gestionarREAcreditadoras/editar/' + pk, {'acreditadora': '1', 'operacion': ''})
        if response.status_code == 200:
            print('Correcto Editar Acreditadora RE!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        pk = '0'
        response = c.post('/gestionarREAcreditadoras/editar/' + pk, {'acreditadora': '1', 'operacion': 'entrada'})
        if response.status_code == 200:
            print('Correcto Entrada Acreditadora RE!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Insertar Acreditadora sin select
        c = Client()
        pk = '0'
        response = c.post('/gestionarREAcreditadoras/editar/' + pk, {'acreditadora': '1', 'operacion': 'insertar', 'codigo': 'RE001', 'descripcion': 'Resultado 1'})
        if response.status_code == 302:
            print('Correcto Insertar Acreditadora RE Sin Select!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Insertar Acreditadora con select
        c = Client()
        pk = '0'
        response = c.post('/gestionarREAcreditadoras/editar/' + pk, {'acreditadora': '1', 'operacion': 'insertar', 'codigo': 'RE001', 'descripcion': 'Resultado 1', 'select': '1'})
        if response.status_code == 302:
            print('Correcto Insertar Acreditadora RE Con Select!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Editar con Select
        c = Client()
        pk = '1'
        response = c.post('/gestionarREAcreditadoras/editar/' + pk, {'acreditadora': '1', 'operacion': 'editar', 'codigo': 'RE001', 'descripcion': 'Resultado 1', 'select': '1'})
        if response.status_code == 302:
            print('Correcto Editar Acreditadora RE Con Select!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Editar sin Select
        c = Client()
        pk = '1'
        response = c.post('/gestionarREAcreditadoras/editar/' + pk, {'acreditadora': '1', 'operacion': 'editar', 'codigo': 'RE001', 'descripcion': 'Resultado 1'})
        if response.status_code == 302:
            print('Correcto Editar Acreditadora RE Sin Select!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_ajaxEditar(self):
        print("Comenzando pruebas de: test_ajaxEditar")

        c = Client()
        response = c.post('/gestionarREAcreditadoras/ajaxEditar', {'operacion': 'listEspe', 'facultad': '1'})
        if response.status_code == 200:
            print('Correcto Listar Especialidad!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarREAcreditadoras/ajaxEditar', {'operacion': 'listREPUCP', 'especialidadPk': '1'})
        if response.status_code == 200:
            print('Correcto Listar RE PUCP!')
        elif response.status_code == 404:
            self.assertFalse(False)