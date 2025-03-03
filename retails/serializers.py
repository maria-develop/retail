from rest_framework.serializers import ModelSerializer, CharField
from .validators import TitleValidator
from .models import Retail, Product


class RetailSerializer(ModelSerializer):
    name = CharField(
        validators=[TitleValidator(field="name")],  # Используем поле name вместо title
    )

    class Meta:
        model = Retail
        fields = '__all__'
        read_only_fields = ('debt',)  # Запрещаем обновление задолженности через API


class ProductSerializer(ModelSerializer):
    name = CharField(
        validators=[TitleValidator(field="name")],  # Используем поле name вместо title
    )

    class Meta:
        model = Product
        fields = '__all__'
