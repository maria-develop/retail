from django.db import models


class Retail(models.Model):
    FACTORY = 'factory'
    RETAIL = 'retail'
    ENTREPRENEUR = 'entrepreneur'
    TYPE_CHOICES = [
        (FACTORY, 'Factory'),
        (RETAIL, 'Retail Network'),
        (ENTREPRENEUR, 'Individual Entrepreneur'),
    ]

    username = None
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип поставщика")
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наименование")
    email = models.EmailField(unique=True, verbose_name="Почта")
    country = models.CharField(max_length=255, verbose_name="Страна")
    city = models.CharField(max_length=255, verbose_name="Город", null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name="Улица", null=True, blank=True)
    house_number = models.CharField(max_length=10, verbose_name="Номер дома", null=True, blank=True)
    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='customers',
        verbose_name="Поставщик"
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Задолженность перед поставщиком"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} ({self.email})"

    def get_level(self):
        level = 0
        current = self.supplier
        while current:
            level += 1
            current = current.supplier
        return level

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Product(models.Model):
    supplier = models.ForeignKey(Retail, related_name='products', on_delete=models.CASCADE, verbose_name="Поставщик")
    name = models.CharField(max_length=255, verbose_name="Название продукта")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
