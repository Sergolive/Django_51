from django.db import models

#Создаем таблицу для категорий
class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class ProductsModel(models.Model):
    title = models.CharField(max_length=100, help_text='Напишите название продукта!')
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='product_images')
    descriptions = models.TextField()
    count = models.IntegerField(default=0)
    link = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class CartModel(models.Model):
    product = models.CharField(max_length=100)
    total_price = models.FloatField()
    total_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)