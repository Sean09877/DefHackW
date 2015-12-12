var forum=new Firebase ("https://donald-trump.firebaseio.com/"); 
document.getElementById("submit").onclick=function(){
	var username=$("#username").val();
	var message=$("#your_message").val();
	console.log('LOL');
	forum.push({name:username,message:message});
	$("#your_message").val("");
	return false;
};
var messages=[]
forum.on("child_added", function (snapshot) {
	var value=snapshot.val()
	var count=20
	messages.push(value)
	$("#content").html("")
	var start=0
	if(messages.length > count){
		start=messages.length-count
	}

	for(var i=start;i <messages.length;i++){
			$("#content").prepend("<li><strong>"+messages[i].name+"</strong>: "+messages[i].message+"</li>")
		}w
	//$("#content").prepend("<p>"+value.name+": "+value.message+"</p>")
})