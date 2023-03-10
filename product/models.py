from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)  #slugfield - не по айди а по текстовому полю
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='categories', null=True, blank=True) #null = в базе данных может не сохранятся(пустое значение), blank = можем не указывать при заполнении

    def __str__(self) -> str:
        return f'{self.title}'


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ammount = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'{self.title}'