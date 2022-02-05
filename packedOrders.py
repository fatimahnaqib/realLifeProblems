
# - The following are the the Products and packaging boxes information
#   of Acme Inc.
# - Each product in given dictionary/hash contain possible packing boxes
#   that can be used to ship the product when ordered
# - Each packaging boxes gives you how many numbers of the given product
#   can be packed in the box.
# - Packing box names are just reference names, they are not dimension
#   of the packing box
# - Following are product details where data structure will be consistent
#   but number of product and boxes available for given product will be
#   variable and you will not know their size before hand.
# - You can use  as many as boxes you like from the boxes list

product_boxes = {
   'IoT Box': {
       'BOX-06x02x02': 2.0,
       'BOX-20x20x12': 16.0,
       'BOX-16x16x16': 9.0,
       'BOX-08x08x08': 4.0,
   },
   'Scale-Up! The Business Game': {
       'BOX-16x16x16': 7.0,
       'BOX-10x08x08': 3.0,
       'BOX-23x17x12': 14.0,
   },
   'Basic Cash Drawer': {},
   'Shoes': {
       'BOX-06x02x02': 6.0,
   }
}

# -Following data contians order details with an order number, the ordered
#  products and their initial demand of product quantity by customer
# - Orders data structure will be consistent but data in orders will vary


orders = {
   'S0101': {
       'Scale-Up! The Business Game': 15.0,
       'Basic Cash Drawer': 10.0,
       'IoT Box': 47.0,
   },
   'S0102': {
       'IoT Box': 2.0,
       'Scale-Up! The Business Game': 10.0,
   },
   'S0103': {
       'IoT Box': 500.0,
       'Scale-Up! The Business Game': 32.0,
       'Basic Cash Drawer': 10.0,
   },
}

# - Write a program/script/solution to find and return the best and least
# possible packing boxes to be used for shipping the ordered products
# in an order.
# - Also, each box should give a count of product quantity to be packed
# in each selected boxe(s) from the given list.

"""
Expected output

packed_orders = {
    'S0101': {
        'Scale-Up! The Business Game': {
            'packs': [('BOX-23x17x12', 14.0),
                      ('BOX-10x08x08', 1.0)],
            'quantity': 15.0
        },
        'IoT Box': {
            'packs': [('BOX-20x20x12', 16.0),
                      ('BOX-20x20x12', 16.0),
                      ('BOX-16x16x16', 9.0),
                      ('BOX-08x08x08', 4.0),
                      ('BOX-06x02x02', 2.0)],
            'quantity': 47.0
        },
        'Basic Cash Drawer': {
            'packs': [],
            'quantity': 10.0
        },
        'Shoes': {
            'packs': [('BOX-06x02x02', 5.0)],
            'quantity': 5.0
        }
    },
    'S0102': {...},
    'S0103': {...},
}


"""

productOrders = {}
for order_no, prod_boxes in orders.items():
    productBoxes = {}
    for product_box, quantity in prod_boxes.items():
        packed_products = {}
        total_quantity = quantity
        products = product_boxes[product_box]
        packs = []

        if not products:
            packed_products['packs'] = packs
        else:

            while total_quantity >= min(products.values()):
                # print(f"{res} is higher than {min(boxes.values())}")
                max_size = ('name',0)
                for name, prod_size in products.items():
                    if prod_size > max_size[1] and prod_size <= total_quantity:
                        max_size = name, prod_size
                total_quantity -= max_size[1]
                packs.append(max_size)
            if total_quantity:
                smallest_box = min(products, key=lambda k: products[k])
                packs.append((smallest_box,total_quantity))

            packed_products['packs'] = packs

        packed_products['quantity'] = quantity


        productBoxes[product_box] = packed_products
    productOrders[order_no] = productBoxes

print(productOrders)

