from django.contrib import admin
from .models import *

admin.site.register(books)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ProductReview)
admin.site.register(Order)

# Register your models here.