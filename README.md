# Binar configuration core 🔒 

<p align="center">
<img src="https://github.com/synth-me/Binar/blob/main/static/locker-unscreen.gif" width=25% height=25% align='center'>
</p>

## Introduction 

<p> Binar is a binary locker made to be minimalist, useful and secure </p>
<p> The system was prototyped to be embedded in any micro-python 🐍 supported system</p>

## The system 
* Binar uses a simple flask server to make the app for the password config
* for the front-end we choosed livescript as a cleaner and more functional alternative to common Js 

## The Build

* To setup all project use the file 
```
setup.bat 
```
* Then acess the livescript core files and compile to javascript 
```
git clone 
automatic.bat 
```
* Then run the main server with 
```
py app.py 
```
* Then , in another terminal spawn the raspberry link 
```
py main.py
```

# The front-end 
<p>If everything went good when acessing the local server you must see </p>
<img src="https://github.com/synth-me/Binar/blob/main/static/Captura%20de%20Tela%20(111).png" width=50% height=50%>
<p> And after you input any binary combination : </p>
<img src="https://github.com/synth-me/Binar/blob/main/static/Captura%20de%20Tela%20(113).png" width=50% height=50%>


# Future updates 
```diff
+ A better hash system , given that the default hash from python is already well indexed a new and safer one is needed
+ GPIO better integration. Now the GPIO is interpreted as keyboard 0,1 not as output source, this must change to better integration between the interface 
```
