
"""
    Write Python function with 3 arguments [ip] [start_port] [end_port]
    Using socket library try to scan specific host with range of ports .
    write a report with screens for your output scanning port 21 and 22
    Magdy Yasser Mahmoud Khalil (220100403)
"""

import socket

# afunction that takes ip , start port , and last port
def ports( ip,  firstPort, lastPort ):

    #check if the start ip is grater than last ip if true stops the recursion
    if firstPort>lastPort:
        return 

    #creating a instance of the Socket class where AF_inet is ipv4 and SOCK_STREAM is TCP connection
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    if sock.connect_ex( (ip, firstPort)) == 0:
        print(f"The port {firstPort} is open")

    else:
        print(f"The port {firstPort} is closed")

    #recursion 
    ports( ip, firstPort+1, lastPort )

ports('192.168.1.1', 21, 80) #Router's ip which has two ports opened in range 21 to 80 which are 53 DNS and 80 HTTP

