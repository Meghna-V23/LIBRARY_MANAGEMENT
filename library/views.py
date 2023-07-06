from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from library.models import *



# Create your views here.

# Create your views here.
def log(request):
    username = request.POST["textfield"]
    password = request.POST["textfield2"]
    object = login_table.objects.get(username=username,password=password)
    try:
        if object is None:
             return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')
        elif object.type == "admin":
             request.session['lid'] = object.id
             return HttpResponse('''<script>alert("success");window.location ="admin_home"</script>''')
        elif object.type == "user":
            request.session['lid'] = object.id
            return HttpResponse('''<script>alert("success");window.location="userhome"</script>''')
        elif object.type == "library":
            request.session['lid'] = object.id
            return HttpResponse('''<script>alert("success");window.location="library_home"</script>''')
        else:
             return HttpResponse('''<script>alert("invalid");window.location="/</script>''')
    except:
           return HttpResponse('''<script>alert("invalid");window.location="/</script>''')


def add_and_mangelibrary(request):
    ob = library_table.objects.all()
    print(ob)
    return render(request,'add and manage library.html',{'val':ob})


def edit_library(request,id):
    ob = library_table.objects.get(id=id)
    print(ob)
    request.session['libid']=id
    return render(request,'edit library.html',{'val':ob})

def edit_lib(request):
    libraryname = request.POST["textfield"]
    place = request.POST["textfield2"]
    email = request.POST["textfield5"]
    post = request.POST["textfield3"]
    pin = request.POST["textfield4"]
    phone = request.POST["textfield6"]

    object1 = library_table.objects.get(id=request.session['libid'])

    object1.libraryname = libraryname
    object1.email = email
    object1.place = place
    object1.post = post
    object1.pin = pin
    object1.phone = phone
    object1.save()

    return HttpResponse('''<script>alert("update");window.location="/add_and_mangelibrary"</script>''')

def deletelibrary(request,id):
    obj = library_table.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert("delete");window.location="/add_and_mangelibrary"</script>''')

def add_library(request):
    return render(request,'addlibrary-admin .html')

def add_lib(request):
    libraryname = request.POST["textfield"]
    place = request.POST["textfield2"]
    email = request.POST["textfield5"]
    post = request.POST["textfield3"]
    pin = request.POST["textfield4"]
    phone = request.POST["textfield6"]
    username = request.POST["textfield7"]
    password = request.POST["textfield8"]

    object = login_table()
    object.username = username
    object.password = password
    object.type = "library"
    object.save()

    object1 = library_table()
    object1.libraryname = libraryname
    object1.place = place
    object1.email = email
    object1.post = post
    object1.pin = pin
    object1.phone = phone
    object1.lid = object
    object1.save()

    return HttpResponse('''<script>alert("update");window.location="/add_and_mangelibrary"</script>''')






def admin_home(request):
    return render(request, 'admin home.html')

def library_home(request):
    return render(request, 'library home.html')

def library_reg(request):
    return render(request, 'indexlib.html')

def libreg(request, obect=None):
    libraryname = request.POST["textfield"]
    email = request.POST["textfield5"]
    place = request.POST["textfield2"]
    post = request.POST["textfield3"]
    pin = request.POST["textfield4"]
    phone = request.POST["textfield6"]
    username = request.POST["textfield7"]
    password = request.POST["textfield8"]

    object = login_table()
    object.username = username
    object.password = password
    object.type = "pending"
    object.save()

    object1 = library_table()
    object1.libraryname = libraryname
    object1.email = email
    object1.place =place
    object1.post = post
    object1.pin = pin
    object1.phone = phone
    object1.lid = object
    object1.save()

    return HttpResponse('''<script>alert("success");window.location="/"</script>''')


def login(request):
    return render(request, 'log  in.html')



def managebook_lib(request):
    ob = book_table.objects.filter(libid__lid=request.session['lid'])
    print(ob)
    return render(request, 'manage book lib.html', {'val': ob})

def editbooks1(request,id):
    ob = book_table.objects.get(id=id)
    print(ob)
    request.session['id'] = id
    return render(request,'edit books.html',{'val':ob})




def edit_books(request):
    try:
        bookname = request.POST["textfield"]
        image = request.FILES["file"]
        fs = FileSystemStorage()
        fsave = fs.save(image.name, image)
        authorname = request.POST["textfield2"]

        object1 = book_table.objects.get(id=request.session['id'])
        object1.bookname = bookname
        object1.image = image
        object1.authorname = authorname

        object1.save()

        return HttpResponse('''<script>alert("update");window.location="/managebook_lib"</script>''')
    except:
        bookname = request.POST["textfield"]
        authorname = request.POST["textfield2"]

        object1 = book_table.objects.get(id=request.session['id'])
        object1.bookname = bookname
        object1.authorname = authorname

        object1.save()

        return HttpResponse('''<script>alert("update");window.location="/managebook_lib"</script>''')


def deletebooks(request,id):
    obj = book_table.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert("delete");window.location="/managebook_lib"</script>''')

def addbooks1(request):
    return render(request,'add books.html')

