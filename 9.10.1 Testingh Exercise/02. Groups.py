import unittest

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('Bai', 'Ivan')

    def test_custom_add(self):
        person_2 = Person('Second', 'Person')
        person_3 = self.person + person_2
        self.assertEqual(person_3.name, 'Bai')
        self.assertEqual(person_3.surname, 'Person')

    def test_custom_string(self):
        self.assertEqual(self.person.__str__(), 'Bai Ivan')


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.person_1 = Person('Bai', 'Ivan')
        self.person_2 = Person('Second', 'Person')
        self.group = Group('Group 1', [self.person_1, self.person_2])

    def test_custom_add(self):
        person_3 = Person('Third', 'Person')
        group_2 = Group('Group 2', [person_3])
        group_3 = self.group + group_2
        self.assertEqual(len(group_3), 3)

    def test_custom_len(self):
        result = len(self.group)
        self.assertEqual(result, 2)

    def test_custom_getitem(self):
        result = self.group[1]
        self.assertIn('Second', result)
        self.assertEqual(result, 'Person 1: Second Person')

    def test_custom_getitem_wrong_index(self):
        with self.assertRaises(IndexError):
            result = self.group[4]

    def test_custom_str(self):
        result = str(self.group)
        self.assertIn('Bai', result)
        self.assertIn('Second', result)
        self.assertIn('Group', result)
        self.assertNotIn('Third', result)
        self.assertEqual(result, 'Group Group 1 with members Bai Ivan, Second Person')


if __name__ == '__main__':
    unittest.main()