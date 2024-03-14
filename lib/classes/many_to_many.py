class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
        
    def orders(self):
        return[order for order in Order.all if order.coffee == self]
        
    
    def customers(self):
        return[customer for customer in Customer.all if Customer.coffee == self]
        
    
    def num_orders(self):
        
        return orders,get(coffee, 0)
    
    def average_price(self):
        pass

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        self.orders = []
        Customer.all.append(self)

    def orders(self):
        return[order for order in self.orders if isinstance(order, Order)]
    
    def coffees(self):
        # coffee_set = set()
        # for order in self.orders:
        #     for coffee in order.coffee: 
        #         if isinstance(coffee, Coffee):
        #             coffee_set.add(coffee)
        # return list(coffee_set)
        pass
    
    def create_order(self, coffee, price):
        self.coffee = coffee
        self.price = price

class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
