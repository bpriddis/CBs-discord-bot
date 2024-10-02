# tests/test_data_processor.py
import unittest
from unittest.mock import Mock
from data_processor import process_message_data

class TestDataProcessor(unittest.TestCase):
    def test_process_message_data(self):
        mock_message = Mock()
        mock_message.content = "Win vs XLDS (bravo)"
        mock_message.id = 123456789

        ocr_data = {
            "map": "Trap",
            "clan_tag": "ABC",
            "clan_name": "AlphaBravo",
            "timestamp": "01.10.24 10:30"
        }

        result = process_message_data(mock_message, ocr_data)

        self.assertEqual(result["Result"], "Win")
        self.assertEqual(result["Enemy"], "XLDS")
        self.assertEqual(result["Rating"], "bravo")
        self.assertEqual(result["Map"], "Trap")
        self.assertEqual(result["Clan Tag"], "ABC")
        self.assertEqual(result["Clan Name"], "AlphaBravo")
        self.assertEqual(result["Message ID"], "123456789")
        self.assertEqual(result["Timestamp"], "10/01/24 10:30")

if __name__ == '__main__':
    unittest.main()