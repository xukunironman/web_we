function onSideTabClick(event,id)
{
	var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("sidetabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("sidetablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(id).style.display = "block";
    event.currentTarget.className += " active";
	
}
function CreatTab(ulid,text)
{
	ul=document.getElementById(ulid);
	var li=document.createElement("li");
	var a = document.createElement("a");
	a.href = "#";
	a.innerHTML = text;
	a.setAttribute("class","sidetablink");
	a.setAttribute("onclick","onSideTabClick(event,'"+text+"')");
	
	li.appendChild(a);
	ul.appendChild(li);
	
}
function CreatMyImg(parid,cla,imgurl,alt,des){
	
	var div=document.createElement("div");
	div.setAttribute("class",cla);
	
	var a = document.createElement("a");
	a.setAttribute("target","_blank");
	a.setAttribute("href",imgurl);
	
	var img=document.createElement("img");
	img.setAttribute("src",imgurl);
	img.setAttribute("alt",alt);
	
	var desdiv=document.createElement("div");
	desdiv.setAttribute("class","desc");
	desdiv.innerHTML=des;
	
	a.appendChild(img);
	div.appendChild(a);
	div.appendChild(desdiv);
	
	document.getElementById(parid).appendChild(div);
}
function CreatTabConFram(parid,id,cla){
	
	var div=document.createElement("div");
	div.setAttribute("id",id);
	div.setAttribute("class",cla);
	document.getElementById(parid).appendChild(div);
}
function InsertImgToCon(parid,imgurl,alt,des){
	CreatMyImg(parid,"img",imgurl,alt,des);
}
function CreatTab_Con(year){
	CreatTab("sidetab",year);
	CreatTabConFram("album",year,"sidetabcontent");
}