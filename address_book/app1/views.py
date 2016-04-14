from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    global header
    user = "Logan"
    html = """<h1>This is a website. Hello %s</h1>
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
    """%(user)
    return HttpResponse(html)

def home(request):
    global header
    user = "Logan"
    html = "<h1>Welcome to your address book %s</h1>"%user

    return HttpResponse(html)

def insertUser(request, user=None):
    #html= "insert user here"
    errors = []
    user = "Zack"
    data = {
        'heading': 'Insert a New User',
        'content': 'Fill in the following information',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def deleteUser(request, user=None):
    #html= "delete user here"
    errors = []

    data = {
        'heading': 'Delete a User',
        'content': 'Chooses which User to Delete',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def updateUser(request, user=None):
    #html= "update user here"
    errors = []

    data = {
        'heading': 'Update User Information',
        'content': 'Fill in the following UPDATED information',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def searchUser(request, user=None):
    #html= "search for users here"
    errors = []

    data = {
        'heading': 'Search for a User',
        'content': 'Fill in the following information',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def template(request):
    errors = []

    data = {
        'heading': 'Add New Student Grade',
        'content': 'Fill in the following information',
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)


