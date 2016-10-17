function initHome(){
	initTitleClock();
}
var yea=2016,mon=9,day=4,hou=14,min=50,sec=0,mil=0;

function getData(){
	$.Ajax({
		type:"GET",
		data:{"request":"datatime"},
		cache:false,
		url:"/request",
		dataType:"json",
		success:function(data){
			if (data["status"]=="OK")
			{
				
				
			}
			
		}
		
	})
	
}

window.onload=initHome