from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    banner = models.BooleanField(default=False, null=True, blank=True)
    sign = models.BooleanField(default=False, null=True, blank=True)
    badge = models.BooleanField(default=False, null=True, blank=True)
    busincard = models.BooleanField(default=False, null=True, blank=True)
    pillow = models.BooleanField(default=False, null=True, blank=True)
    towel = models.BooleanField(default=False, null=True, blank=True)
    keyring = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, through='Likes', related_name='liked_products')

    def __str__(self):
        return self.name

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designproduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_likes')
    liked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} likes {self.designproduct.name}"

class UserComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designproduct = models.ForeignKey('Product', on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s comment on {self.designproduct.name}"

    class Meta:
            verbose_name = "User Comment"  # Customize the singular name
            verbose_name_plural = "User Comments"  # Customize the plural name
