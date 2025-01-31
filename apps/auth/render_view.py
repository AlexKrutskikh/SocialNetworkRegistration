from django.shortcuts import render


def registration_completed(request):
    return render(request, "registration_completed.html")
