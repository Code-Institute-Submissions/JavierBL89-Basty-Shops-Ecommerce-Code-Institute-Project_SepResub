from django.shortcuts import get_object_or_404
from products.models import Product, Size


def handle_stock(item_size_id):

    data_item = Size.objects.filter(id=item_size_id).all()
    for data in data_item.values():
        product_id = data['product_id_id']
        size_id = data['id']
        size = data['size']
        size_stock = data['stock'] - 1

        new_stock = Size(id=size_id, product_id_id=product_id, size=size, stock=size_stock)
        new_stock.save()
        print(data, 'dataaaaa')


def decrement_stock(item_size_id):

    data_item = Size.objects.filter(id=item_size_id).all()

    # print(stock)
    for data in data_item.values():
        product_id = data['product_id_id']
        size_id = data['id']
        size = data['size']
        size_stock = data['stock'] - 1

        new_stock = Size(id=size_id, product_id_id=product_id, size=size, stock=size_stock)
        new_stock.save()
        print(data, 'dataaaaa')
        print(data)


def increment_stock(item_size_id):

    data_item = Size.objects.filter(id=item_size_id).all()

    # print(stock)
    for data in data_item.values():

        product_id = data['product_id_id']
        size_id = data['id']
        size = data['size']
        size_stock = data['stock'] + 1

        new_stock = Size(id=size_id, product_id_id=product_id, size=size, stock=size_stock)
        new_stock.save()
        print(data, 'dataaaaa')
        print(data)


def update_stock(item_size_id, quantity):

    data_item = Size.objects.filter(id=item_size_id).all()
    for data in data_item.values():
        product_id = data['product_id_id']
        size_id = data['id']
        size = data['size']
        size_stock = data['stock'] + int(quantity)

        new_stock = Size(id=size_id, product_id_id=product_id, size=size, stock=size_stock)
        new_stock.save()


def handle_stock_admin(request, product_id, product_sizes):
    
    for sizes in list(product_sizes.values()):
        size = sizes['size']
        if size == '36':
            size_id = sizes['id']
            size_number = sizes['size']
            size_stock = sizes['stock']
            size_stock = request.POST['stock_size_36']
            new_stock = Size(id=size_id, product_id_id=product_id, size=size_number, stock=size_stock)
            new_stock.save()
        if size == '37':
            size_id = sizes['id']
            size_number = sizes['size']
            size_stock = sizes['stock']
            size_stock = request.POST['stock_size_37']
            new_stock = Size(id=size_id, product_id_id=product_id, size=size_number, stock=size_stock)
            new_stock.save()
        if size == '38':
            size_id = sizes['id']
            size_number = sizes['size']
            size_stock = sizes['stock']
            size_stock = request.POST['stock_size_38']
            new_stock = Size(id=size_id, product_id_id=product_id, size=size_number, stock=size_stock)
            new_stock.save()
        if size == '39':
            size_id = sizes['id']
            size_number = sizes['size']
            size_stock = sizes['stock']
            size_stock = request.POST['stock_size_39']
            new_stock = Size(id=size_id, product_id_id=product_id, size=size_number, stock=size_stock)
            new_stock.save()
        if size == '40':
            size_id = sizes['id']
            size_number = sizes['size']
            size_stock = sizes['stock']
            size_stock = request.POST['stock_size_40']
            new_stock = Size(id=size_id, product_id_id=product_id, size=size_number, stock=size_stock)
            new_stock.save()
