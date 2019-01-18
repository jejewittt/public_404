#!/usr/bin/env python3



# https://github.com/awwong1/cmput404lab2h05

import socket 
from multiprocessing  import Pool

# can do socket.create connection 
# will want the ip adress info of google.com
# get addr info

# echo "Foobar" | nc localhost 8001 -q 1

# make sure to end with 2 newlines


HOST = "localhost"
PORT = 80 

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

BUFFER_SIZE = 1024






def get_request(addr):
    (family, socktype, proto, cannoame, sockaddr) = addr
    try:
        s = socket.socket(family,socktype,proto) #good to put into try accept
        s.connect(sockaddr)
        s.sendall(payload.encode())  #need to put in byte format

        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data: break
            full_data+= data
        print(full_data)
        # print(s)



    except Exception as e:
        print(e)
    finally:
        s.close()




def main():
    addr_info = socket.getaddrinfo(HOST, PORT)

    for addr in addr_info:
        (family, socktype, proto, canonname, sockaddr) = addr
        # print(addr_info)
        if family  == socket.AF_INET and socktype == socket.SOCK_STREAM:
            # print(sockaddr)
            # get_request(addr)
            with Pool() as p:
                p.map(get_request, [addr] * 10)




if __name__ == "__main__":
    main()
