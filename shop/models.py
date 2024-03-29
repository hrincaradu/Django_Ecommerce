import uuid
from django.urls import reverse
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from accounts.models import CustomUser
class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'category', blank=True)

# Create your models here.
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.id])
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank = True, null= True)
    updated = models.DateTimeField(auto_now=True, blank = True, null= True)
    image_thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(200,200)],
        format="JPEG",
        options={'quality':80} )

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.category.id, self.id])
    
    def __str__(self):
        return str(self.name)

    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return 'static/images/No-Image.jpg'

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Slider(models.Model):
    image = models.ImageField(upload_to="slide")
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="reviews", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank = True)
    content = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


