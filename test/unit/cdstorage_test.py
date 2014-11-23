import unittest
from cdrent import CD
from cdstorage import CDStorage

class CDStorageTest(unittest.TestCase):
    def test_storage_is_initially_empty(self):
        cdstorage = CDStorage()
        self.assertEqual({}, cdstorage.cds)
        self.assertEqual(len(cdstorage.cds), 0)

    def test_add_cd_to_storage(self):
        cdstorage = CDStorage()
        cd1 = CD(001, "XOXO", "Available")
        cd2 = CD(002, "2014 S/S", "Available")

        cdstorage.add_cd(cd1)
        cdstorage.add_cd(cd2)
        self.assertEqual(len(cdstorage.cds), 2)

    def test_get_cd_info(self):
        cdstorage = CDStorage()
        cd1 = CD(001, "XOXO", "Available")
        cdstorage.add_cd(cd1)
        self.assertEqual(cdstorage.get_cd_info(001), cd1)

if __name__ == '__main__':
    unittest.main()
