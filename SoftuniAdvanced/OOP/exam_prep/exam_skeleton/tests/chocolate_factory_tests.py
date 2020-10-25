from SoftuniAdvanced.OOP.exam_prep.exam_skeleton.project.factory.chocolate_factory import ChocolateFactory
import unittest


class ChocolateFactoryTests(unittest.TestCase):
    def setUp(self):
        self.ch_f = ChocolateFactory('Paris', 30)
        self.ch_f.add_ingredient('white chocolate', 10)

    def test_classes_inherited(self):
        par_class = str(self.ch_f.__class__.mro()[1]).split('.')[-1][::][:7]
        abc_class = str(self.ch_f.__class__.mro()[2]).split('.')[-1][:3]
        self.assertEqual(par_class, 'Factory')
        self.assertEqual(abc_class, 'ABC')

    def test_setattr_is_successful(self):
        self.ch_f.name = 'Sofia'
        self.ch_f.capacity = 20
        self.assertEqual(self.ch_f.name, 'Sofia')
        self.assertEqual(self.ch_f.capacity, 20)

    def test_add_ingredient_wrong_type_expect_raise(self):
        with self.assertRaises(TypeError) as context:
            self.ch_f.add_ingredient('test', 5)
        self.assertRaises(TypeError, context)

    def test_add_ingredient_bigger_quantity_expect_raise(self):
        with self.assertRaises(ValueError):
            self.ch_f.add_ingredient('sugar', 30)

    def test_add_ingredient_expect_success(self):
        self.ch_f.add_ingredient('sugar', 5)
        self.assertEqual(sum([x for x in self.ch_f.ingredients.values()]), 15)
        self.assertEqual(self.ch_f.ingredients['sugar'], 5)

    def test_remove_item_should_raise_not_existing(self):
        with self.assertRaises(TypeError):
            self.ch_f.remove_ingredient('test', 2)
        self.assertRaises(TypeError)

    def test_remove_item_should_raise_if_quantity_less_than_zero(self):
        with self.assertRaises(ValueError):
            self.ch_f.remove_ingredient('white chocolate', 50)
        self.assertRaises(ValueError)

    def test_valid_input_should_be_fine(self):
        self.ch_f.remove_ingredient('white chocolate', 2)
        self.assertEqual(self.ch_f.ingredients['white chocolate'], 8)
        self.ch_f.remove_ingredient('white chocolate', 5)
        self.assertEqual(self.ch_f.ingredients['white chocolate'], 3)

    def test_valid_recite_input_should_have_success(self):
        self.ch_f.add_recipe('cake', {'cake': 'dsdaeweasdwe'})
        self.assertIn('cake', self.ch_f.recipes)

    def test_make_choco_raise_invalid_receipt(self):
        with self.assertRaises(TypeError):
            self.ch_f.make_chocolate('test')
        self.assertRaises(TypeError)

    def test_make_choco_successful(self):
        self.ch_f.add_recipe('cake', {'cake': 'dsdaeweasdwe'})
        self.ch_f.make_chocolate('cake')
        self.assertEqual(len(self.ch_f.ingredients), 0)
        self.assertTrue(len(self.ch_f.products) > 0)


if __name__ == '__main__':
    unittest.main()
