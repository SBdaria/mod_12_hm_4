import logging
import rt_with_exceptions as rt
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            test_runner = rt.Runner('Elsa', speed=-5)
            logging.info(msg='"test_walk" выполнен успешно')
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
        except:
            logging.warning(msg="Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            test_runner = rt.Runner(('Nika', 'Lenina'))
            logging.info(msg='"test_run" выполнен успешно')
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
        except:
            logging.warning(msg="Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        test_runner1 = rt.Runner('Elsa')
        test_runner2 = rt.Runner('Nika')
        for _ in range(10):
            test_runner1.run()
            test_runner2.walk()
        self.assertNotEqual(test_runner1.distance, test_runner2.distance)

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = rt.Runner('Усэйн', 4)
        self.runner2 = rt.Runner('Андрей', 5)
        self.runner3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    def test_tour1(self):
        tour = rt.Tournament(9, self.runner1, self.runner3)
        self.all_results['test1'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1],'Ник')

    def test_tour2(self):
        tour = rt.Tournament(9, self.runner2, self.runner3)
        self.all_results['test2'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1],'Ник')

    def test_tour3(self):
        tour = rt.Tournament(9, self.runner1, self.runner2, self.runner3)
        self.all_results['test3'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[-1],'Ник')

    def test_tour4(self):
        tour = rt.Tournament(9, self.runner1, self.runner2, self.runner3)
        self.all_results['test4'] = tour.start()
        temp = list(self.all_results.values())
        self.assertTrue(temp[0],'Андрей')

if __name__ == "__main__":
    unittest.main()