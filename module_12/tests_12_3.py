import unittest
import runner as r
import runner_and_tournament as rat

# Декоратор, который пропускает тесты в зависимости от атрибута is_frozen
def skip_if_frozen(test_method):
    def wrapper(self):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self)
    return wrapper

# Класс тестов для Runner
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @skip_if_frozen
    def test_walk(self):
        runner = r.Runner("TestRunnerWalk")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = r.Runner("TestRunnerRun")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = r.Runner("TestRunner1")
        runner2 = r.Runner("TestRunner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

# Класс тестов для Tournament
class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip_if_frozen
    def setUp(self):
        self.runner1 = rat.Runner(name="Усэйн", speed=10)
        self.runner2 = rat.Runner(name="Андрей", speed=9)
        self.runner3 = rat.Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result1 in cls.all_results.values():
            result = {}
            for key, value in result1.items():
                result[key] = str(value)
            print(result)
            # for key, value in result.items():
            #     print(f"{key}: {value}")

    @skip_if_frozen
    def test_tournament_1(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_tournament_2(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @skip_if_frozen
    def test_tournament_3(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

# Создание набора тестов и их запуск
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)