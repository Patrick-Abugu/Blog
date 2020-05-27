  function toggle(){
    var e =document.getElementById('nav-div');
    var m =document.getElementById('image1-div');
    if(e.style.display=== 'none'){
      e.style.display='block';
      e.style.width='100%';
      e.style.top='0px';
      e.style.position='fixed';
      e.style.background='white';
      e.style.transition='all 1s linear';
      m.style.top='200px';
    }
    else{
      e.style.display='none';
    }
  }

function hide(){
  var m = window.matchMedia("screen and (max-width:882px)");
  if(m.matches){
    var a =document.getElementById('nav-div');
    a.style.display='none';
  }
  else{
    a.style.display='inline';
  }

}

  /*function nav(){
    alert("Welcome");
    var m = window.matchMedia("screen and (min-width:882px)");
    var e =document.getElementById('nav-div');
    if(mq.matches){
      e.ul.li.style.display='inline';
      e.style.background='white';
      e.style.zIndex='1';
      e.style.width='100%';
      e.style.textAlign='right';
      e.style.marginTop='50px';
    }
    else{
      e.style.display='none';
    }
  }
  */
