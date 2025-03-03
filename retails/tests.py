from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from retails.models import Retail, Product
from users.models import User
from retails.serializers import RetailSerializer, ProductSerializer


class RetailTestCase(APITestCase):

    def setUp(self):
        # Создаем пользователя для аутентификации
        self.user = User.objects.create(email="test@example.com", is_active=True)
        self.user.set_password("testpassword")
        self.user.save()

        # Создаем объекты Retail для тестов
        self.factory = Retail.objects.create(
            type=Retail.FACTORY,
            name="Factory 1",
            email="factory1@example.com",
            country="Country 1",
            city="City 1",
            street="Street 1",
            house_number="1",
        )
        self.retail = Retail.objects.create(
            type=Retail.RETAIL,
            name="Retail 1",
            email="retail1@example.com",
            country="Country 2",
            city="City 2",
            street="Street 2",
            house_number="2",
            supplier=self.factory,
        )
        self.product = Product.objects.create(
            name="Product 1",
            model="Model 1",
            release_date="2023-01-01",
            supplier=self.retail,
        )

        # Аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_retail_retrieve(self):
        """Тест получения деталей объекта Retail."""
        url = reverse("retails:retail_retrieve", args=(self.retail.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.retail.name)

    def test_retail_retrieve_unauthenticated(self):
        """Тест получения деталей объекта Retail без аутентификации."""
        self.client.logout()
        url = reverse("retails:retail_retrieve", args=(self.retail.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retail_create(self):
        """Тест создания объекта Retail."""
        url = reverse("retails:retail_create")
        data = {
            "type": Retail.RETAIL,
            "name": "Retail 2",
            "email": "retail2@example.com",
            "country": "Country 3",
            "city": "City 3",
            "street": "Street 3",
            "house_number": "3",
            "supplier": self.factory.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Retail.objects.all().count(), 3)

    def test_retail_create_invalid(self):
        """Тест создания объекта Retail с невалидными данными."""
        url = reverse("retails:retail_create")
        data = {
            "type": Retail.RETAIL,
            "name": "",  # Невалидное поле
            "email": "retail2@example.com",
            "country": "Country 3",
            "city": "City 3",
            "street": "Street 3",
            "house_number": "3",
            "supplier": self.factory.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

    def test_retail_update(self):
        """Тест обновления объекта Retail."""
        url = reverse("retails:retail_update", args=(self.retail.pk,))
        data = {"name": "Updated Retail"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Updated Retail")

    def test_retail_update_debt(self):
        """Тест запрета обновления поля debt через API."""
        url = reverse("retails:retail_update", args=(self.retail.pk,))
        data = {"debt": 1000.00}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.retail.refresh_from_db()
        self.assertEqual(self.retail.debt, 0)  # Поле debt не должно обновиться

    def test_retail_destroy(self):
        """Тест удаления объекта Retail."""
        url = reverse("retails:retail_delete", args=(self.retail.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Retail.objects.all().count(), 1)

    def test_retail_list(self):
        """Тест получения списка объектов Retail."""
        url = reverse("retails:retail_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data["results"]), 2)


class ProductTestCase(APITestCase):

    def setUp(self):
        # Создаем пользователя для аутентификации
        self.user = User.objects.create(email="test@example.com", is_active=True)
        self.user.set_password("testpassword")
        self.user.save()

        # Создаем объекты Retail и Product для тестов
        self.factory = Retail.objects.create(
            type=Retail.FACTORY,
            name="Factory 1",
            email="factory1@example.com",
            country="Country 1",
            city="City 1",
            street="Street 1",
            house_number="1",
        )
        self.product = Product.objects.create(
            name="Product 1",
            model="Model 1",
            release_date="2023-01-01",
            supplier=self.factory,
        )

        # Аутентифицируем пользователя
        self.client.force_authenticate(user=self.user)

    def test_product_retrieve(self):
        """Тест получения деталей объекта Product."""
        url = reverse("retails:product_retrieve", args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.product.name)

    def test_product_create(self):
        """Тест создания объекта Product."""
        url = reverse("retails:product_create")
        data = {
            "name": "Product 2",
            "model": "Model 2",
            "release_date": "2023-02-01",
            "supplier": self.factory.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_product_update(self):
        """Тест обновления объекта Product."""
        url = reverse("retails:product_update", args=(self.product.pk,))
        data = {"name": "Updated Product"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], "Updated Product")

    def test_product_destroy(self):
        """Тест удаления объекта Product."""
        url = reverse("retails:product_delete", args=(self.product.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)

class RetailSerializerTest(APITestCase):
    def setUp(self):
        self.factory = Retail.objects.create(
            type=Retail.FACTORY,
            name="Factory 1",
            email="factory1@example.com",
            country="Country 1",
            city="City 1",
            street="Street 1",
            house_number="1",
        )
        self.retail = Retail.objects.create(
            type=Retail.RETAIL,
            name="Retail 1",
            email="retail1@example.com",
            country="Country 2",
            city="City 2",
            street="Street 2",
            house_number="2",
            supplier=self.factory,
        )

    def test_retail_serializer(self):
        """Тест сериализатора RetailSerializer."""
        serializer = RetailSerializer(self.retail)
        data = serializer.data
        self.assertEqual(data["name"], "Retail 1")
        self.assertEqual(data["supplier"], self.factory.id)


class ProductSerializerTest(APITestCase):
    def setUp(self):
        self.factory = Retail.objects.create(
            type=Retail.FACTORY,
            name="Factory 1",
            email="factory1@example.com",
            country="Country 1",
            city="City 1",
            street="Street 1",
            house_number="1",
        )
        self.product = Product.objects.create(
            name="Product 1",
            model="Model 1",
            release_date="2023-01-01",
            supplier=self.factory,
        )

    def test_product_serializer(self):
        """Тест сериализатора ProductSerializer."""
        serializer = ProductSerializer(self.product)
        data = serializer.data
        self.assertEqual(data["name"], "Product 1")
        self.assertEqual(data["supplier"], self.factory.id)


from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase
from retails.validators import TitleValidator


class TitleValidatorTest(APITestCase):
    def test_title_validator_valid(self):
        """Тест валидатора с корректными данными."""
        validator = TitleValidator(field="name")
        value = "Valid Name 123"
        try:
            validator(value)
        except ValidationError:
            self.fail("TitleValidator raised ValidationError unexpectedly!")

    def test_title_validator_invalid(self):
        """Тест валидатора с некорректными данными."""
        validator = TitleValidator(field="name")
        value = "Invalid@Name"
        with self.assertRaises(ValidationError):
            validator(value)
