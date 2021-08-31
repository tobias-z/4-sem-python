from modules.week2.file_management import (
    print_file_content,
    write_list_to_file,
    read_csv,
    FILE_NAME,
)
import unittest


class Test(unittest.TestCase):
    def test_print_file_content(self):
        self.assertEqual(None, print_file_content(FILE_NAME))

    def test_read_csv(self):
        rows = read_csv(FILE_NAME)
        self.assertTrue(type(rows) == list)

    def test_write_list_to_file(self):
        write_list_to_file(FILE_NAME, "test", "one", "two", "tree")
        self.assertEqual(read_csv(FILE_NAME)[0], "test\n")
