from products.models import Product, Size


def handle_stock(item_size_id):

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
        print(data, 'dataaaaa')
        print(data)


