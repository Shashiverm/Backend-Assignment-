from django.test import TestCase
from .utils import process_excel_data
from django.core.files.uploadedfile import SimpleUploadedFile

class IngestionTests(TestCase):
    def setUp(self):
        self.excel_file = SimpleUploadedFile(
            "test_data.xlsx",
            b"Excel file content",
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    def test_process_excel_data(self):
        result = process_excel_data(self.excel_file)
        self.assertIsInstance(result, dict)
        self.assertIn('customers', result)
        self.assertIn('loans', result)

    def test_invalid_excel_file(self):
        invalid_file = SimpleUploadedFile(
            "invalid_data.txt",
            b"Not an Excel file",
            content_type="text/plain"
        )
        with self.assertRaises(ValueError):
            process_excel_data(invalid_file)