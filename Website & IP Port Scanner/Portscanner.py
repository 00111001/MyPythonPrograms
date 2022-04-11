# -----------------------------------------------
# Author: Nick V.
# Website & IP Portscanner Multi threaded
# Version: 1.0
# creation date: 27.03.2022
# -----------------------------------------------

# For colouring Fonts when Port is closed or open
import colorama
from colorama import Fore
# Multithreading
import concurrent.futures
import threading
# For checking validation of ip addresses
import ipaddress
# To do arithmetic Operations with Time
from datetime import datetime
# For working with operating system features (path)
import os
# For Communication outside
import socket
from http.client import HTTPConnection
from urllib.parse import urlparse

# This script uses the socket api to see if you can connect to a port on the target ip address.
# Once you have successfully connected a port is seen as open.

# calling init() will filter ANSI escape sequences out of any text sent and replace them with equivalent Win32 calls
colorama.init()
# Locking the current Port and print him down below
print_lock = threading.Lock()

# Printing some Information
print(Fore.LIGHTWHITE_EX + "****************************************************************")
print("* Copyright of Nick V. 2022                                    *")
print("* Use on your Own Risk!                                        *")
print("* Only for testing. Do not try to damage other!                *")
print("****************************************************************")

def main_menu():
    while True:
        print("""(1) Scanning Website
(2) Scanning IP Address
(0) Exit""")  # Printing the Menu

        choice = input("Which function you wanna use?: ")  # Main Menu Choice Input for accessing functions in Menus

        if choice == "1":
            scan_website()  # Menu for converting sentences in List or smth else
        elif choice == "2":
            scan_ipaddress()  # Menu for counting Lists,Letters or words
        elif choice == "0":
            break

#  Creating a function with the Parameters target and Port
#  Delivers opened Port in the Input field
def scan(target, port):
    #  Referencing a new socket using the given address family, socket type and protocol number.
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #  Setting Scanner timeout to 1 Second
    scanner.settimeout(1)
    try:
        # Try to connect using the target input and using the referenced Var.
        scanner.connect((target, port))
        # Close the Connection
        scanner.close()
        # Print the opened Port.
        with print_lock:
            print(Fore.LIGHTWHITE_EX + f"[{port}]" + Fore.GREEN + " Opened")
    except:
        # If we were interested in the closed ports we'd put something her
        pass

def scan_website():
    # Return True if the target URL is online.
    def site_is_online(target, timeout=2):
        # Referencing Exception to var
        error = Exception("unknown error")
        # The URL parsing functions focus on splitting a URL string into its components
        parser = urlparse(target)
        host = parser.netloc or parser.path.split("/")[0]
        # Loop checking 2 Ports
        for port in (80, 443):
            # Referencing connection to use it
            connection = HTTPConnection(host=host, port=port, timeout=timeout)
            try:
                # Do the request
                connection.request("HEAD", "/")
                # if online return true
                return True
            # If not able to open the connection
            except Exception as e:
                error = e
            finally:
                # Close the connection
                connection.close()
        # Raise an exception otherwise.
        raise error

    target = input("Insert Website you want to scan: ")
    # Here's the Input for the Minimum Port
    port_min = int(input("Insert the Port you want start to scan: "))
    # Here's the Input for the Maximum Port
    port_max = int(input("Insert the Port until you want to scan: "))
    # Reference to do arithmetic Operations with time
    scan_start = datetime.now()
    try:
        if site_is_online(target):
            print("Ip address valid")
            # returns the IP address of the host and reference it to var
            ip = socket.gethostbyname(target)
            # Checking after validation responsibility and send a ping
            response = os.system("ping -n 1" + ip)
            # if website responded what corresponds 0 then:
            if response == 0:
                # Open with more Threads
                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    # Loop for looping through the Ports using range function
                    for port in range(port_min, port_max):
                        # Schedules the callable Scan function  to be executed
                        executor.submit(scan, target, port + 1)
                # Referencing Time which scan has ended
                scan_end = datetime.now()
                # Do Arithmetic Operations to get the difference between the Scan_end and scan_start
                diff = scan_end - scan_start
                # Printing the Scan duration
                print(Fore.LIGHTWHITE_EX + "Scan finished within: " + Fore.GREEN + str(diff))
            else:
                # Error Msg if URL is valid aber ping didnt go right
                print("Valid Url but no Connection. Check your URL!")
        else:
            # Error if Website was not valid
            print("Not a valid URL")
    except socket.gaierror:
        print(Fore.RED + "IP address is not a valid " + Fore.LIGHTWHITE_EX)



# Calling main and therefor the Program
if __name__ == '__main__':
    main_menu()
