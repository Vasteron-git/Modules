import unittest
import runner_and_tournament as rat


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

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

    def test_tournament_1(self):
        tournament = rat.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_2(self):
        tournament = rat.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_tournament_3(self):
        tournament = rat.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()