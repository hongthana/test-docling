import unittest
import os
from unittest.mock import Mock, patch
from test_docling.app import extract_info

class TestApp(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        # Create output directory if it doesn't exist
        os.makedirs("output", exist_ok=True)
        
        # Mock file object
        self.mock_file = Mock()
        self.mock_file.name = "test_document.pdf"

    def tearDown(self):
        """Clean up after each test"""
        # Remove test output file if it exists
        test_output = os.path.join("output", "test_document.md")
        if os.path.exists(test_output):
            os.remove(test_output)

    @patch('test_docling.app.convert_document')
    def test_extract_info_success(self, mock_convert):
        """Test successful document conversion"""
        # Mock the convert_document function to return a sample result
        mock_convert.return_value = "Sample converted content"

        # Call the function
        time_spent, result = extract_info(self.mock_file)

        # Assertions
        self.assertTrue(isinstance(time_spent, str))
        self.assertTrue("Time spent:" in time_spent)
        self.assertEqual(result, "Sample converted content")
        self.assertTrue(os.path.exists(os.path.join("output", "test_document.md")))
        mock_convert.assert_called_once_with(self.mock_file.name)

    @patch('test_docling.app.convert_document')
    def test_extract_info_empty_content(self, mock_convert):
        """Test conversion with empty content"""
        mock_convert.return_value = ""

        time_spent, result = extract_info(self.mock_file)

        self.assertTrue(isinstance(time_spent, str))
        self.assertEqual(result, "")

    @patch('test_docling.app.convert_document')
    def test_extract_info_timing(self, mock_convert):
        """Test that timing information is returned correctly"""
        mock_convert.return_value = "Test content"

        time_spent, _ = extract_info(self.mock_file)

        self.assertTrue(isinstance(time_spent, str))
        self.assertTrue("Time spent:" in time_spent)

if __name__ == "__main__":
    unittest.main()
