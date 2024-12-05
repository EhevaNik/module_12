from Runner_2 import *
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.beg_1 = Runner('Усэйн', 10)
        self.beg_2 = Runner('Андрей', 9)
        self.beg_3 = Runner('Ник', 3)
        self.dist = 90

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_tourne1(self):
        tourne_1 = Tournament(self.dist, self.beg_1, self.beg_3)
        result = tourne_1.start()
        self.all_results['test_tourne1'] = result

    def test_tourne2(self):
        tourne_2 = Tournament(self.dist, self.beg_2, self.beg_3)
        result = tourne_2.start()
        self.all_results['test_tourne2'] = result

    def test_tourne3(self):
        tourne_3 = Tournament(self.dist, self.beg_1, self.beg_2, self.beg_3)
        result = tourne_3.start()
        self.all_results['test_tourne3'] = result