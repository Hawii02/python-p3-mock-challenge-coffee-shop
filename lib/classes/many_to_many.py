class Coffee:
    all = []
    def __init__(self, name):
        self._name = name
        self.customers_list = []
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be be greater or equal to 3 characters")
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("cannot change the name of the coffee")
        self._name = value


    def orders(self):
        return[order for order in Order.all if order.coffee == self]
        
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def add_customer(self, customer):
        if customer not in self.customers_list:
            self.customers_list.append(customer)
        
    
    def num_orders(self):
        return len(self.orders())
        
    
    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        return total_price / len(self.orders()) if self.orders() else None

class Customer:
    all = []
    def __init__(self, name):
        self._name = None
        self.name = name
        self.orders_list = []
        Customer.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) > 15:
            raise ValueError("Name must be 15 characters or less")
        self._name = value

    def orders(self):
       return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        new_order = Order(self, coffee, price)
        return new_order
        
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    def get_price(self):
        return self._price

    def set_price(self, val):
        if isinstance(val, float) and 1.0  <= val <= 10.0 and not hasattr(self, 'price'):
            self._price = val

    price = property(get_price, set_price)

# def test_create_order():
#     customer = Customer("John")
#     coffee = Coffee("Cappucino")
#     customer.create_order(coffee, 10)
#     assert True
# print(test_create_order())


