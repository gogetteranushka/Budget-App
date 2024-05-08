import unittest
from budget import Category, create_spend_chart

class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        # Set up category objects for testing
        self.food = Category("Food")
        self.clothing = Category("Clothing")

    def test_deposit_method(self):
        # Test deposit method functionality
        self.food.deposit(900, "deposit")
        self.assertEqual(self.food.ledger[0], {"amount": 900, "description": "deposit"})
        self.food.deposit(500)  # Test with no description
        self.assertEqual(self.food.ledger[1], {"amount": 500, "description": ""})

    def test_withdraw_method(self):
        # Test withdraw method functionality
        self.food.deposit(900, "deposit")
        self.assertTrue(self.food.withdraw(45.67, "milk, cereal, eggs, bacon, bread"))
        self.assertEqual(self.food.get_balance(), 854.33)
        self.assertTrue(self.food.withdraw(100))  # Test with no description
        self.assertEqual(self.food.get_balance(), 754.33)

    def test_transfer_method(self):
        # Test transfer method functionality
        self.food.deposit(900, "deposit")
        self.assertTrue(self.food.transfer(50, self.clothing))
        self.assertEqual(self.food.get_balance(), 850)
        self.assertEqual(self.clothing.get_balance(), 50)
        self.assertTrue(self.clothing.transfer(20, self.food))  # Test transfer back
        self.assertEqual(self.clothing.get_balance(), 30)
        self.assertEqual(self.food.get_balance(), 870)

    def test_check_funds_method(self):
        # Test check_funds method functionality
        self.food.deposit(500)
        self.assertTrue(self.food.check_funds(300))
        self.assertFalse(self.food.check_funds(700))

    def test_string_representation(self):
        # Test string representation of Category objects
        self.assertEqual(str(self.food), "*************Food*************\n")
        self.assertEqual(str(self.clothing), "***********Clothing***********\n")

    def test_create_spend_chart(self):
        # Test create_spend_chart function
        self.food.deposit(1000, "initial deposit")
        self.food.withdraw(10.15, "groceries")
        self.clothing.deposit(500, "initial deposit")
        self.clothing.withdraw(5.75, "clothing")
        expected_chart = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|          \n 60|          \n 50|          \n 40|          \n 30|          \n 20|    o     \n 10|    o     \n  0| o  o     \n    ----------\n     F  C     \n     o  l     \n     o  o     \n     d  t     \n        h     \n        i     \n        n     \n        g     \n"
        self.assertEqual(create_spend_chart([self.food, self.clothing]), expected_chart)

if __name__ == '__main__':
    unittest.main()
