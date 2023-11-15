class Product:
    def __init__(self, name, model, price) -> None:
        self.name = name
        self.model = model
        self.price = price


class Test(Product):
    def __init__(self, name, model, price, max_speed) -> None:
        super().__init__(name, model, price)
        self.max_speed = max_speed

    def speed(self):
        print(f'Test show that {self.name}({self.model}) get maximum speed {
              self.max_speed} km/h')


tesla = Product('Tesla', 'Model T', 60000)
porsche = Test('Porsche', '918', 160000, 318)
porsche.speed()
