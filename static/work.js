// Generated by LiveScript 1.6.0
(function(){
  var s, e, pm, al, z, u, insert0, insert1, reset, doneGif, setNewInfo;
  s = document.getElementById('send');
  e = document.getElementById('senha');
  pm = document.getElementById('pm');
  al = document.getElementById('all');
  z = document.getElementById('z');
  u = document.getElementById('u');
  insert0 = function(){
    e.value += 0;
  };
  insert1 = function(){
    e.value += 1;
  };
  reset = function(){
    e.value = '';
  };
  doneGif = function(){
    var am, des, s;
    am = document.getElementById('check');
    am.src = "/static/check-unscreen.gif";
    am.style.width = '200px';
    am.style.height = '200px';
    des = function(){
      am.src = '';
    };
    s = setTimeout(des, '3500');
  };
  setNewInfo = function(){
    var xmlhttp;
    xmlhttp;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
      s.style.backgroundColor = '#1DB954';
      pm.innerHTML = "Done!";
      doneGif();
    };
    xmlhttp.open("GET", "http://192.168.100.36:5000/senha?senha=" + e.value, true);
    xmlhttp.send();
    e.value = "";
  };
  s.addEventListener("click", setNewInfo);
  z.addEventListener("click", insert0);
  u.addEventListener("click", insert1);
}).call(this);
