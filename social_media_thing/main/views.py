from django.shortcuts import render
from django.http import HttpResponse as response
from django.template import loader
from django.urls import reverse
# Create your views here.

def index(request) -> response:
    """
    main_page = loader.get_template("index.html")
    return response(main_page.render())
    """
    return render(request, "index.html")
