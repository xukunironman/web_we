var yea=2016,mon=9,day=4,hou=14,min=50,sec=0,mil=0;
var initTimeFlag=0;

function initHome(){
	initTitleClock();
}

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
				datatime=data["value"];
				yea=datatime["yea"];mon=datatime["mon"];day=datatime["day"];
				hou=datatime["hou"];min=datatime["min"];sec=datatime["sec"];	
				initTimeFlag=1;
			}		
		}	
	});
}
function initTimer()
{
	var str="";

	var timer=document.getElementById("timer");
	timer.innerHTML=str;
	
}
window.onload=initHome