class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Customer: {self.get_customer()}")
        print(f"     Quantity: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class QueueInterface:
    def size(self):
        raise NotImplementedError("Subclasses should implement this!")

    def is_empty(self):
        raise NotImplementedError("Subclasses should implement this!")

    def front(self):
        raise NotImplementedError("Subclasses should implement this!")

    def enqueue(self, info):
        raise NotImplementedError("Subclasses should implement this!")

    def dequeue(self):
        raise NotImplementedError("Subclasses should implement this!")


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_next(self):
        return self.next_node


class SimpleQueue(QueueInterface):
    def __init__(self):
        self.top = None
        self.size_count = 0

    def size(self):
        return self.size_count

    def is_empty(self):
        return self.size_count == 0

    def front(self):
        return self.top.data if self.top else None

    def enqueue(self, info):
        new_node = Node(info)
        if self.top is None:
            self.top = new_node
        else:
            current = self.top
            while current.get_next() is not None:
                current = current.get_next()
            current.next_node = new_node
        self.size_count += 1

    def dequeue(self):
        if self.top is None:
            return None
        removed_data = self.top.data
        self.top = self.top.get_next()
        self.size_count -= 1
        return removed_data

    def dump(self):
        print("********* QUEUE DUMP *********")
        print(f"   Size: {self.size()}")
        current = self.top
        index = 1
        while current is not None:
            print(f"   ** Element {index}")
            current.data.print_order()  # Imprimir la información del pedido
            current = current.get_next()
            index += 1
        print("******************************")


# Ejemplo de uso
queue = SimpleQueue()
order1 = Order(20, "cust1")
order2 = Order(30, "cust2")
order3 = Order(40, "cust3")
order4 = Order(50, "cust4")

queue.enqueue(order1)
queue.enqueue(order2)
queue.enqueue(order3)
queue.enqueue(order4)

queue.dump()
