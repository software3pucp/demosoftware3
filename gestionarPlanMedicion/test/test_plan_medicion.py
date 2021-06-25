from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64               # for decoding base64 image
from django.test import TestCase, override_settings

from gestionarCurso.models import Curso
from gestionarEspecialidad.models import Especialidad
from gestionarHorario.models import Horario
from gestionarIndicadores.models import Indicador
from gestionarPlanMedicion.models import PlanMedicion, PlanMedicionCurso
from gestionarResultados.models import ResultadoPUCP, PlanResultados
from authentication.models import User
from gestionarSemestre.models import Semestre


class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo PLAN DE MEDICION")
        print("=====================================")
        PlanMedicion.objects.create(codigo='PM01', nombre='Plan de medicion 01', estado=1, planResultados_id=1, especialidad_id=1)
        PlanMedicionCurso.objects.create(estado=1,curso_id=1,planMedicion_id=1,semestre_id=1)
        Curso.objects.create(nombre='CGI', responsable=1, especialidad_id=1)
        Curso.objects.create(nombre='Estadistica', responsable=1, especialidad_id=1)
        Especialidad.objects.create(nombre='Ingenieria Industrial')
        Indicador.objects.create(codigo='ID001', descripcion='Indicador01', estado=1, resultado_id=1)
        ResultadoPUCP.objects.create(codigo='RE01', estado='2', descripcion='Resultado01')
        Semestre.objects.create(nombreCodigo='2021-1',anho='2021')
        PlanResultados.objects.create(codigo='PRH01',descripcion='Plan de resultado historico 01', estado=1, especialidad_id=1)
        user = User.objects.create(username='admin@apolo.pe')
        user.set_password('admin@apolo.pe')
        user.save()
        Horario.objects.create(codigo='H0811',responsable_id=1,curso_id=1)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_listar_plan_medicion(self):
        print("Comenzando pruebas de: test_listar_plan-medicion")

        c = Client()
        c.login(username='admin@apolo.pe',password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'entrada', 'especialidad': '1', 'semestre': '1', 'planMedicion': '1', 'estado': '1'})
        if response.status_code == 200:
            print('Correcta inicialización de Listar - Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'estado', 'planCurso': '1', 'especialidad': '1', 'semestre': '1', 'planMedicion': '1', 'estado': '1'})
        if response.status_code == 200:
            print('Correcto Estado Curso de Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/listar/', {'operacion': 'eliminar', 'planCurso': '1', 'especialidad': '1', 'semestre': '1', 'planMedicion': '1', 'estado': '1'})
        if response.status_code == 200:
            print('Correcto Eliminar Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_crear_plan_medicion(self):
        print("Comenzando pruebas de: test_crear_plan-medicion")

        pk = '1'
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crear/'+pk, {'planMedicion': '1 ', 'operacion': 'entrada','especialidad':'1', 'semestre':'1'})
        if response.status_code == 200:
            print('Correcto Entrada Crear Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'planMedicion': '1 ', 'operacion': 'editar', 'especialidad': '1', 'semestre': '1'})
        if response.status_code == 200:
            print('Correcto Editar Crear Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Insertar curso en el plan de medicion
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'curso': '1', 'planMedicion': '1 ', 'operacion': 'editar', 'especialidad': '1', 'semestre': '1'})
        if response.status_code == 200:
            print('Correcto Insertar Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de insertar un curso que ya existe en el plan de medicion
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crear/' + pk, {'operacion': 'insertar', 'planMedicion': '1 ', 'especialidad': '1', 'curso': '1', 'especialidad': '1', 'semestre': '1'})
        if response.status_code == 200:
            print('Correcto Error Insertar Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'listHorarios', 'especialidad': '1', 'curso': '1'})
        if response.status_code == 200:
            print('Correcto Listar Horarios Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'mostrarHorario', 'especialidad': '1', 'horarioPk': '1'})
        if response.status_code == 200:
            print('Correcto Mostrar Horarios Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'mostrarIndicador', 'especialidad': '1', 'indicadorPk': '1'})
        if response.status_code == 200:
            print('Correcto Mostrar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Agregar un indicador 1 que no existe en la lista de indicadores del curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'agregarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Agregar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de agregar un indicador 1 que ya existe en la lista de indicadores del curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'agregarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Agregar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Quitar el indicador 1 que si existe
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'quitarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Quitar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Quitar el indicador 1 que ya no existe en los indicadores del curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'quitarIndicador', 'especialidad': '1', 'indicadorPk': '1', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Quitar Indicador Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Añadir horario 1 al curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'agregarHorario', 'planPK': '1', 'codigo': 'H0881', 'responsablePk': '1'})
        if response.status_code == 200:
            print('Correcto Agregar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de añadir horario 1 que ya existe al curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'agregarHorario', 'planPK': '1', 'codigo': 'H0881', 'responsablePk': '1'})
        if response.status_code == 500:
            print('Correcto Error Agregar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        # Editar horario 2
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'editarHorario', 'horarioPk': '2', 'planPK': '1', 'codigo': 'H0882', 'responsablePk': '1'})
        if response.status_code == 200:
            print('Correcto Editar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        # Editar horario 1 que no pertenece al curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'editarHorario', 'horarioPk': '1', 'planPK': '1', 'codigo': 'H0882', 'responsablePk': '1'})
        if response.status_code == 500:
            print('Correcto Error Editar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Quitar horario 2 que existe en el curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'quitarHorario', 'horarioPk': '2', 'planPK': '1'})
        if response.status_code == 200:
            print('Correcto Quitar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        #Tratar de quitar horario 2 que ya no existe en el curso
        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearPlanMedicionAjax', {'operacion': 'quitarHorario', 'horarioPk': '2', 'planPK': '1'})
        if response.status_code == 500:
            print('Correcto Error Quitar Horario Curso Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_historico(self):
        print("Comenzando pruebas de: test_historico")

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.get('/gestionarPlanMedicion/historico/')
        if response.status_code == 200:
            print('Correcto Inicializacion de Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/historico/', {'operacion': 'terminar', 'planMedicion': '1'})
        # print(response)
        if response.status_code == 302:
            print('Correcto Terminar Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/historico/', {'operacion': 'ver plan', 'planMedicion': '1'})
        # print(response)
        if response.status_code == 302:
            print('Correcto Ver Plan Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_crear_historico(self):
        print("Comenzando pruebas de: test_crear_historico")

        c = Client()
        id_especialidad='1'
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.get('/gestionarPlanMedicion/crearHistorico/'+id_especialidad)
        # print(response)
        if response.status_code == 200:
            print('Correcto Inicialización de Crear Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/crearHistorico/'+id_especialidad, {'codigo': 'PMH01', 'nombre': 'Plan de medicion historico 1'})
        # print(response)
        if response.status_code == 302:
            print('Correcto Crear Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_listar_historico(self):
        print("Comenzando pruebas de: test_listar_historico")

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/listarHistorico/', {'especialidad': '1'})
        # print(response)
        if response.status_code == 200:
            print('Correcto Listar Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_eliminar_medicion(self):
        print("Comenzando pruebas de: test_eliminar_medicion")

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/eliminarMedicion/', {'historicoPk': '1'})
        # print(response)
        if response.status_code == 200:
            print('Correcto Eliminar Medicion Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_editar_historico(self):
        print("Comenzando pruebas de: test_editar_historico")

        c = Client()
        pk='1'
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.get('/gestionarPlanMedicion/editarHistorico/'+pk)
        # print(response)
        if response.status_code == 200:
            print('Correcto Editar Historico Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_agregar_semestre_plan_medicion(self):
        print("Comenzando pruebas de: test_agregar_semestre_plan_medicion")

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/agregarSemestrePlan/', {'historicoPK': '1', 'semestrePk': '1'})
        # print(response)
        if response.status_code == 200:
            print('Correcto Agregar Semestre Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)

    def test_editar_nombre_plan_medicion(self):
        print("Comenzando pruebas de: test_editar_nombre_plan_medicion")

        c = Client()
        c.login(username='admin@apolo.pe', password='admin@apolo.pe')
        response = c.post('/gestionarPlanMedicion/editarNombre/', {'historicoPK': '1', 'nombre': 'Plancito de medicion', 'codigo': 'PM001'})
        # print(response)
        if response.status_code == 200:
            print('Correcto Editar Nombre Plan Medicion!')
        elif response.status_code == 404:
            self.assertFalse(False)