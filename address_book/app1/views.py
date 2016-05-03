from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


# Create your views here.
def index(request, user=None):
    errors = []

    data = {
        'heading': 'Address Book',
        'content': 'This is an address book',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def home(request, user=None):
    errors = []

    data = {
        'heading': 'Address Book',
        'content': 'This is an address book',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/home.html', data)

def deleteUser(request, user=None):
    errors = []

    data = {
        'heading': 'Delete a Contact',
        'content': 'Chooses which Contact to Delete',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def updateUser(request, user=None):
    errors = []

    query_result = Student.objects.all()
    data = {
        'heading': 'Update Contact Information',
        'content': 'Fill in the following UPDATED information',
        'user' : user,
        'errors': errors,
        'query_result': query_result,
    }

    return render(request, 'app1/update.html', data)

def saveUser(request, userId=None):
    errors = []
    
    if request.method == 'POST':

        #do form validation on back end
        if not request.POST.get('first_name', ''):
            errors.append('Enter first name.')
        if not request.POST.get('last_name'):
            errors.append('Enter last name.')
        if not request.POST.get('phone', ''):
            errors.append('Enter phone')
        if not request.POST.get('email', ''):
            errors.append('Enter email')

        data = {'heading': 'Thank You!',
                'content': 'Your entry updated!',
                'errors': errors,
            }
        if errors:
            data['heading'] = 'Update Contact Information'
            data['content'] = 'Fill in the following UPDATED information'
            return render(request, 'app1/update.html', data)
        else:
            if userId:
                student = Student.objects.get(pk=userId)
                student.first_name = request.POST.get('first_name')
                student.last_name = request.POST.get('last_name')
                student.phone = (request.POST.get('phone'))
                student.email = (request.POST.get('email'))
                student.save()

                query_result = Student.objects.all()
                data['heading'] = 'Success'
                data['content'] =  '%s %s updated successfully!'%(request.POST.get('first_name'),request.POST.get('last_name'))
                data['student'] = student
                data['query_result'] = query_result
            return render(request, 'app1/update.html', data)

def searchUser(request, user=None):
    errors = []

    data = {
        'heading': 'Search for a Contact',
        'content': 'Fill in the following information',
        'user' : user,
        'errors': errors,
    }

    return render(request, 'app1/search.html', data)

def template(request):
    errors = []

    data = {
        'heading': 'Add New Student Grade',
        'content': 'Fill in the following information',
        'errors': errors,
    }

    return render(request, 'app1/template.html', data)

def viewAll(request, user=None):
    errors=[]
    query_result = Student.objects.all()
    
    data = {
        'heading': 'View All Contacts',
        'content':'The following is a list of all contacts',
        'user':user,
        'errors':errors,
        'query_result': query_result,
    }

    return render(request,'app1/db_Display_Template.html',data)

def addUser(request, contact_id=None):
    errors = []
    if request.method == 'POST':
        # handle data posted from the from
        if not request.POST.get('first_name', ''):
            errors.append('Enter first name.')
        if not request.POST.get('last_name'):
            errors.append('Enter last name.')
        if not request.POST.get('email', ''):
            errors.append('Enter email')
        if not request.POST.get('phone', ''):
            errors.append('Enter phone number')

        data = {'heading': 'Contact Added!',
                'content': 'Your data has been saved!',
                'errors': errors,
            }

        # This essentially returns the page if there is errors and makes you refill it out
        if errors:
            data['heading'] = 'Add New Contact'
            data['content'] = 'Fill in the following information:'
            return render(request, 'app1/new_Student.html', data)
        else:
            if contact_id: # checks to see if student id was provided and if so sets that student to what we are editing
                student = Student.objects.get(pk=id)
            else:
                student = Student() # if no contact id is provided, create a new student object
            student.first_name = request.POST.get('first_name')
            student.last_name = request.POST.get('last_name')
            student.email = request.POST.get('email')
            student.phone = request.POST.get('phone')
            student.save()
            data['heading'] = 'Success'
            data['content'] = 'Contact updated successfully!'
            data['student'] = student
            return render(request, 'app1/new_Student.html', data)
    else:
        if not contact_id:
            # must be a get method to enter new grade info so render the form for user to enter
            # data
            data = {
                'heading': 'Add New Contact',
                'content': 'Fill in the following information',
                'errors': errors,
            }
        else:
            # edit existing student
            student = Student.objects.get(pk=id)
            data = {
                'heading': 'Edit Contact',
                'content': 'Update the following information',
                'errors': errors,
                'student':student,
            }

        return render(request, 'app1/new_Student.html', data)




