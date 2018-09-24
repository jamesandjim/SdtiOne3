
def byteinfotostr(rec_data):

    '''解析0x20查询设备状态返回的字节流，得到设备状态 参数为完整的64字节字节流'''
    cn_rec_data = {}
    # 最后一条记录的索引号
    cn_last_no = int.from_bytes(rec_data[8:12], byteorder='little')
    cn_rec_data['cn_last_no'] = cn_last_no

    # 记录类型
    no_type = rec_data[12]
    if no_type == 0:
        cn_no_type = '无记录'
    elif no_type == 1:
        cn_no_type = '刷卡记录'
    elif no_type == 2:
        cn_no_type = '门磁,按钮, 设备启动, 远程开门记录'
    elif no_type == 3:
        cn_no_type = '报警记录'
    else:
        cn_no_type = '未知记录'

    cn_rec_data['cn_no_type'] = cn_no_type

    # 开门有效性
    yn = rec_data[13]
    if yn == 1:
        cn_yn = '正常通过'
    else:
        cn_yn = '未通过'

    cn_rec_data['cn_yn'] = cn_yn

    # 门号
    door_no = rec_data[14]
    if door_no == 1:
        cn_door_no = '一号门'
    elif door_no == 2:
        cn_door_no = '二号门'
    elif door_no == 3:
        cn_door_no = '三号门'
    elif door_no == 4:
        cn_door_no = '四号门'

    cn_rec_data['cn_door_no'] = cn_door_no

    # 进门还是出门
    in_out = rec_data[15]
    if in_out == 1:
        cn_in_out = '进门'
    else:
        cn_in_out = '出门'

    cn_rec_data['cn_in_out'] = cn_in_out

    # 卡号或编号
    cn_card_no = int.from_bytes(rec_data[16:20], byteorder='little')

    cn_rec_data['cn_card_no'] = cn_card_no

    # 刷卡时间
    temp1_card_time = []
    temp_card_time = [hex(i) for i in rec_data[20:27]]
    for x in temp_card_time:
        if len(x) == 4:
            temp1_card_time.append(x.replace('0x', ''))
        else:
            temp1_card_time.append(x.replace('0x', '0'))

    cn_card_time = ''.join(temp1_card_time)

    cn_rec_data['cn_card_time'] = cn_card_time

    # 刷卡记录说明
    temp_card_desc = rec_data[27]
    if temp_card_desc == 1:
        cn_card_desc = '刷卡开门'
    elif temp_card_desc == 5:
        cn_card_desc = '刷卡禁止通过: 电脑控制'
    elif temp_card_desc == 6:
        cn_card_desc = '刷卡禁止通过: 没有权限'
    elif temp_card_desc == 7:
        cn_card_desc = '刷卡禁止通过: 密码不对'
    elif temp_card_desc == 8:
        cn_card_desc = '刷卡禁止通过: 反潜回'
    elif temp_card_desc == 9:
        cn_card_desc = '刷卡禁止通过: 多卡'
    elif temp_card_desc == 10:
        cn_card_desc = '刷卡禁止通过: 首卡'
    elif temp_card_desc == 11:
        cn_card_desc = '刷卡禁止通过: 门为常闭'
    elif temp_card_desc == 12:
        cn_card_desc = '刷卡禁止通过: 互锁'
    elif temp_card_desc == 13:
        cn_card_desc = '刷卡禁止通过: 受刷卡次数限制'
    elif temp_card_desc == 15:
        cn_card_desc = '刷卡禁止通过: 卡过期或不在有效时段'
    elif temp_card_desc == 18:
        cn_card_desc = '刷卡禁止通过: 原因不明'
    elif temp_card_desc == 20:
        cn_card_desc = '按钮开门'
    elif temp_card_desc == 23:
        cn_card_desc = '门打开[门磁信号]'
    elif temp_card_desc == 24:
        cn_card_desc = '门关闭[门磁信号]'
    elif temp_card_desc == 25:
        cn_card_desc = '超级密码开门'
    elif temp_card_desc == 28:
        cn_card_desc = '控制器上电'
    elif temp_card_desc == 29:
        cn_card_desc = '控制器复位'
    elif temp_card_desc == 31:
        cn_card_desc = '按钮不开门: 强制关门'
    elif temp_card_desc == 32:
        cn_card_desc = '按钮不开门: 门不在线'
    elif temp_card_desc == 33:
        cn_card_desc = '按钮不开门: 互锁'
    elif temp_card_desc == 34:
        cn_card_desc = '胁迫报警'
    elif temp_card_desc == 37:
        cn_card_desc = '门长时间未关报警[合法开门后]'
    elif temp_card_desc == 38:
        cn_card_desc = '强行闯入报警'
    elif temp_card_desc == 39:
        cn_card_desc = '火警'
    elif temp_card_desc == 40:
        cn_card_desc = '强制关门'
    elif temp_card_desc == 41:
        cn_card_desc = '防盗报警'
    elif temp_card_desc == 42:
        cn_card_desc = '烟雾煤气温度报警'
    elif temp_card_desc == 43:
        cn_card_desc = '紧急呼救报警'
    elif temp_card_desc == 44:
        cn_card_desc = '操作员远程开门'
    elif temp_card_desc == 45:
        cn_card_desc = '发卡器确定发出的远程开门'
    else:
        cn_card_desc = '未知'

    cn_rec_data['cn_card_desc'] = cn_card_desc

    # 门状态
    dev_sn = str(int.from_bytes(rec_data[4:8], byteorder='little'))

    cn_doorstatus1 = ''
    cn_doorstatus2 = ''
    cn_doorstatus3 = ''
    cn_doorstatus4 = ''

    if dev_sn[0] == '1':
        temp_doorstatus1 =rec_data[28]
        if temp_doorstatus1 == 1:
            cn_doorstatus1 = '一号门已打开'
        else:
            cn_doorstatus1 = '一号门已关闭'

    elif dev_sn[1] == '2':
        temp_doorstatus1 = rec_data[28]
        temp_doorstatus2 = rec_data[29]
        if temp_doorstatus1 == 1:
            cn_doorstatus1 = '一号门已打开'
        else:
            cn_doorstatus1 = '一号门已关闭'

        if temp_doorstatus2 == 1:
            cn_doorstatus2 = '二号门已打开'
        else:
            cn_doorstatus2 = '二号门已关闭'

    elif dev_sn[4] == '4':
        temp_doorstatus1 = rec_data[28]
        temp_doorstatus2 = rec_data[29]
        temp_doorstatus3 = rec_data[30]
        temp_doorstatus4 = rec_data[31]
        if temp_doorstatus1 == 1:
            cn_doorstatus1 = '一号门已打开'
        else:
            cn_doorstatus1 = '一号门已关闭'

        if temp_doorstatus2 == 1:
            cn_doorstatus2 = '二号门已打开'
        else:
            cn_doorstatus2 = '二号门已关闭'

        if temp_doorstatus3 == 1:
            cn_doorstatus3 = '一号门已打开'
        else:
            cn_doorstatus3 = '一号门已关闭'

        if temp_doorstatus4 == 1:
            cn_doorstatus4 = '二号门已打开'
        else:
            cn_doorstatus4 = '二号门已关闭'

    cn_rec_data['cn_doorstatus1'] = cn_doorstatus1
    cn_rec_data['cn_doorstatus2'] = cn_doorstatus2
    cn_rec_data['cn_doorstatus3'] = cn_doorstatus3
    cn_rec_data['cn_doorstatus4'] = cn_doorstatus4

    return cn_rec_data

    # 按钮状态



