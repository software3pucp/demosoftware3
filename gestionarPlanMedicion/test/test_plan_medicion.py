from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64               # for decoding base64 image
from django.test import TestCase, override_settings

from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarPlanMedicion.models import PlanMedicion
from gestionarResultados.models import ResultadoPUCP


class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo PLAN DE MEDICION")
        print("=====================================")
        PlanMedicion.objects.create(estado=1, curso_id=1)
        Curso.objects.create(nombre='CGI', responsable=1, especialidad_id=1)
        Curso.objects.create(nombre='Estadistica', responsable=1, especialidad_id=1)
        Especialidad.objects.create(nombre='Ingenieria Industrial')
        Indicador.objects.create(codigo='ID001', descripcion='Indicador01', estado=1, resultado_id=1)
        ResultadoPUCP.objects.create(codigo='RE01', estado='2', descripcion='Resultado01')
        Horario.objects.create(codigo='H0811',responsable=1,curso_id=1)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_listar_plan_medicion(self):
        print("Comenzando pruebas de: test_listar_plan-medicion")

        c = Client()
        response = c.get('/gestionarPlanMedicion/listar/')
        if response.status_code == 200:
            print('Correcta inicialización de Listar - Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'listEspec', 'facultad': '1'})
        if response.status_code == 200:
            print('Correcto Listar Especialidades Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'listCur', 'especialidad': '1', 'estado': '1'})
        if response.status_code == 200:
            print('Correcto Listar Cursos Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'estado', 'planpk': '1'})
        if response.status_code == 200:
            print('Correcto Cambiar Estado Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'eliminar', 'planPk': '1'})
        if response.status_code == 200:
            print('Correcto Eliminar Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_crear_plan_medicion(self):
        print("Comenzando pruebas de: test_crear_plan-medicion")

        pk = '1'
        c = Client()
        response = c.get('/gestionarPlanMedicion/crear/'+pk)
        if response.status_code == 200:
            print('Correcta inicialización de Crear Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/'+pk, {'operacion': 'editar','especialidad':'1'})
        if response.status_code == 200:
            print('Correcto Editar Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de insertar un curso que ya existe en el plan de medicion
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'insertar', 'especialidad': '1', 'curso': '1'})
        if response.status_code == 200:
            print('Correcto Error Insertar Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Ingresar curso 2 que no existe en el plan de medicion
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'insertar', 'especialidad': '1', 'curso': '2', 'estado': '1'})
        if response.status_code == 200:
            print('Correcto Insertar Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'listHorarios', 'especialidad': '1', 'curso': '1'})
        if response.status_code == 200:
            print('Correcto Listar Horarios Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'mostrarHorario', 'especialidad': '1', 'horarioPk': '1'})
        if response.status_code == 200:
            print('Correcto Mostrar Horarios Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'mostrarIndicador', 'especialidad': '1', 'indicadorPk': '1'})
        if response.status_code == 200:
            print('Correcto Mostrar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Agregar un indicador 1 que no existe en la lista de indicadores del curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'agregarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Agregar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de agregar un indicador 1 que ya existe en la lista de indicadores del curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'agregarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Agregar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Quitar el indicador 1 que si existe
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'quitarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Quitar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Quitar el indicador 1 que ya no existe en los indicadores del curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'quitarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Quitar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Añadir horario 1 al curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'agregarHorario', 'especialidad': '1', 'horarioPk': '1', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Agregar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de añadir horario 1 que ya existe al curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'agregarHorario', 'especialidad': '1', 'horarioPk': '1', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Agregar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Quitar horario 1 que existe en el curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'quitarHorario', 'especialidad': '1', 'horarioPk': '1', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Quitar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de quitar horario 1 que ya no existe en el curso
        c = Client()
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'quitarHorario', 'especialidad': '1', 'horarioPk': '1', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Quitar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)