$(function () {
    $("button#add").click(function(){
		// 遍历所有的table数据
		var html= new Array();
		$('table#t1').find('tbody').each(function () {

            $(this).find('tr').each(function () {

            	$(this).find('td').filter("[class !='td-manage']").each(function () {
            		html.push($(this).text());
            	});


            });


            return false;
        });
       alert(html);
	});


})