from django.shortcuts import render, redirect
from .models import Menu, Booking
from .forms import BookingForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookingSerializer, MenuSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book.html', {'form': form})


def bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return render(request, 'bookings.html', {'bookings': serializer.data})


def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_data})


def display_menu_item(request, pk=None):
    menu_item = Menu.objects.get(pk=pk) if pk else ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


@api_view(['GET'])
def bookings_api(request):
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
    else:
        bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def menu_api(request):
    menu = Menu.objects.all()
    serializer = MenuSerializer(menu, many=True)
    return Response(serializer.data)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')