s = document.getElementById 'send'
e = document.getElementById 'senha'
pm = document.getElementById 'pm'
al = document.getElementById 'all'
z = document.getElementById 'z'
u = document.getElementById 'u'

insert0 = ! -> e.value+=0

insert1 = ! -> e.value+=1

reset = ! -> e.value = ''

doneGif = ! ->
# here we deploy the gif from the serve's url
              am = document.getElementById 'check'
              am.src = "/static/check-unscreen.gif"
              am.style.width = '200px'
              am.style.height = '200px'
              des = ! -> am.src = ''
              s = setTimeout des,'3500'

setNewInfo = ! ->
              xmlhttp
              xmlhttp = new XMLHttpRequest!
              xmlhttp.onreadystatechange = ! ->
                              s.style.backgroundColor = '#1DB954'
                              pm.innerHTML = "Done!"
                              doneGif!

              xmlhttp.open "GET", "http://192.168.100.36:5000/senha?senha=#{e.value}", true
              xmlhttp.send()
              e.value = ""

s.addEventListener "click", setNewInfo
z.addEventListener "click", insert0
u.addEventListener "click", insert1
