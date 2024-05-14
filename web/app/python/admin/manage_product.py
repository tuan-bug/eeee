from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *


def manageProduct(request):
    products = Product.objects.all()
    form = AddProduct()
    context = {'products': products}
    return render(request, 'admin/managementProduct.html', context)

# def addProduct(request):
#     form = AddProduct()
#     if request.method == 'POST':
#         form = AddProduct(request.POST, request.FILES)
#         if form.is_valid():
#             count39 = form.cleaned_data["count39"]
#             count40 = form.cleaned_data["count40"]
#             count41 = form.cleaned_data["count41"]
#             # count = count39 + count40 + count41  # Tính tổng count từ count39, count40, count41
#             name = form.cleaned_data["name"]
#             category = form.cleaned_data["category"]
#             price = form.cleaned_data["price"]
#             price_sale = form.cleaned_data["price_sale"]
#             describe = form.cleaned_data["describe"]
#             # digital = form.cleaned_data["digital"]
#             image = form.cleaned_data["image"]
#             image1 = form.cleaned_data["image1"]
#             image2 = form.cleaned_data["image2"]
#             image3 = form.cleaned_data["image3"]
#             image4 = form.cleaned_data["image4"]
#             unit = form.cleaned_data["unit"]
#             print(count)
#             print(category)
#             print(name)
#             print(price)
#             print(price_sale)
            
#             print(describe)
#             print(image)
#             print(image1)
#             print(image2)
#             print(image3)
#             print(image4)
#             print(unit)

#             product = Product(
#                 name=name,
#                 category=category,
#                 price=price,
#                 price_sale=price_sale,
#                 describe=describe, 
#                 digital = False,
#                 count39=count39, 
#                 count40=count40,
#                 count41=count41, 
#                 image=image, 
#                 image1=image1, 
#                 image2=image2, 
#                 image3=image3,
#                 image4=image4, 
#                 unit=unit, 
#                 count=count39 + count40 + count41)
#             print("gfhdsjgfgd: ")
#             print(product)
#             product.save()
#             name = models.CharField(max_length=200, null=True)
#             messages.success(request, 'Product saved successfully!')
#             return redirect('manageProduct') # Chuyển hướng sau khi thêm sản phẩm thành công
#         else:
#             count = 0
#             count39 = form.cleaned_data["count39"]
#             count40 = form.cleaned_data["count40"]
#             count41 = form.cleaned_data["count41"]
#             # count = count39 + count40 + count41  # Tính tổng count từ count39, count40, count41
#             name = form.cleaned_data["name"]
#             category = form.cleaned_data["category"]
#             price = form.cleaned_data["price"]
#             price_sale = form.cleaned_data["price_sale"]
#             describe = form.cleaned_data["describe"]
            
#             image = form.cleaned_data["image"]
#             image1 = form.cleaned_data["image1"]
#             image2 = form.cleaned_data["image2"]
#             image3 = form.cleaned_data["image3"]
#             image4 = form.cleaned_data["image4"]
#             unit = form.cleaned_data["unit"]
#             print("loix form")
#             print(form.errors)
#             print(form.errors.as_data())
#             print()
#             print(count)
#             print(category)
#             print(name)
#             print(price)
#             print(price_sale)
            
#             print(describe)
#             print(image)
#             print(image1)
#             print(image2)
#             print(image3)
#             print(image4)
#             print(unit)
#     else:
#         count = 0
#         form = AddProduct()
#     context = {'form': form,'messages': messages,}
#     return render(request, 'admin/addProduct.html', context)
    

def addProduct(request):
    form = AddProduct()
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Thông báo thành công và chuyển hướng
            messages.success(request, 'Product saved successfully!')
            return redirect('manageProduct')
        else:
            # Xử lý trường hợp form không hợp lệ
            print(form.errors.as_data())
            print(form.errors)
            count = 0  # Hoặc giá trị mặc định khác tùy ý
    else:
        form = AddProduct()
        count = 0  # Hoặc giá trị mặc định khác tùy ý

    context = {'form': form, 'messages': messages, 'count': count}
    return render(request, 'admin/addProduct.html', context)



def editProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng click vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('manageProduct')
    form = AddProduct(instance=product,
                      initial={'name': product.name,
                               'category': product.category.values_list('id', flat=True),
                               'price': product.price,
                               'describe': product.describe,
                               'image': product.image})

    context = {'product': product,
               'form': form}
    return render(request, 'admin/editProduct.html', context)

def deleteProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('manageProduct')
    context ={'product': product}
    return render(request, 'admin/deleteProduct.html', context)

def viewProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    user = request.user
    print(user)
    product = get_object_or_404(Product, id=id)
    count = product.count39 + product.count40 + product.count41
    context = {'product': product,
               'count': count,}
    return render(request, 'admin/view_product.html', context)