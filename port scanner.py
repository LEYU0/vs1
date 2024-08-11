import socket
import sys

def port_scan(target_host, start_port, end_port):
    
    """Scans a range of ports on the target host and prints the open ports.
    
    Args:
        target_host (str): The IP address or hostname of the target host.
        start_port (int): The starting port number to scan.
        end_port (int): The ending port number to scan.
    """
    try:
        for port in range(start_port, end_port+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #target host must be IPv4 family and must include TCP protocol
            s.settimeout(0.1)  # Adjust the timeout value as needed
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()
    except socket.gaierror: #if there is problem withe host
        print(f"Hostname could not be resolved: {target_host}")
        sys.exit()
    except socket.error:  # if there is problem with network connection
        print(f"Couldn't connect to server: {target_host}")
        sys.exit()

  #used to separate executable code from importable code 
if __name__ == "__main__":
    target_host = input("Enter the target host (IP or hostname): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    port_scan(target_host, start_port, end_port)
