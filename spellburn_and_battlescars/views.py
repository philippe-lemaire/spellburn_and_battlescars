from django.shortcuts import render


def page_not_found_view(request, exception=None):
    return render(request, "404.html")


def error_view(request, exception=None):
    return render(request, "500.html")
