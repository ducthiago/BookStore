from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.db.models import Max,Min,Count,Avg
# Create your models here.

class books(models.Model):
    authorName = models.CharField('Tên tác giả', max_length=200)
    bookName = models.CharField('Tên cuốn sách', max_length=50, default=None)
    decriptions = models.TextField('Mô tả', null=True, blank=True)
    pages = models.IntegerField('Số trang', validators=[MaxValueValidator(99999), MinValueValidator(1)],  default=100, null=True, blank=True)
    releaseDate = models.DateField('Ngày phát hành', default=date.today)
    CATES_CHOICES = [
        ('Lãng mạn', 'Lãng mạn'),
        ('Trinh thám', 'Trinh thám'),
        ('Khoa học', 'Khoa học'),
        ('Nghệ Thuật', 'Nghệ Thuật'),
        ('Thể Thao', 'Thể Thao'),
    ]
    category = models.CharField('Thể loại', max_length=12, default=None, choices=CATES_CHOICES)
    avatar = models.ImageField('Ảnh', upload_to='images/', blank=True, null=True)
    price = models.IntegerField('Giá (USD)', null= False, blank=False, default=100)
    def __str__(self):
        return self.bookName
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
class CartItem(models.Model):
    book = models.ForeignKey(books, verbose_name='Cuốn sách', on_delete=models.CASCADE)
    quantity = models.IntegerField('Số lượng', null=False, blank=False, default=1, validators=[MinValueValidator(1)])
    cart = models.ForeignKey(Cart, verbose_name='Giỏ hàng',on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def total_item_price(self):
        total = self.quantity * self.book.price
        return total
    def bookName(self):
        return self.book.bookName
    def authorName(self):
        return self.book.authorName
    def avatar(self):
        return self.book.avatar
    def cart_item_total(self):
        total = self.quantity * self.book.price
        return total
    def cartid(self):
        return self.cart.id
class Order(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    cart_items = models.ManyToManyField(CartItem)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField('Tên', max_length=255)
    last_name = models.CharField('Họ', max_length=255)
    phone_number = models.CharField('Số Điện Thoại',max_length=255)
    address = models.CharField('Địa Chỉ',max_length=255)
    email = models.EmailField('Email', max_length=255)
    paid_amount = models.IntegerField(blank=True, null=True)
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(books,related_name="comments", on_delete=models.CASCADE)
    review_text=models.TextField("Đánh giá")
    RATING=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    )
    review_rating=models.CharField("Số sao",choices=RATING,max_length=10, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_review_rating(self):
        return sum(self.review_rating)/Count(self.review_rating)