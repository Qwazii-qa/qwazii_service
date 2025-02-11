from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='상품명')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='카테고리')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='단가')
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='판매가격')
    manufacturer = models.CharField(max_length=200, verbose_name='제조사')
    stock_quantity = models.IntegerField(verbose_name='재고 수량')
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='수수료')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
