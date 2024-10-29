# tests/test_scanner.py

import unittest
from unittest.mock import patch
from src.scanner import NetworkScanner

class TestNetworkScanner(unittest.TestCase):
    
    @patch('src.scanner.socket.socket.connect_ex')
    def test_is_port_open(self, mock_connect_ex):
        """Test if is_port_open correctly identifies an open port."""
        # Arrange: Set up the mock to simulate an open port
        mock_connect_ex.return_value = 0  # Simulate open port
        scanner = NetworkScanner("127.0.0.1")

        # Act: Call is_port_open with a test port
        result = scanner.is_port_open(80)

        # Assert: Verify the result is True (indicating the port is open)
        self.assertTrue(result)

    @patch('src.scanner.socket.socket.connect_ex')
    def test_is_port_closed(self, mock_connect_ex):
        """Test if is_port_open correctly identifies a closed port."""
        # Arrange: Set up the mock to simulate a closed port
        mock_connect_ex.return_value = 1  # Simulate closed port
        scanner = NetworkScanner("127.0.0.1")

        # Act: Call is_port_open with a test port
        result = scanner.is_port_open(80)

        # Assert: Verify the result is False (indicating the port is closed)
        self.assertFalse(result)
    
    @patch('src.scanner.NetworkScanner.is_port_open')
    def test_scan_ports(self, mock_is_port_open):
        """Test scan_ports method for a range of ports."""
        # Simulate ports 80 and 443 as open
        mock_is_port_open.side_effect = lambda port: port in [80, 443]
        
        scanner = NetworkScanner("127.0.0.1")
        open_ports = scanner.scan_ports(75, 85)

        # Expect ports 80 and 443 only within the scanned range
        self.assertEqual(open_ports, [80])

if __name__ == "__main__":
    unittest.main()
