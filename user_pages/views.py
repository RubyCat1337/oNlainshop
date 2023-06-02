from django.shortcuts import render


def show_about_us(request):
    return render(request, "user_pages/about_us.html")

def show_main(request):
    return render(request, "user_pages/main.html")
