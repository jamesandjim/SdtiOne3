from deviceManage.mjCommunity import WGPaketShort
from deviceManage.devicestatustostr import byteinfotostr


# 搜索控制器
def search_dev():
    dev = WGPaketShort('255.255.255.255', 0, 0x94)
    ret = dev.send_data()
    if ret is True:
        # 从返回值取得设备的SN,并以低位在前的方式，将字节码转为int
        dev_sn = dev.rec_data[4:8]
        rt_dev_sn = int.from_bytes(dev_sn, byteorder='little')

        # 从返回的字节中分别取出IP的四个段并生成列表.进行组合，形成IP字符串
        tm_ip = dev.rec_data[8:12]
        list_ip = [str(tm_ip[i]) for i in range(4)]
        rt_dev_ip = '.'.join(list_ip)

        # 从返回的字节中分别取出掩码的四个段并生成列表.进行组合，形成掩码字符串
        dev_netmask = dev.rec_data[12:16]
        list_netmask = [str(dev_netmask[i]) for i in range(4)]
        rt_dev_netmask = '.'.join(list_netmask)

        # 从返回的字节中分别取出网关的四个段并生成列表.进行组合，形成网关字符串
        dev_netgate = dev.rec_data[16:20]
        list_netgate = [str(dev_netgate[i]) for i in range(4)]
        rt_dev_netgate = '.'.join(list_netgate)

        # 从返回的字节中分别取出MAC的6个段并生成列表.进行组合，形成MAC字符串
        dev_mac = dev.rec_data[20:26]
        list_mac = [str(hex(dev_mac[i])) for i in range(6)]
        rt_dev_mac = ':'.join(list_mac)

        dev_ver = dev.rec_data[26:28]
        list_ver = [str(dev_ver[i]) for i in range(2)]
        rt_dev_ver = '.'.join(list_ver)


        # rt_dev_ver = dev_ver-(dev_ver/16)*6
        # 从返回的字节中分别取出时间的四个段并生成列表.进行组合，形成时间字符串
        dev_date = dev.rec_data[28:32]
        list_date = [str(dev_date[i]) for i in range(4)]
        rt_dev_date = '-'.join(list_date)

        one = dict(rt_dev_sn=rt_dev_sn, rt_dev_ip=rt_dev_ip, rt_dev_netmask=rt_dev_netmask, rt_dev_netgate=rt_dev_netgate, rt_dev_mac=rt_dev_mac, rt_dev_ver=rt_dev_ver, rt_dev_date=rt_dev_date)

        return one


# 设置设备IP地址
def set_ip(ip, sn, netmask, netgate):
    dev = WGPaketShort('255.255.255.255', sn, 0x96)

    list_ip = ip.split('.')
    bytelist_ip = [int(list_ip[i]) for i in range(4)]
    dev.udp_data[8:12] = bytelist_ip

    list_netmask = netmask.split('.')
    bytelist_netmask = [int(list_netmask[i]) for i in range(4)]
    dev.udp_data[12:16] = bytelist_netmask

    list_netgate = netgate.split('.')
    bytelist_netgate = [int(list_netgate[i]) for i in range(4)]
    dev.udp_data[16:20] = bytelist_netgate

    dev.udp_data[20] = 0x55
    dev.udp_data[21] = 0xAA
    dev.udp_data[22] = 0xAA
    dev.udp_data[23] = 0x55

    dev.send_data()

    return True


# 查询控制器状态
def show_dev_info(ip, sn):
    dev = WGPaketShort(ip, int(sn), 0x20)
    ret = dev.send_data()

    if ret is True and dev.udp_data[4:8] == dev.rec_data[4:8]:
        rt_data = dev.rec_data

        cn_data = byteinfotostr(rt_data)

        return cn_data


# 远程开门
def open_door(ip, sn, doorno):
    dev = WGPaketShort(ip, sn, 0x40)
    dev.udp_data[8] = int(doorno)
    ret = dev.send_data()

    print(dev.rec_data[1])

    if ret is True and dev.udp_data[4:9] == dev.rec_data[4:9]:
        cn_opendoor_ok = '开门成功'

        return {'cn_opendoor_ok':cn_opendoor_ok}

# 读取控制器时间
def get_device_time(ip, sn):
    pass


# 设置控制器时间
def set_device_time(ip, sn):
    pass


# 获取指定索引号的记录[功能号: 0xB0]
def get_record(ip, sn, recordno):
    pass


# 设置已读取过的记录索引号[功能号: 0xB2]
def set_no_readed(ip, sn, recordno):
    pass


# 获取已读取过的记录索引号[功能号: 0xB4]
def get_no_readed(ip, sn):
    pass


# 权限添加或修改[功能号: 0x50]
def add_auth(ip, sn):
    pass


# 权限删除(单个删除)[功能号: 0x52]
def del_auth(ip, sn):
    pass


# 权限清空(全部清掉)[功能号: 0x54]
def del_all_auth(ip, sn):
    pass


# 权限总数读取[功能号: 0x58]
def get_total_auth(ip, sn):
    pass


# 权限查询[功能号: 0x5A]
def get_auth(ip, sn):
    pass


# 获取指定索引号的权限[功能号: 0x5C]
def get_auth_no(ip, sn):
    pass


# 设置门控制参数(在线/延时) [功能号: 0x80]
def set_door_option(ip, sn):
    pass


# 读取门控制参数(在线/延时) [功能号: 0x82]
def get_door_option(ip, sn):
    pass


# 设置接收服务器的IP和端口 [功能号: 0x90]
def set_server_option(ip, sn):
    pass


# 读取接收服务器的IP和端口 [功能号: 0x92]
def get_server_option(ip, sn):
    pass


# 权限按从小到大顺序添加[功能号: 0x56] 适用于权限数过1000
def add_all_auth(ip, sn):
    pass



