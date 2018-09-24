
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
    print(temp_card_desc)


    return cn_rec_data



