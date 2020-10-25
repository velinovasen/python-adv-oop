import unittest
from SoftuniAdvanced.OOP.testing.account.account import Account


class AccountTests(unittest.TestCase):
    def test_if_correct_input_is_fine(self):
        acc = Account('bob', 10)
        expected_name = 'bob'
        expected_amount = 10

        self.assertEqual(acc.owner, expected_name)
        self.assertEqual(acc.amount, expected_amount)

    def test_if_balance_is_updating(self):
        acc = Account('bob', 10)
        expected_amount = 10

        self.assertEqual(acc.balance, expected_amount)

    def test_if_valid_transaction_is_appended(self):
        acc = Account('bob', 10)
        transaction_to_append = 5
        acc.add_transaction(transaction_to_append)

        self.assertIn(transaction_to_append, acc._transactions)

    def test_if_invalid_transaction_raises_err(self):
        acc = Account('bob', 10)
        transaction_to_append = None
        with self.assertRaises(ValueError) as context:
            acc.add_transaction(transaction_to_append)

        self.assertRaises(ValueError, context)

    def test_if_str_method_returns_as_expected(self):
        acc = Account('bob', 10)
        self.assertEqual(str(acc), f"Account of {acc.owner} with starting amount: {acc.amount}")

    def test_if_repr_method_returns_as_expected(self):
        acc = Account('bob', 10)
        self.assertEqual(repr(acc), f"Account({acc.owner}, {acc.amount})")

    def test_if_len_method_is_working(self):
        acc = Account('bob', 100)
        acc.add_transaction(10)
        acc.add_transaction(10)
        acc.add_transaction(10)
        self.assertEqual(len(acc._transactions), 3)

    def test_if_comparison_is_working_correct(self):
        acc = Account('bob', 100)
        acc2 = Account('mike', 50)
        self.assertTrue(acc > acc2)
        self.assertTrue(acc != acc2)
        self.assertTrue(acc2 < acc)

    def test_if_comparison_raises_error(self):
        acc = Account('bob', 100)
        acc2 = Account('mike', 50)
        self.assertFalse(acc == acc2)
        self.assertFalse(acc < acc2)
        self.assertFalse(acc2 > acc)

    def test_if_add_method_is_working_fine(self):
        acc = Account('bob', 100)
        acc2 = Account('mike', 50)
        acc3 = acc + acc2
        trans_expected = len(acc._transactions + acc2._transactions)
        self.assertEqual(acc3.owner, 'bob&mike')
        self.assertEqual(acc3.amount, 150)
        self.assertEqual(len(acc3._transactions), trans_expected)

if __name__ == '__main__':
    unittest.main()