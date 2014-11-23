import unittest
from cdrent import CD
from cdstorage import CDStorage

class CDStorageTest(unittest.TestCase):
    def test_storage_is_initially_empty(self):
        cdstorage = CDStorage()
        self.assertEqual({}, cdstorage.cds)
        self.assertEqual(len(cdstorage.cds), 0)
