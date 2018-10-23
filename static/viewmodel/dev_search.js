$(function () {
    $("button#add").click(function(){
		// 遍历所有的table数据
		var html= new Array();
		var title= new Array();
		title[0]="sn";
        title[1]="ip";
        title[2]="netmask";
        title[3]="netgate";
        title[4]="mac";



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

	});


})