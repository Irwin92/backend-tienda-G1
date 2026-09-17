from django.test import TestCase
from .serializers import ProductoSerializer

class ProductoSerializerTests(TestCase):
    def test_precio_debe_ser_mayor_que_cero(self):
        datos={
            "nombre":"Mouse",
            "descripcion":"Mouse USB",
            "precio":0,
            "stock":5,
            "activo":True,
        }
        serializer = ProductoSerializer(data = datos)

        self.assertFalse(serializer.is_valid())
        self.assertIn("precio",serializer.errors)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from django.contrib.auth import get_user_model
from django.urls import reverse 
from rest_framework import status
from rest_framework.test import APITestCase

class PerfilAPITests(APITestCase):
    def setUp(self):
        Usuario = get_user_model()
        self.usuario = Usuario.objects.create_user(
            username="ana",
            password="ClaveSegura123!"
        )
        self.url = reverse("api_perfil")

    def test_rechaza_sin_autentication(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_acepta_usuario_autenticadon(self):
            #Permite asociar directamente un usuario al cliente de pruebas
            self.client.force_authenticate(user=self.usuario)
            response = self.client.get(self.url)
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK
            )
    