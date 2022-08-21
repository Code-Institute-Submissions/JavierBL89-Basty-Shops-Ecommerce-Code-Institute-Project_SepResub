from django.shortcuts import render


def handler404_view(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler403_view(request, exception):
    """ Error Handler 403 - Forbiden access """
    return render(request, "errors/403.html", status=403)


def handler500_view(request, exception):
    """ Error Handler 500 - Internal server error """
    return render(request, "errors/500.html", status=500)
