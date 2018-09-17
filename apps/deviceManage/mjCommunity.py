#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-05-28 15:11
# @Author  : James
# @Site    :
# @File    : mj_communication.py
# @Software: PyCharm

from socket import *
import struct
import binascii

#数据报及其操作方法
#4、接收服务器发送回的数据包
#5、对接收到的数据包进行解析


#定义短报文包的类
class WGPaketShort:
    '短报文类，实现发送短报文和收到返回短报文的功能'

    # 定义全局类变量
    Type = 0x17
    ControllerPort = 60000
    SpecialFlag = 0x55AAAA55
    WGPacketSize = 64

    def __init__(self, ip, dev_sn, func_id):
        #self.udp_data = [0 for i in range(WGPaketShort.WGPacketSize)]
        self.udp_data = bytearray(WGPaketShort.WGPacketSize)
        self.udp_data[0] = WGPaketShort.Type
        self.udp_data[1] = func_id
        self.udp_data[4:8] = dev_sn.to_bytes(4, byteorder='little')
        self.ip = ip
        self.rec_data = None

    #发送短报文功能
    def send_data(self):
        #s1 = bytearray(32)
        #s2 = bytearray(20)
        #values = (WGPaketShort.Type, self.func_ID, 0, self.dev_sn, s1, 0, s2)
        #s = struct.Struct('<BBHI32sI20s')
        #packed_data = s.pack(*values)
        #unpacked_data = s.unpack(packed_data)
        #print(s.size)
        #print(packed_data)

        udp_cli_socket = socket(AF_INET, SOCK_DGRAM)

        # 定义UDP数据包

        ip = '192.168.0.99'
        ADDR = (self.ip, WGPaketShort.ControllerPort)

        try:
            udp_cli_socket.sendto(self.udp_data, ADDR)
            self.rec_data, ADDR = udp_cli_socket.recvfrom(WGPaketShort.WGPacketSize)
            #rec = s.unpack(rec_data)
            print(self.rec_data[4:8])
            b = self.rec_data[4:8]
            i = int.from_bytes(b, byteorder = 'little')
            print(i)
            print(self.rec_data[0])
            print(self.rec_data)
            if len(self.rec_data) == WGPaketShort.WGPacketSize:
                if self.rec_data[0] == self.udp_data[0] and self.rec_data[1] == self.udp_data[1]:
                    x = self.rec_data
                    return x
                else:
                    x = 't'
                    return x
            else:
                x = 'no'
                return x

        except error:
            print(error.message)

        udp_cli_socket.close()

    #接收短报文功能
    def receive_data(self):
        pass













