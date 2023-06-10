from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.db.models import Max,Min,Count,Avg
import detectlanguage
def username_check(User):
    return User.username.endswith('vanduc')
@login_required(login_url='signin')
def index(request):   
    sach1 = books.objects.all()
    sach =[]
    for item in sach1:
        sach.append(item)
    sach.reverse()
    return render(request, 'myapp.html', {'sach':sach})
@login_required(login_url='signin')
def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched', False)
        tim = books.objects.filter(bookName__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'tim':tim})
    else:
        return render(request, 'search.html', {})
def signup(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Chào {username}, tài khoản của bạn đã tạo thành công! Mời đăng nhập.')
            return redirect('signin')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form':form})
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'không tồn tại')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'signin.html', {})
@login_required(login_url='signin')
def profile(request):
    order = Order.objects.filter(user=request.user, paid=False)
    return render(request, 'profile.html', {"order":order})
@user_passes_test(username_check, login_url='index')
def viewandadd(request):
    addbook = MyBooks()
    if request.method == 'POST' and 'addbook':
        addbook = MyBooks(request.POST, request.FILES)
        if addbook.is_valid():
            data = addbook.save(commit=False)
            data.bookName = request.POST["bookName"]
            data.authorName = request.POST["authorName"]
            data.decriptions = request.POST["decriptions"]
            data.pages = request.POST["pages"]
            data.releaseDate = request.POST["releaseDate"]
            data.category = request.POST["category"]
            data.price = request.POST["price"]
            data.avatar = request.FILES["oke"]
            data.save()
            messages.success(request, f'Thêm cuốn sách vào kệ thành công!')
            return redirect('index')
    else:
        addbook = MyBooks()
    return render(request, 'viewandadd.html', {'addbook':addbook})
@login_required(login_url='signin')
def edit_book(request, pk):
    change = books.objects.get(id=pk)
    sach1 = books.objects.filter(id=change.id)
    addbook = MyBooks(instance=change)
    formcartitem = CartItemForm(request.POST or None)
    #cập nhật sách
    if request.user.username.endswith('vanduc'):
        if request.method == 'POST' and 'update' in request.POST:
            addbook = MyBooks(request.POST or None, request.FILES, instance=change)
            if addbook.is_valid():
                addbook.save()
                messages.success(request, f'Thay đổi thông tin cuốn sách thành công!')
                return redirect('index')
    #tạo review
    form = ReviewForm(request.POST or None)
    comment = ProductReview.objects.filter(book=change)
    count = 0
    abc = []
    for p in comment:
        abc.append(p.user)
    for cmt in abc:
        if cmt == request.user:
            count += 1
    if request.method == "POST" and 'postReview' in request.POST:
        if count == 0:
            
            if form.is_valid():
                data = form.save(commit=False)
                data.review_text = request.POST["review_text"]
                data.review_rating = request.POST["review_rating"]
                data.user = request.user
                data.book = change
                data.save()
                messages.success(request, f'Gửi đánh giá thành công!')
                return redirect("edit_book",pk)
    else:
        form = ReviewForm()
    
    #thêm hàng vào giỏ
    if request.method == 'POST' and 'addtocart' in request.POST:
        user= request.user
        cart, _ = Cart.objects.get_or_create(user=user, complete=False)
        cart_item = CartItem.objects.filter(cart=cart, book=change)
        x = cart_item.values('quantity')
        #thêm mới
        if not cart_item.exists():
            if formcartitem.is_valid():
                data = formcartitem.save(commit=False)
                data.quantity = request.POST["quantity"]
                data.book = change
                data.cart = cart
                data.save()
                messages.success(request, f'Thêm hàng thành công!')
                return redirect('cart')
        #cập nhật số lượng sách
        else:
            y = int(x[0]['quantity'])
            if formcartitem.is_valid():
                for item in cart_item:
                    item.quantity = int(request.POST["quantity"]) + y
                    item.save()
                messages.success(request, f'Cập nhật thành công!')
            return redirect('cart')
    else:
        formcartitem = CartItemForm()
    context = {
        'addbook':addbook, 
        'sach1':sach1, 
        'form':form,
        'change':change,
        'formcartitem':formcartitem
        }
    return render(request, 'edit_book.html', context)
@user_passes_test(username_check, login_url='index')
def delete_book(request, pk):
    change = books.objects.get(id=pk)
    if request.method == 'POST':
        change.delete()
        return redirect('index')
    return render(request, 'delete_book.html', {'delete':change})
@login_required(login_url='signin')
def deletereview(request,book_id,review_id):
    change = books.objects.get(id=book_id)
    review = ProductReview.objects.get(book=change, id=review_id)
    if request.user == review.user:
        review.delete()
    return redirect("edit_book",book_id)
@login_required(login_url='signin')
def cart(request):
    user= request.user
    cart = Cart.objects.get(user=user, complete=False)
    cart2 = Cart.objects.filter(user=user, complete=False)
    cart_item = CartItem.objects.filter(cart=cart)
    paid_amount = 0
    for item in cart_item:
        paid_amount = item.cart_item_total() + paid_amount
    context = {
        "cart_item":cart_item,
        'cart2':cart2,
        "paid_amount":paid_amount,
    }
    return render(request, 'cart.html', context)
@login_required(login_url='signin')
def deleteitem(request, cart_item_id):
    cart = Cart.objects.get(user=request.user, complete=False)
    cart_item2 = CartItem.objects.get(id=cart_item_id, cart=cart)
    cart_item2.delete()
    return redirect('cart')
@login_required(login_url='signin')
def check_out(request):
    cart = Cart.objects.get(user=request.user, complete=False)
    cart_items = CartItem.objects.filter(cart=cart)
    paid_amount = 0
    for item in cart_items:
        paid_amount = item.cart_item_total() + paid_amount
    form = OrderForm(request.POST or None)
    if request.method == 'POST' and 'address' in request.POST:
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.fist_name = request.POST["first_name"]
            data.last_name = request.POST['last_name']
            data.email = request.POST['email']
            data.phone_number = request.POST['phone_number']
            data.address = request.POST['address']
            data.cart = cart
            data.paid = False
            data.paid_amount = paid_amount
            data.save()
            for i in CartItem.objects.filter(cart=cart):
                data.cart_items.add(i)
            return redirect("profile")
    context = {
        "form": form, 
        "cart_item":cart_items,
        "paid_amount":paid_amount,
    }
    return render(request, 'check_out.html', context)
@login_required(login_url='signin')
def deleteorder(request, order_id):
    order = Order.objects.get(user=request.user, id=order_id)
    order.delete()
    return redirect('profile')
def danhanhang(request, order_id):
    order = Order.objects.get(user=request.user, id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST or None, instance=order)
        if form.is_valid():
            data = form.save(commit=False)
            data.paid = True
            data.save()
            return redirect('history_order')
    return render(request, 'danhanhang.html', {'order':order,'form':form})
def history_order(request):
    order = Order.objects.filter(user=request.user, paid=True)
    return render(request, 'history_order.html', {'order':order})