from django.shortcuts import render
from django.http import HttpResponse

header = """<link rel='stylesheet' href='css/global.css' /><link rel='stylesheet' href='css/bootstrap.min.css' />
"""
# Create your views here.
def index(request):
	global header
	user = "Logan"
	html = """%s<h1>This is a website. Hello %s</h1>
	<script type="text/javascript">
	window.addEventListener("load", colorStuff, false);

	function colorStuff(){
		setInterval( function(){
			r = Math.floor(Math.random() * 255);
			g = Math.floor(Math.random() * 255);
			b = Math.floor(Math.random() * 255);
			var h1s = document.getElementsByTagName("h1");
			h1s[0].setAttribute("style", "color: rgb("+r+","+g+","+b+"); font-size: 100px;");
			},1000);
	}

	</script>
	"""%(header, user)
	return HttpResponse(html)

def home(request):
	global header
	user = "Logan"
	html = """%s<h1>Welcome to your address book %s</h1>
	"""%(header, user)

	return HttpResponse(html)

def insertUser(request, user=None):
	html= "insert user here"

	return HttpResponse(html)

def deleteUser(request, user=None):
	html= "delete user here"

	return HttpResponse(html)

def updateUser(request, user=None):
	html= "update user here"

	return HttpResponse(html)

def searchUser(request, user=None):
	html= "search for users here"

	return HttpResponse(html)

