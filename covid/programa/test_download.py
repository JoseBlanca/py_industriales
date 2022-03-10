import unittest

from download import get_and_store_isciii_data


class DownloadTest(unittest.TestCase):
    def test_download(self):
        isciii_csv_path = get_and_store_isciii_data()
        assert str(isciii_csv_path).endswith(".csv")


if __name__ == "__main__":
    unittest.main()
