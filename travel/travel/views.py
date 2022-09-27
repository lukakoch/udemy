

from os import rename
from pydoc import render_doc
from django.shortcuts import render

def home(request):
    name = "Bob"
    return render(request, "home.html", {"name": name})