from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Adress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name_user = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    commune = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_user


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ManyToManyField(Category, related_name='product_category')
    price = models.IntegerField(default=0)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    describe = models.CharField(max_length=300, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    count39 = models.IntegerField(default=0)
    count40 = models.IntegerField(default=0)
    count41 = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)
    # count = models.IntegerField(default=0)

    @property

    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def ImageURL1(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    
    def ImageURL2(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url
    
    def ImageURL3(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url
    
    def ImageURL4(self):
        try:
            url = self.image4.url
        except:
            url = ''
        return url
    
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    size = models.IntegerField(default=0,null=True, blank=True)
    total = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Adress, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        # lấy hết tất cả tiền của các mặt hàng
        total = sum([item.get_total for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    size = models.IntegerField(default=0,null=True, blank=True)
    total = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    # lấy tiền của mỗi sản phẩm
    @property
    def get_total(self):
        return self.total

class Payment_VNPay(models.Model):
    order_id = models.IntegerField(default=0, null=True, blank=True)
    amount = models.FloatField(default=0.0, null=True, blank=True)
    order_desc = models.CharField(max_length=200,null=True, blank=True)
    vnp_TransactionNo = models.CharField(max_length=200,null=True, blank=True)
    vnp_ResponseCode = models.CharField(max_length=200,null=True, blank=True)

class AddProduct(forms.ModelForm):
    # count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'price_sale', 'describe', 'digital', 'image', 'image1', 
                  'image2', 'image3', 'image4', 'unit','count39','count40','count41']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'describe': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 150px'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'price_sale': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input, d-flex'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'count39': forms.TextInput(attrs={'class': 'form-control'}),
            'count40': forms.TextInput(attrs={'class': 'form-control'}),
            'count41': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['sub_category', 'is_sub', 'name', 'slug', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['customer', 'name_user', 'adress', 'city', 'mobile', 'district', 'commune']
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'name_user': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'commune': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),

        }

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PaymentForm(forms.Form):

    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)
