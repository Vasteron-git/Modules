import logging
import unittest
import rt_with_exceptions as r  # Импортируем класс Runner

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    filename='runner_tests.log',
                    filemode='w',
                    encoding='utf-8',
                    format='%(levelname)s: %(message)s')

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = r.Runner("Спортсмен", -10)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner")
            self.assertEqual(str(e), "Скорость не может быть отрицательной, сейчас -10")

    def test_run(self):
        try:
            runner = r.Runner(1234, 10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner")
            self.assertEqual(str(e), "Имя может быть только строкой, передано int")

    def test_challenge(self):
        runner1 = r.Runner("TestRunner1")
        runner2 = r.Runner("TestRunner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)



if __name__ == '__main__':
    unittest.main()