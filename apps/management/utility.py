from .models import Menu


class Menu_operator:
    '''
    用于菜单的操作，从数据库转化列表。列表有顺序。列表中的元素用字典表示
    '''
    @staticmethod
    def toList():
        list_menus = []
        top_menu = Menu.objects.filter(parentmenu='0').order_by('seq')

        for m1 in top_menu:
            m1_name = m1.name
            m1_name = m1_name.strip()
            m2_menus = {}
            sec_menu = Menu.objects.filter(parentmenu=m1_name).order_by('seq')

            for m2 in sec_menu:
                m3_menus = {}
                m2_name = m2.name
                m2_name = m2_name.strip()
                m2_submenu = m2.submenu

                # 如果submenu为‘0’，表示无下级菜单
                if m2_submenu.strip() == '0':
                    m2_one = {m2_name: {'icon': m2.icon, 'url': m2.url}}
                    m2_menus.update(m2_one)

                #如果submenu为‘1’，表示有下级菜单，继续循环
                elif m2_submenu.strip() == '1':
                    third_menu = Menu.objects.filter(parentmenu=m2_name).order_by('seq')
                    for m3 in third_menu:
                        m3_one = {m3.name: {'icon': m3.icon, 'url': m3.url}}
                        m3_menus.update(m3_one)

                    m2_one = {m2_name: {'icon': m2.icon, 'value': m3_menus}}
                    m2_menus.update(m2_one)

            m1_one = {m1_name: {'icon': m1.icon, 'value': m2_menus}}

            list_menus.append(m1_one)

        #print(list_menus)
        return list_menus


