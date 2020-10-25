from project.factory.paint_factory import PaintFactory
import unittest


class PaintFactoryTests(unittest.TestCase):
    def test_set_attr(self):
        paint_f = PaintFactory('test', 20)
        self.assertEqual(paint_f.name, 'test')
        self.assertEqual(paint_f.capacity, 20)
        self.assertEqual(paint_f.ingredients, {})
        self.assertEqual(paint_f.products, {})

    def test_add_ingredient(self):
        paint_f = PaintFactory('test', 20)
        paint_f.add_ingredient('red', 5)
        self.assertIn('red', paint_f.ingredients)
        self.assertEqual(paint_f.ingredients['red'], 5)
        with self.assertRaises(TypeError) as ex:
            paint_f.add_ingredient('sd', 5)
        self.assertEqual(str(ex.exception), f"Ingredient of type sd not allowed in PaintFactory")
        with self.assertRaises(ValueError) as ex:
            paint_f.add_ingredient('red', 20)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_remove_ingredient(self):
        paint_f = PaintFactory('test', 20)
        paint_f.add_ingredient('red', 5)
        paint_f.remove_ingredient('red', 2)
        self.assertEqual(paint_f.ingredients['red'], 3)
        with self.assertRaises(KeyError) as ex:
            paint_f.remove_ingredient('sd', 2)
        self.assertEqual(str(ex.exception), "'No such ingredient in the factory'")
        with self.assertRaises(ValueError) as ex:
            paint_f.remove_ingredient('red', 10)
        self.assertEqual(str(ex.exception), "Ingredient quantity cannot be less than zero")

    def test_products_method(self):
        paint_f = PaintFactory('test', 20)
        paint_f.add_ingredient('red', 5)
        self.assertIn('red', paint_f.products)

    def test_can_add_method(self):
        paint_f = PaintFactory('test', 20)
        paint_f.add_ingredient('red', 5)
        self.assertIn('red', paint_f.ingredients.keys())
        with self.assertRaises(ValueError) as ex:
            paint_f.add_ingredient('red', 20)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_repr_method(self):
        paint_f = PaintFactory('test', 20)
        paint_f.add_ingredient('red', 10)
        expected_output = f"Factory name: {paint_f.name} with capacity {paint_f.capacity}.\n"
        for key, value in paint_f.ingredients.items():
            expected_output += f"{key}: {value}\n"
        self.assertEqual(paint_f.__repr__(), expected_output)