from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    if util.get_entry(title) == None:
        return HttpResponse("Sorry, Your page was not found!")
    else:
        context = dict()
        for topic in util.list_entries:
            if topic == title:
                context["centent"] = title
                break

        return render(request, 
                      "encyclopedia/entry_page.html",
                      context)

