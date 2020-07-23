from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100,null=True)
    pub_date = models.DateField(null=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price_per_unit = models.FloatField()


class Order(models.Model):
    order_no = models.UUIDField()
    total_price = models.FloatField()
    products = models.ManyToManyField(Product, through='OrderProducts')


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE,
                              related_name='order_products')
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='order_products')
    quantity = models.IntegerField(default=1)