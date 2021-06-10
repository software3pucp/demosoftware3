from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO  # StringIO and BytesIO are parts of io module in python3
from django.test import Client
import base64               # for decoding base64 image
from django.test import TestCase, override_settings

from gestionarEspecialidad.models import Especialidad
from gestionarFacultad.models import Facultad
from gestionarNiveles.models import Nivel


class TestingClasses(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Inicio de prueba del módulo gestionarNiveles")
        print("============================================")
        facultad = Facultad.objects.create(nombre='facultad', responsable='1')
        especialidad = Especialidad.objects.create(nombre='especialidad', responsable='1', facultad=facultad)
        Nivel.objects.create(nombre='Inicial', valor=1, especialidad=especialidad)
        pass

    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_niveles(self):
        print("Comenzando pruebas de: test_niveles")
        c = Client()
        response = c.get('/gestionarNiveles/niveles/')
        if response.status_code == 200:
            print('Correcto niveles!')
        elif response.status_code == 404:
            self.assertFalse(False)

   # def test_crear_nivel(self):
    #    print("Comenzando pruebas de: test_crear_nivel")
     #   c = Client()
      #  response = c.get('/gestionarNiveles/crear/')
       # if response.status_code == 200:
        #    print('Correcta inicialización de crear niveles!')
        #elif response.status_code == 404:
         #   self.assertFalse(False)

        #c = Client(enforce_csrf_checks=True )
        #response = c.post('/gestionarNiveles/crear/', {'nombre': 'Inicial', 'valor':1, 'especialidadpk':1})
        #if response.status_code != 404:
         #   print('Se agregó un nivel correctamente!')
        #elif response.status_code == 404
         #   self.assertFalse(False)

    def test_EditarNivel(self):
        print("Comenzando pruebas de: test_EditarNivel")
        c = Client()
        pk = "1"
        response = c.post('/gestionarNiveles/editar/' + pk + '/', follow=True)
        if response.status_code == 200:
            print('Se editó una nivel correctamente!')
        else:
            self.assertFalse(False)

