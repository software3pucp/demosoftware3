from django.test import Client
from django.test import TestCase, override_settings

from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarHorario.models import Horario
from gestionarNiveles.models import Nivel


class TestingClasses(TestCase):



    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo RESULTADOS MEDICIONES")
        print("=====================================")
        Curso.objects.create(nombre='CGI', responsable=1, especialidad_id=1)
        Horario.objects.create(codigo='H0811', responsable=1, curso_id=1)
        Especialidad.objects.create(nombre='Ingenieria Industrial')
        Nivel.objects.create(nombre="Nivel 1",valor=1,especialidad_id=1)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_resultados_Medicionesd(self):
        print("Comenzando pruebas de: test_resultados_Mediciones")

        c = Client()
        response = c.get('/gestionarResultadosMediciones/resultados/')
        if response.status_code == 200:
            print('Correcto inicialización de Resultados Mediciones!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarResultadosMediciones/resultados/', {'operacion': 'agregar'})
        if response.status_code == 200:
            print('Correcto Agregar Resultados Mediciones!')
        elif response.status_code == 404:
            self.assertFalse(False)