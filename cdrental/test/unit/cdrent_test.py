import unittest
from cdrent import CD


class TestCD(unittest.TestCase):
    def test_cd_object_can_be_created(self):
        cd = CD("CD1","XOXO","Available")
        self.assertEqual(cd.cd_id, "CD1")
        self.assertEqual(cd.cd_name, "XOXO")
        self.assertEqual(cd.cd_status, "Available")

if __name__ == '__main__':
    unittest.main()
