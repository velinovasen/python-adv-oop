from project.survivor import Survivor
import unittest


class SurvivorTests(unittest.TestCase):
    def test_set_attr(self):
        survivor = Survivor('test', 20)
        self.assertEqual(survivor.name, 'test')
        self.assertEqual(survivor.age, 20)
        self.assertEqual(survivor.health, 100)
        self.assertEqual(survivor.needs, 100)

    def test_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Survivor('', 20)
        self.assertEqual(str(ex.exception), "Name not valid!")

    def test_age_raises(self):
        with self.assertRaises(ValueError) as ex:
            Survivor('test', -2)
        self.assertEqual(str(ex.exception), "Age not valid!")

    def test_health_setter(self):
        survivor = Survivor('test', 20)
        survivor.health = 60
        self.assertEqual(survivor.health, 60)
        survivor.health += 20
        self.assertEqual(survivor.health, 80)
        survivor.health += 40
        self.assertEqual(survivor.health, 100)
        with self.assertRaises(ValueError) as ex:
            survivor.health = -50
        self.assertEqual(str(ex.exception), "Health not valid!")

    def test_needs_setter(self):
        survivor = Survivor('test', 20)
        survivor.needs = 60
        self.assertEqual(survivor.needs, 60)
        survivor.needs += 20
        self.assertEqual(survivor.needs, 80)
        survivor.needs += 40
        self.assertEqual(survivor.needs, 100)
        with self.assertRaises(ValueError) as ex:
            survivor.needs = -50
        self.assertEqual(str(ex.exception), "Needs not valid!")

    def test_needs_sustenance(self):
        survivor = Survivor('test', 20)
        self.assertFalse(survivor.needs_sustenance)
        survivor.needs -= 20
        self.assertTrue(survivor.needs_sustenance)

    def test_needs_healing(self):
        survivor = Survivor('test', 20)
        self.assertFalse(survivor.needs_healing)
        survivor.health -= 20
        self.assertTrue(survivor.needs_healing)