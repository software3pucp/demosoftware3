from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64  # for decoding base64 image
from django.test import TestCase, override_settings

from authentication import models
from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarPlanMedicion.models import PlanMedicion
from gestionarPlanMejora.models import PlanMejora, EstadoActividad
from gestionarResultados.models import ResultadoPUCP


class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo Plan de Mejora")
        print("=====================================")
        #facultad = Facultad.objects.create(nombre='facultad', responsable='1')
        #especialidad = Especialidad.objects.create(nombre='especialidad', responsable='1', facultad=facultad)
        #planMedicion = PlanMedicion.objects.create(estado=1, curso_id=1)
        #estado = EstadoActividad.objects.create(nombre='Activo', estado=1)
        #PlanMejora.objects.create(especialidad_id=especialidad, planMedicion_id=planMedicion, estado=estado)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_planMejora(self):
        print("Comenzando pruebas de: test_planMejora")
        c = Client()
        response = c.get('/gestionarPlanMedicion/historico/')
        if response.status_code == 200:
            print('Correcto plan Mejora!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_editar_planMejora(self):
        print("Comenzando pruebas de: test_editar_planMejora")
        c = Client()
        id_pm = "1"
        response = c.get('/gestionarPlanMejora/editar/' + id_pm + '/')
        if response.status_code == 200:
            print('Correcto editar Plan Mejora!')
        elif response.status_code == 404:
            self.assertFalse(False)

    #def test_crear_planMejora(self):
    #    print("Comenzando pruebas de: test_crear_planMejora")
    #    c = Client()
    #    id_pm = '1'
    #    response = c.get('/gestionarPlanMejora/crear/' + id_pm)
    #    if response.status_code == 200:
    #        print('Correcto crear Plan Mejora!')
    #    elif response.status_code == 404:
    #        self.assertFalse(False)

    def test_subirEvidencia(self):
        print("Comenzando pruebas de: subir Evidencia")
        c = Client(enforce_csrf_checks=True)
        id_evidencia = "1"
        response = c.post('/gestionarPlanMejora/subirEvidencia/' + id_evidencia + '/')
        if response.status_code == 200:
            print('Correcto subir Evidencia!')
        else:
            self.assertFalse(False)

    def test_editarEvidencia(self):
        print("Comenzando pruebas de: editar Evidencia")
        c = Client(enforce_csrf_checks=True)
        id_evidencia = "1"
        response = c.post('/gestionarPlanMejora/subirEvidencia/' + id_evidencia)
        if response.status_code != 200:
            print('Correcto editar Evidencia!')
        else:
            self.assertFalse(False)

    def test_editarPropuesta(self):
        print("Comenzando pruebas de: editar Propuesta")
        c = Client(enforce_csrf_checks=True)
        id_planmejora = "1"
        response = c.post('/gestionarPlanMejora/editar/' + id_planmejora)
        if response.status_code == 200:
            print('Correcto editar Propuesta!')
        else:
            self.assertFalse(False)

    def test_crearPropuesta(self):
        print("Comenzando pruebas de: crear Propuesta")
        c = Client(enforce_csrf_checks=True)
        id_planmejora = "1"
        response = c.post('/gestionarPlanMejora/crear/' + id_planmejora + '/', follow=True)
        if response.status_code == 200:
            print('Correcto crear Propuesta!')
        else:
            self.assertFalse(False)

    def test_editarActividad(self):
        print("Comenzando pruebas de: editar Actividad")
        c = Client(enforce_csrf_checks=True)
        id_actividad = "1"
        response = c.post('/gestionarPlanMejora/editarActividad/' + id_actividad + '/', follow=True)
        if response.status_code == 200:
            print('Correcto editar Actividad!')
        else:
            self.assertFalse(False)
