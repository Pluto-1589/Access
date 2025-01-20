from unittest import TestCase
import task_2 as script


class MyTestSuite(TestCase):

    def test_add_stock(self):
        warehouse = {"Phone": 12}
        script.add_stock(warehouse, "Phone")
        self.assertEqual(warehouse["Phone"], 13)

    def test_remove_stock(self):
        warehouse = {"Guitar": 5}
        script.remove_stock(warehouse, "Guitar")
        self.assertEqual(warehouse["Guitar"], 4)

    def test_get_stock(self):
        warehouse = {"Baby Oil": 100000}
        script.get_stock(warehouse, "Baby Oil")
        self.assertEqual(warehouse["Baby Oil"], 100000)
