from django.shortcuts import render

rooms = [
    {'room_id':'1', 'room_name':'psychiatrist'},
    {'room_id':'2', 'room_name':'internal medicine'},
    {'room_id':'3', 'room_name':'cardiologist'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = None
    for r in rooms:
        if r['room_id']==pk:
            room = r
    context = {'room':room}
    return render(request, 'base/room.html', context)
