function initPhoto(){
	initTitleClock();
	CreatTab_Con("2016");
	InsertImgToCon("2016","image/2014-8-taishan.jpg","this is a image","Love");
	CreatTab_Con("2015");
	InsertImgToCon("2015","image/test2.jpg","this is a image","good");
	InsertImgToCon("2015","image/2014-8-taishan.jpg","this is a image","Love You");
/*	
	$(".titletext").innerHTML="abc";
	$.get("104.223.16.55/photo",function(data,status)
	{
		alert("Data: " + data + "\nStatus: " + status);
	});	
	CreatTab_Con("2015");
	InsertImgToCon("2015","image/test2.jpg","this is a image","good");
	InsertImgToCon("2015","image/2014-8-taishan.jpg","this is a image","Love You");
	
	CreatTab_Con("2014");
	InsertImgToCon("2014","image/test2.jpg","this is a image","good");
	*/
}

window.onload=initPhoto