def addbooks(request):
    bookname = request.POST["textfield"]
    image = request.FILES["file"]
    fs = FileSystemStorage()
    fsave = fs.save(image.name,image)
    authorname = request.POST["textfield2"]


    object1 = book_table()
    object1.bookname = bookname
    object1.image = fsave
    object1.authorname = authorname
    object1.libid = library_table.objects.get(lid=request.session['lid'])
    object1.save()

    return HttpResponse('''<script>alert("successfully added");window.location="/managebook_lib"</script>''')




def send_complaint(request):
    ob = library_table.objects.all()
    return render(request, 'send complaint - user.html',{'val':ob})


def s_complaint(request):
    library = request.POST["select"]
    print(library)
    complaint = request.POST["textarea"]

    object2 = complaint_table()
    object2.complaint = complaint
    object2.date = datetime.now().strftime("%Y-%m-%d")
    object2.reply = 'pending'
    object2.uid = user_table.objects.get(lid__id = request.session['lid'])
    object2.libid = library_table.objects.get(id=library)
    object2.save()
    return HttpResponse('''<script>alert("success");window.location="send_complaint"</script>''')


def sendrating_user(request):
    ob = library_table.objects.all()
    return render(request, 'send rating- user.html',{'val':ob})

def usrrating(request):
    libraries = request.POST["select2"]

    print(libraries)
    rating = request.POST["select"]
    object3 = rating_table()
    object3.rating = rating
    object3.date = datetime.now().strftime("%Y-%m-%d")
    object3.uid = user_table.objects.get(lid__id=request.session['lid'])
    object3.libid = library_table.objects.get(id=libraries)
    object3.save()
    return HttpResponse('''<script>alert("success");window.location="sendrating_user"</script>''')




def userhome(request):
    return render(request, 'user home.html')

def userreg(request):
    return render(request, 'userregindex.html')

def usrrg(request,object=None):
    fname = request.POST["textfield"]
    housename = request.POST["textfield2"]
    email = request.POST["textfield7"]
    place = request.POST["textfield3"]
    post = request.POST["textfield4"]
    pin = request.POST["textfield5"]
    phone = request.POST["textfield6"]
    username = request.POST["textfield8"]
    password = request.POST["textfield9"]

    object = login_table()
    object.username = username
    object.password = password
    object.type = "user"
    object.save()

    object1 = user_table()
    object1.username = fname
    object1.housename = housename
    object1.email = email
    object1.place = place
    object1.post = post
    object1.pin = pin
    object1.phone = phone
    object1.lid = object
    object1.save()

    return HttpResponse('''<script>alert("success");window.location="/"</script>''')


def verifylibrary(request):
    ob = library_table.objects.all()
    return render(request, 'verify library.html',{'val':ob})

def Accept_library(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "library"
    obj.save()
    return HttpResponse('''<script>alert("Accepted");window.location="/verifylibrary"</script>''')


def Reject_library(request,id):
    obj = login_table.objects.get(id=id)
    obj.type = "Rejected"
    obj.save()
    return HttpResponse('''<script>alert("Rejected");window.location="/verifylibrary"</script>''')


def viewbook_adm(request):
    ob = book_table.objects.all()
    print(ob)
    return render(request, 'view book adm.html', {'val': ob})


def viewbooks_user(request,id):
    ob = book_table.objects.filter(libid__lid__id=id)
    print(ob)
    return render(request, 'view books - user.html', {'val': ob})


def viewcomplaintreply_user(request):
    ob = complaint_table.objects.filter(uid__lid__id=request.session['lid'])
    print(ob,"hhhhhhhhhhhhhhhhhhhh")
    return render(request, 'view com reply - user.html',{'val':ob})

def viewlib_and_books(request):
    ob = library_table.objects.all()
    print(ob)
    return render(request, 'view lib and books- user.html',{'val':ob})



def viewrating_lib(request):
    ob = rating_table.objects.filter(libid__lid__id=request.session['lid'])
    print(ob)
    return render(request, 'view rating -lib.html', {'val': ob})


def viewratinglibrary_adm(request):
    ob = rating_table.objects.all()
    print(ob)
    return render(request, 'view rating libary-adm.html', {'val': ob})




def admin_home(request):
    return render(request, 'admin home.html')

def viewuser_adm(request):
    ob = user_table.objects.all()
    return render(request, 'view user adm.html', {'val': ob})


def viewcomplaintsndrply_lib(request):
    ob = complaint_table.objects.filter(libid__lid__id=request.session['lid'])
    print(ob)
    return render(request, 'viewcomplaint snd rply -lib.html', {'val': ob})

def sendreply_lib(request,id):
    ob = complaint_table.objects.get(id=id)
    request.session['complaint'] = id
    return render(request, 'send reply lib.html', {'val': ob})



def sndrplylib(request):
    reply = request.POST["textarea"]
    object4 = complaint_table.objects.get(id=request.session['complaint'])
    object4.reply = reply
    object4.save()
    return HttpResponse('''<script>alert("success");window.location="/viewcomplaintsndrply_lib"</script>''')








