import re
from rest_framework.serializers import ValidationError


class TitleValidator:
    """
    Валидатор для проверки поля name.
    Поле должно содержать только буквы, цифры, точки, дефисы, запятые и пробелы.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r"^[а-яА-Яa-zA-Z0-9\.\-\,\№\s]+$")
        if not reg.match(value):
            raise ValidationError(
                f"{self.field} может содержать только буквы, цифры, точки, дефисы, запятые и пробелы."
            )
