import unittest
from SoftuniAdvanced.OOP.testing.groups.groups import Person, Group
## TO DO TEST FOR AUTO INCREMENT TEST NUMBER


class Group_Tests(unittest.TestCase):
    def test_if_correct_person_input_is_fine(self):
        person = Person('Asen', 'Velinov')
        self.assertEqual(person.name, 'Asen')
        self.assertEqual(person.surname, 'Velinov')

    def test_if_incorrect_person_input_raises(self):
        with self.assertRaises(TypeError) as context:
            per = Person()
        self.assertRaises(TypeError, context)

    def test_if_add_method_is_working_fine(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Sestrimska')
        person3 = person2 + person
        self.assertEqual(str(person3), 'Julka Velinov')

    def test_if_str_method_returns_as_expected(self):
        person = Person('Asen', 'Velinov')
        self.assertEqual(person.__str__(), 'Asen Velinov')

    def test_if_group_class_input_is_working_fine(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Velinova')
        group1 = Group('Velinovi', [person, person2])
        self.assertEqual(group1.name, 'Velinovi')
        self.assertEqual(group1.people[0].__str__(), 'Asen Velinov')
        self.assertEqual(len(group1.people), 2)

    def test_if_wrong_group_class_input_raises(self):
        with self.assertRaises(TypeError) as context:
            group1 = Group('Velinovi')
        self.assertRaises(TypeError, context)

    def test_if_group_len_returns_correct(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Velinova')
        group1 = Group('Velinovi', [person, person2])
        expected_len = 2
        self.assertEqual(len(group1), expected_len)

    def test_if_str_func_in_group_returns_correct(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Velinova')
        group1 = Group('Velinovi', [person, person2])
        expected_output = f"Group {group1.name} with members: {', '.join([f'{x.name} {x.surname}' for x in group1.people])}"
        self.assertEqual(str(group1), expected_output)

    def test_if_get_item_in_group_works_correct(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Velinova')
        group1 = Group('Velinovi', [person, person2])
        indx_to_get = 0
        expected_output = f"Person {indx_to_get}: {group1.people[indx_to_get].__str__()}"
        self.assertEqual(str(group1[indx_to_get]), expected_output)

    def test_if_add_func_in_group_works_correct(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Velinova')
        group1 = Group('BLG', [person])
        group2 = Group('Sofia', [person2])
        group3 = group1 + group2
        self.assertEqual(group3.name, 'BLG&Sofia')
        self.assertEqual(len(group3), 2)

    def test_if_wrong_input_in_add_func_in_group_raises(self):
        person = Person('Asen', 'Velinov')
        person2 = Person('Julka', 'Velinova')
        group1 = Group('BLG', [person])
        group2 = Group('Sofia', [person2])
        with self.assertRaises(TypeError) as context:
            group3 = group1 + None
        self.assertRaises(TypeError, context)

if __name__ == '__main__':
    unittest.main()
