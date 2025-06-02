# DONE
from abc import ABC, abstractmethod
from typing import List, Tuple


class Order:
    def __init__(self, items: List[Tuple[str, int, float]]):
        """
        Initialize an Order with a list of items.

        Args:
        items (List[Tuple[str, int, float]]): A list where each tuple represents an item in the order.
            Each tuple contains:
                - item_name (str): The name of the item.
                - quantity (int): The number of units of the item.
                - price_per_unit (float): The price of a single unit of the item.

        Example:
        items = [
            ("apple", 2, 0.5),  # 2 apples, each costing $0.5
            ("banana", 5, 0.3), # 5 bananas, each costing $0.3
        ]
        """
        self.items = items

    def calculate_total(self) -> float:
        """
        Calculate the total price of all items in the order.

        Returns:
        float: The total price of the order.
        """
        return sum(quantity * price for _, quantity, price in self.items)


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):

    def pay(self, amount):
        print(f'Processing credit card payment for ${amount}')



class PayPalPayment(PaymentMethod):

    def pay(self, amount):
        print(f'Processing PayPal payment for ${amount}')


class PaymentProcessor:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, order: Order):

        total_amount = order.calculate_total()
        self.payment_method.pay(total_amount)



order_obj = Order([
    ('Apple', 2, 1.0),
    ('Banana', 5, 0.5)
])

credit_card_payment = CreditCardPayment()
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(order_obj)
