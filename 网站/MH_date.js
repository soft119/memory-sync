       var nowdate=new Date(); 
       var y =nowdate.getFullYear();
       var m = (nowdate.getMonth()+1).toString().padStart(2,'0');
       var day = nowdate.getDay();

if (day==0){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
}else if(day==1){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
}else if(day==2){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
}else if(day==3){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
}else if(day==4){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
}else if(day==5){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
}else if(day==6){
       var day1 = y+'年'+m+'月'+day+'日'+'下午16:00';
       var day2 = y+'年'+m+'月'+day+'日'+'晚上20:00';
};
document.getElementById("day1").innerHTML = day1;
document.getElementById("day2").innerHTML = day2;
 