$(function () {
    $("button#add").click(function () {
        // 遍历所有的table数据
        var html = new Array();
        var title = new Array();
        title[0] = "sn";
        title[1] = "ip";
        title[2] = "netmask";
        title[3] = "netgate";
        title[4] = "mac";

        $('table#t1').find('tbody').each(function () {

            $(this).find('tr').each(function () {

                $(this).find('td').filter("[class !='td-manage']").filter("[id != 'one']").each(function () {
                    html.push($(this).text());
                });

            });
            return false;
        });
        alert(html[0]);
        alert(html[1]);
        alert(html[2]);

        //做ajax请求
        $.ajax({

                type: 'POST',
                url: '/dev/deviceset/',
                dataType: 'json',
                data: {'html': html},
                success: function (data_get) {
                    window.location.href = '/dev/list/'
                    alert('ok')
                },

            }
        )

    });


    $("table tr").dblclick(function () {//为表格的行添加点击事件
        var dic = new Array();
        var tr = $(this);//找到tr原色
        var td = tr.find("td");//找到td元素
        dic['sn'] = td[0].innerHTML;
        dic['ip'] = td[1].innerHTML;
        dic['netmask'] = td[2].innerHTML;
        dic['netgate'] = td[3].innerHTML;
        dic['mac'] = td[4].innerHTML;
        alert(dic.sn);//指定下标即可
        $.ajax({

                type: 'POST',
                url: '/dev/deviceset/',
                dataType: 'json',
                data: {'dev':dic},
                success: function (data_get) {
                    window.location.href = '/dev/list/'
                    alert('ok')
                },

            }
        );

    });


})