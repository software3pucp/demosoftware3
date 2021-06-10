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
class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Inicio de prueba del módulo EVALUACION          ||")
        print("==================================================")
        RespuestaEvaluacion.objects.create(nombreAlumno='Mario Calderon', codigoAlumno='20101585')
        Nivel.objects.create(name='Inicial',value=1,estado="1")
        ResultadoPUCP.objects.create(codigo='RE01', estado='1', descripcion='Resultado del estudiante de pruebas 1')
        Indicador.objects.create(codigo='ID101',descripcion='2.1 Diseña una solucion informatica bvuscando satisfacer necesidades.',
                                 estado=1,resultado_id = '1')
        Facultad.objects.create(nombre='Ciencias e Ingenieria', responsable='1', foto='imagen')
        Especialidad.objects.create(nombre='Ingenieria Informatica',responsable='1',foto='imagen',facultad_id= 1)
        Rubrica.objects.create(descripcion='Nivel 1 del indicador ID101',especialidad_id=1,indicador_id=1,nivel_id=1)

        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_evaluar(self):
        print("Comenzando pruebas de: test_evaluar")
        c = Client()
        response = c.get('/gestionarEvaluacion/evaluar/')
        if response.status_code == 200:
            print('Correcto llamado de evaluar!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")

    def test_agregarAlumno(self):
        print("Comenzando pruebas de: test_agregarAlumno")
        c = Client()
        response = c.post('/gestionarEvaluacion/agregarAlumno/', {'nombreAlumno': 'Juan Casas', 'codigoAlumno': '20162581','horario': 'H102'})
        if response.status_code == 200:
            print('Correcto llamado de agregarAlumno!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")

    def test_listarAlumno(self):
        print("Comenzando pruebas de: test_listarAlumno")
        c = Client()
        response = c.post('/gestionarEvaluacion/listarAlumno/', {'filtrado': '', 'horarioSeleccionado': 'H102'})
        if response.status_code == 200:
            print('Correcto llamado de listarAlumno!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")


    def test_editarAlumno(self):
        print("Comenzando pruebas de: editarAlumno")
        c = Client()
        response = c.post('/gestionarEvaluacion/editarAlumno/', {'idAlumno': '1' ,'codigoAlumno': '20142081','nombreAlumno':'Carlos Calderon'})
        if response.status_code == 200:
            print('Correcto llamado de editarAlumno!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")


    def test_eliminarAlumno(self):
        print("Comenzando pruebas de: eliminarAlumno")
        c = Client()
        response = c.post('/gestionarEvaluacion/eliminarAlumno/', {'idAlumno': '1'})
        if response.status_code == 200:
            print('Correcto llamado de eliminarAlumno!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")


    def test_guardarPuntuacion(self):
        print("Comenzando pruebas de: test_guardarPuntuacion")
        c = Client()
        response = c.post('/gestionarEvaluacion/guardarPuntuacion/', {'idAlumno': '1','indicadorSeleccionado': '1', 'nivelSeleccionado': '1'})
        if response.status_code == 200:
            print('Correcto llamado de guardarPuntuacion!')
        elif response.status_code == 404:
            self.assertFalse(False)
        print("==================================================")

    def test_muestraRubrica(self):
        print("Comenzando pruebas de: test_muestraRubrica")
        c = Client()
        response = c.post('/gestionarEvaluacion/muestraRubrica/',{'indicadorSeleccionado': '1'})
        if response.status_code == 200:
            print('Correcto llamado de muestraRubrica!')
        elif response.status_code == 404:
            self.assertFalse(False)

        print("=================================================")


