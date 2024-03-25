from django.db import models
from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Seller(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=500)

    def __str__(self):
        return self.name, self.contact


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.percent, self.date_end, self.date_start


class Promocode(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    is_cumulative = models.BooleanField()

    def __str__(self):
        return self.name, self.percent


class Product(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=100)
    description = models.TextField()
    count_on_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, null=True, blank = True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name, self.article, self.price, self.discount, self.seller


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.image

class Cart():
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class Order(models.Model):
    STATUSES = (

        ('In Process', 'In Process'),
        ('Complited on Stock', 'Complited on Stock'),
        ('Deliveried', 'Deliveried'),
        ('On the way', 'On the way')

    )
    DELIVERY_METHODS = (

        ('Courier', 'Courier'),
        ('Post', 'Post'),
        ('Self-delivery', 'Self-delivery')
    )
    PAYMENT_METHODS = (
        ('Card Online', 'Card Online'),
        ('Card Offline', 'Card Offline'),
        ('Cash', 'Cash')
    )
    PAYMENT_STATUS = (
        ('Paid', 'Paid'),
        ('In process', 'In process'),
        ('Cancelled', 'Cancelled')
    )
    NOTIF_TIMES = (
        (24, 24),
        (6, 6),
        (1, 1)
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=STATUSES, max_length=100)

    delivery_adress = models.CharField(max_length=100, null=True, blank = True)
    delivery_method = models.CharField(choices=DELIVERY_METHODS, max_length=100)
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=100)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=100, default='In process')
    delivery_notification_before = models.PositiveSmallIntegerField(choices=NOTIF_TIMES, default=6)


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class Cashback(models.Model):
    percent = models.PositiveIntegerField()
    treshold = models.PositiveIntegerField()

