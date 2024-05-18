from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *


def manageProduct(request):
    products = Product.objects.all()
    form = AddProduct()
    context = {'products': products}
    return render(request, 'admin/managementProduct.html', context)

def addProduct(request):
    if request.method == 'POST':
        images = request.FILES.getlist('listImages')
        product_form = AddProduct(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            instance = product.save()
            product_form.save_m2m()
            for image in request.FILES.getlist('images'):
                instance.image.create(image=image)

            for image in images:
                photo = ImagesProduct.objects.create(product=instance, image=image)

            sizes = request.POST.getlist('sizes[]')
            quantities = request.POST.getlist('quantities[]')

            for size, quantity in zip(sizes, quantities):
                if size and quantity:
                    Size.objects.create(product=product, size=size, quantity=quantity)

            messages.success(request, 'Thêm sản phẩm thành công')
            return redirect('manageProduct')
    else:
        product_form = AddProduct()
    return render(request, 'admin/addProduct.html', {'product_form': product_form})
def editProduct(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng click vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        images = request.FILES.getlist('listImages')
        form = AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            for image in request.FILES.getlist('images'):
                instance.image.create(image=image)
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

    context = {'product': product,
               }
    return render(request, 'admin/view_product.html', context)