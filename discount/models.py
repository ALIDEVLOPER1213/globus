from django.db import models


class Title (models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    title = models.ForeignKey(Title, max_length=100,  null=True, blank=True, on_delete=models.CASCADE)
    img = models.ImageField()
    description = models.TextField()
    start_data = models.DateTimeField()
    ending_data = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def calculate_discount(self, discount_percentage):
        discount_amount = (self.price * discount_percentage) / 100
        discounted_price = self.price - discount_amount
        return discounted_price

    def __str__(self):
        return self.title