import socket
from concurrent.futures import ThreadPoolExecutor

class NetworkScanner:
    def __init__(self, target):
        """Initialize with a target IP or hostname."""
        self.target = target
    
    def is_port_open(self, port):
        """Check if a specific port is open on the target."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # 1-second timeout for faster scans
            result = sock.connect_ex((self.target, port))
            return result == 0
        
    def scan_ports(self, start_port, end_port):
        """Scan a range of ports and return a list of open ports."""
        open_ports = []
        
        def check_port(port):
            if self.is_port_open(port):
                open_ports.append(port)

        '''for port in range(start_port, end_port + 1):
            if self.is_port_open(port):
                open_ports.append(port)'''
        
        # Use ThreadPoolExecutor for concurrent scanning
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(check_port, range(start_port, end_port + 1))
        
        return open_ports