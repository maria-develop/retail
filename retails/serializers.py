from rest_framework.serializers import ModelSerializer, CharField
from .validators import TitleValidator
from .models import Retail, Product


class RetailSerializer(ModelSerializer):
    """
    Сериализатор для модели Retail.
    Используется для преобразования объектов Retail в JSON и обратно.
    """
    name = CharField(
        validators=[TitleValidator(field="name")],
    )

    class Meta:
        model = Retail
        fields = '__all__'
        read_only_fields = ('debt',)  # Запрещаем обновление задолженности через API


class ProductSerializer(ModelSerializer):
    """
    Сериализатор для модели Product.
    Используется для преобразования объектов Product в JSON и обратно.
    """
    name = CharField(
        validators=[TitleValidator(field="name")],
    )

    class Meta:
        model = Product
        fields = '__all__'
