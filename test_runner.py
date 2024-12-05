# Домашнее задание по теме "Простые Юнит-Тесты"
# Задача "Проверка на выносливость"


import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Test walk method in runner
        :return
        """
        name_1 = runner.Runner('Камамбер')
        for i in range(10):
            name_1.walk()
        self.assertEqual(name_1.distance, 50)

    def test_run(self):
        """ Test run method in runner
        :return
        """
        name_2 = runner.Runner('Гауда')
        for i in range(10):
            name_2.run()
        self.assertEqual(name_2.distance, 100)

    def test_challenge(self):
        """Test of two objects
        :return
        """
        name_3 = runner.Runner('Тильзитер')
        name_4 = runner.Runner('Моцарелла')
        for i in range(10):
            name_3.walk()
            name_4.run()
        self.assertNotEqual(name_3.distance, name_4.distance)


if __name__ == "__main__":
    unittest.main()