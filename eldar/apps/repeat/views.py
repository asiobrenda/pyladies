from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from.models import TennisClub, Author, Books
from.object import PFiles
from .load_data import AlgoUE

def home(request):
    home_ = "WELCOME TO MY HOME PAGE, repeat application"
    author_ = Author.objects.all()
    PFiles()
    return render(request, 'repeat/index.html', {'heading': home_, 'author':author_})


def get_author(request, author_id):
    varx = "AND THEIR BOOKS"
    author_ = Author.objects.get(pk=author_id)
    books_ = Books.objects.filter(author=author_)

    return render(request, 'repeat/author.html', {'heading': varx, 'author':author_, 'books':books_})



def tables(request):
    models = "This is where we will create html tables"
    tennis_club = TennisClub.objects.all()
    #print(tennis_club)

    return render(request, 'repeat/tables.html', {'model':models, 'members':tennis_club})

def addmember(request):
    tclub_ = 'ADD NEW MEMBER'

    if request.method == 'POST':
        name_ = request.POST['fname']
        gender_ = request.POST['gender']
        bio_   = request.POST['bio']
        #print(name_, gender_, bio_ )

        TennisClub.objects.create(member_name=name_, gender=gender_, bio=bio_ )

        return redirect('repeat:Tables')
    return render(request, 'repeat/newmember.html', {'tclub':tclub_})


def view_member(request, pk):
    view_ = 'View the new member'

    view_member = TennisClub.objects.get(id=pk)


    return render(request, 'repeat/view.html', {'view':view_, 'member':view_member})

def update_member(request, pk):
    update_ = 'Update the new member'

    update = TennisClub.objects.get(id=pk)

    if request.method =='POST':
        update.member_name = request.POST['fname']
        update.gender = request.POST['gender']
        update.bio = request.POST['bio']

        update.save()

        return redirect('repeat:Tables')
    return render(request, 'repeat/update.html', {'update1':update_, 'update2':update})

def district(request):
    view_ = 'LIST OF DISTRICTS'
    return render(request, 'repeat/upload_data.html', {'view':view_})


def upload_data(request):
    varx = "Data uploaded successfully"
    district = AlgoUE()
    print(district)
    district.process_excel_files()
    return render(request, 'repeat/load_data.html', {'varx': varx})

