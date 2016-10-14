function displaytime(){
                var elt=document.getElementById("clock");
                var now = new Date();
                elt.innerHTML= now.toLocaleString();
                setTimeout(displaytime,500);
				
				
}
function initTitleClock(){
	
	displaytime();
}
