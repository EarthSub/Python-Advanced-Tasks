# Load the provided skeleton in the IDE you use. Add new project Tests.

# class Worker:
#     def __init__(self, name, salary, energy):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0

#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')

#         self.money += self.salary
#         self.energy -= 1

#     def rest(self):
#         self.energy += 1

#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'

# Create a class WorkerTests

# * In Judge, you must submit just the WorkerTests class, with the unittest module imported and the main block.
#     Create the following tests:

#     · Test if the worker is initialized with the correct name, salary, and energy
#     · Test if the worker's energy is incremented after the rest method is called
#     · Test if an error is raised if the worker tries to work with negative energy or equal to 0
#     · Test if the worker's money is increased by his salary correctly after the work method is called
#     · Test if the worker's energy is decreased after the work method is called
#     · Test if the get_info method returns the proper string with the correct values



class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



from unittest import TestCase, main


class TestWorker(TestCase):
    def test_worker_init(self):
        # Arrange and Act
        worker = Worker("Test", 100, 10)

        # Assert
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_has_no_energy_work_raises(self):
        # Arrange
        worker = Worker("Test", 100, 0)

        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()

        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(worker.money, 0)
        self.assertEqual(worker.money, 0)


        # test with negative energy
        worker.energy = -1

        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()

        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, worker.money)
        self.assertEqual(-1, worker.energy)

    def test_worker_works(self):
        worker = Worker("Test", 100, 2)

        self.assertEqual(0, worker.money)
        self.assertEqual(2, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(100, worker.money)
        self.assertEqual(1, worker.energy)

        worker.work()
        self.assertEqual(200, worker.money)
        self.assertEqual(0, worker.energy)


    def test_worker_rest_increase_energy(self):
        worker = Worker("Test", 100, 0)

        # Arrange
        self.assertEqual(0, worker.energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(1, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker("Test", 100, 0)

        # Act
        result = worker.get_info()

        # Assert
        self.assertEqual(f"Test has saved 0 money.", result)


if __name__ == "__main__":
    main()
