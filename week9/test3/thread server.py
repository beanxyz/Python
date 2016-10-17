#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import socketserver


class mysocketserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes("Welcome to the Test system.", encoding='utf-8'))

        while True:
            try:
                data = conn.recv(1024)
                if len(data) == 0: break
                print("[%s] sends %s" % (self.client_address, data.decode()))
                conn.sendall(data.upper())
            except Exception:
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), mysocketserver)
    server.serve_forever()
