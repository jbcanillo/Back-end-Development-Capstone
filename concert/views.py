from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from concert.forms import LoginForm, SignUpForm
from concert.models import Concert, ConcertAttending
import requests as req


# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.filter(username=username).first()
            if user:
                return render(request, "signup.html", {"form": SignUpForm, "message": "user already exist"})
            else:
                user = User.objects.create(
                    username=username, password=make_password(password))
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return render(request, "signup.html", {"form": SignUpForm})
    return render(request, "signup.html", {"form": SignUpForm})


def index(request):
    return render(request, "index.html")


def songs(request):
    songs = [
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aa6"
            },
            "id": 1,
            "lyrics": "Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.",
            "title": "duis faucibus accumsan odio curabitur convallis"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aa7"
            },
            "id": 2,
            "lyrics": "Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.\n\nMaecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.",
            "title": "dictumst etiam faucibus cursus urna ut"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aa8"
            },
            "id": 3,
            "lyrics": "Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.\n\nPraesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.",
            "title": "in faucibus orci luctus et ultrices"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aa9"
            },
            "id": 4,
            "lyrics": "Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.\n\nSed ante. Vivamus tortor. Duis mattis egestas metus.",
            "title": "nulla quisque arcu libero rutrum ac"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aaa"
            },
            "id": 5,
            "lyrics": "Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.\n\nMauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.\n\nNullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
            "title": "luctus rutrum nulla tellus in sagittis dui vel nisl"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aab"
            },
            "id": 6,
            "lyrics": "Quisque porta volutpat erat. Quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. Nunc purus.\n\nPhasellus in felis. Donec semper sapien a libero. Nam dui.",
            "title": "diam id ornare imperdiet sapien urna pretium nisl ut volutpat"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aac"
            },
            "id": 7,
            "lyrics": "Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.\n\nFusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.",
            "title": "molestie sed justo pellentesque viverra pede ac"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aad"
            },
            "id": 8,
            "lyrics": "Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus. Nulla suscipit ligula in lacus.",
            "title": "adipiscing lorem vitae mattis nibh ligula nec sem duis aliquam"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aae"
            },
            "id": 9,
            "lyrics": "Phasellus in felis. Donec semper sapien a libero. Nam dui.",
            "title": "ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998aaf"
            },
            "id": 10,
            "lyrics": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.\n\nVestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.\n\nDuis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.",
            "title": "lacinia nisi venenatis tristique fusce"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998ab0"
            },
            "id": 11,
            "lyrics": "In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.\n\nNulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.\n\nCras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.",
            "title": "velit eu est congue elementum in"
        },
        {
            "_id": {
                "$oid": "6725c477b1bce18ac5998ab1"
            },
            "id": 12,
            "lyrics": "Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.\n\nInteger ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
            "title": "vestibulum vestibulum ante ipsum primis in faucibus orci luctus"
        },
    ]
    # songs = req.get("http://songs-sn-labs-jbcanillo.labs-prod-openshift-san-a45631dc5778dc6371c67d206ba9ae5c-0000.us-east.containers.appdomain.cloud/song").json()
    return render(request, "songs.html", {"songs": songs})


def photos(request):
    photos = req.get("https://pictures.1nrimg30xpl7.us-south.codeengine.appdomain.cloud/picture").json()
    return render(request, "photos.html", {"photos": photos})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return render(request, "login.html", {"form": LoginForm})
    return render(request, "login.html", {"form": LoginForm})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def concerts(request):
    if request.user.is_authenticated:
        lst_of_concert = []
        concert_objects = Concert.objects.all()
        for item in concert_objects:
            try:
                status = item.attendee.filter(
                    user=request.user).first().attending
            except:
                status = "-"
            lst_of_concert.append({
                "concert": item,
                "status": status
            })
        return render(request, "concerts.html", {"concerts": lst_of_concert})
    else:
        return HttpResponseRedirect(reverse("login"))


def concert_detail(request, id):
    if request.user.is_authenticated:
        obj = Concert.objects.get(pk=id)
        try:
            status = obj.attendee.filter(user=request.user).first().attending
        except:
            status = "-"
        return render(request, "concert_detail.html", {"concert_details": obj, "status": status, "attending_choices": ConcertAttending.AttendingChoices.choices})
    else:
        return HttpResponseRedirect(reverse("login"))
    pass


def concert_attendee(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            concert_id = request.POST.get("concert_id")
            attendee_status = request.POST.get("attendee_choice")
            concert_attendee_object = ConcertAttending.objects.filter(
                concert_id=concert_id, user=request.user).first()
            if concert_attendee_object:
                concert_attendee_object.attending = attendee_status
                concert_attendee_object.save()
            else:
                ConcertAttending.objects.create(concert_id=concert_id,
                                                user=request.user,
                                                attending=attendee_status)

        return HttpResponseRedirect(reverse("concerts"))
    else:
        return HttpResponseRedirect(reverse("index"))
