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
    #data = [0 for i in range(WGPacketSize)]

    def __init__(self, ip, dev_sn, func_ID, door_id = 0):
        self.ip = ip
        self.dev_sn = dev_sn
        self.func_ID = func_ID
        self.door_id = door_id

    #发送短报文功能
    def send_data(self):
        #values = (WGPaketShort.Type, self.func_ID, 0, self.dev_sn, self.door_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        #s = struct.Struct('<BBHIIIIIIIIIIIIIII')
        s1 = bytearray(32)
        s2 = bytearray(20)
        values = (WGPaketShort.Type, self.func_ID, 0, self.dev_sn, s1, 0, s2)
        s = struct.Struct('<BBHI32sI20s')
        packed_data = s.pack(*values)
        #unpacked_data = s.unpack(packed_data)
        print(s.size)
        print(packed_data)


        udp_cli_socket = socket(AF_INET, SOCK_DGRAM)

        # 定义UDP数据包

        ip = '192.168.0.99'
        ADDR = (ip, WGPaketShort.ControllerPort)

        try:
            udp_cli_socket.sendto(packed_data, ADDR)
            rec_data, ADDR = udp_cli_socket.recvfrom(WGPaketShort.WGPacketSize)
            rec = s.unpack(rec_data)
            print(rec_data)
            if len(rec_data) == WGPaketShort.WGPacketSize:
                if rec[0] == values[0] and rec[1] == values[1]:
                    x = rec_data
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













