from modules.week2.utils import (
    get_all_file_names,
    get_file_names,
    print_line_one,
    print_emails,
    write_headlines,
)
import unittest


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.folders = "modules/week2/folders"
        self.output = "files/output.csv"
        self.file_names = [
            "files/output.csv",
            "files/outputtwo.csv",
            "files/emails.csv",
        ]

    def test_get_file_names(self):
        self.assertIsNone(get_file_names(self.folders, self.output))

    def test_get_all_file_names(self):
        self.assertIsNone(get_all_file_names(self.folders, self.output))

    def test_print_line_one(self):
        self.assertIsNone(print_line_one(self.file_names))

    def test_print_emails(self):
        self.assertIsNone(print_emails(self.file_names))

    def test_write_headlines(self):
        self.assertIsNone(write_headlines(["files/some_markdown.md", "files/users.md"]))
