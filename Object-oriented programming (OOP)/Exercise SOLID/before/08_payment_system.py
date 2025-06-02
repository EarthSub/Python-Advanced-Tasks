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

    def process_payment(self, payment_type: str) -> None:
        """
        Process the payment based on the payment type.

        Args:
        payment_type (str): The type of payment (e.g., 'credit_card', 'paypal').
        """
        total_amount = self.calculate_total()

        if payment_type == 'credit_card':
            print(f'Processing credit card payment for ${total_amount}')
        elif payment_type == 'paypal':
            print(f'Processing PayPal payment for ${total_amount}')
        else:
            print('Unsupported payment type.')



order_obj = Order([
 ('Apple', 2, 1.0),
 ('Banana', 5, 0.5)
])

order_obj.process_payment('credit_card')
