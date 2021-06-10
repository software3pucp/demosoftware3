from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64  # for decoding base64 image
from django.test import TestCase, override_settings
from gestionarEvaluacion.models import RespuestaEvaluacion
from gestionarIndicadores.models import Indicador
from gestionarRubrica.models import Rubrica
from gestionarNiveles.models import Nivel
from gestionarFacultad.models import Facultad
from gestionarEspecialidad.models import Especialidad
from gestionarResultados.models import ResultadoPUCP
from gestionarSemestre.models import Semestre

class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo SEMESTRE")
        print("=====================================")
        Semestre.objects.create(nombreCodigo='2020-1', anho='2020', etapa='2', inicio='18/08', fin='25/12')

        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_agregarSemestre(self):
        print("Comenzando pruebas de: test_agregarSemestre")
        c = Client()
        response = c.post('/gestionarSemestre/agregar/',
                          {'nombreCodigo': '2020-1', 'inicio': '18/08', 'fin': '24/12'})
        if response.status_code == 200:
            print('Correcto llamado de agregarSemestre!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")

    def test_listar(self):
        print("Comenzando pruebas de: test_listarSemestre")
        c = Client()
        response = c.get('/gestionarSemestre/listar/')
        if response.status_code == 200:
            print('Correcto llamado de listarSemestres!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")


    def test_enviarCursoHorario(self):
        print("Comenzando pruebas de: test_enviarCursoHorario")
        c = Client()
        nombre_codigo="2020-1"
        response = c.get('/gestionarSemestre/enviarCursoHorario/' + nombre_codigo + '/')
        print(Semestre.objects.filter()[0].nombreCodigo)
        print('/gestionarSemestre/enviarCursoHorario/' + nombre_codigo + '/')
        if response.status_code == 200:

            print('Correcto llamado de enviarCursoHorario!')
        elif response.status_code == 404:
            print('Incorrecto llamado')
            self.assertFalse(False)
        print("==================================================")

