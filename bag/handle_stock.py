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

        # print(new_stock, 'putaaaa')
        # print(data, 'dataaaaa')
        # stock = data_item(stock=puta)
        # stock.save()
        # print(data['stock'], 'dataaaaa')
        # data['stock'] -= 1
        # if data['stock'] >= 0:
        #     data_item[data]['stock'] -= 1
        # item_stock = data['stock']
        # puta = data['stock'] = item_stock
        # print(item_stock, 'putaaaaaa')
        # print(item_stock, 'item size stock')
        print(data)


        # new_stock = item_stock - 1
        # new_stock.save()
        # print(list(data_item), 'new stock')
