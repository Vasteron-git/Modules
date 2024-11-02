from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        # file.close()
        return file.read()
    def add(self, *products):
        exist_products = self.get_products().split('\n')
        # pprint(exist_products)
        exist_names = []
        for product in exist_products:
            if product:
                exist_names.append(product.split(', ')[0])
        # exist_names = [product.split(', ')[0] for product in exist_products if product]
        # pprint(exist_names)
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name not in exist_names:
                file.write(str(product) + '\n')  # Записываем продукт в файл
            else:
                 print(f'Продукт {product} уже есть в магазине')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

