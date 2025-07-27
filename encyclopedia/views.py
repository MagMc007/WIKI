from django.shortcuts import render, redirect
from . import util
from markdown2 import markdown
from .models import NewPageForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "title": "Encyclopedia"
    })


def entry_page(request, title):
    if util.get_entry(title):
        content = util.get_entry(title)
        html_content = markdown(content)

        context = {
            "title": title,
            "content": html_content
        }
        return render(request, 
                      "encyclopedia/entry_page.html",
                      context)

    else:
        return render(request, 
                      "encyclopedia/error.html",
                      {
                          "title": "Error",
                          "message": "Sorry, Page not found!"
                      })
       

def search_page(request):
    query = request.GET.get("q", "").strip()
    entries = util.list_entries() 

    # for the partial match and no match
    matches = []
    # full match
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect('encyclopedia:entry_page', title=entry)
    # for partial entry matching 
    for entry in entries:
        if query.lower() in entry.lower():
            matches.append(entry)
    return render(request, "encyclopedia/search.html", {
        "matches": matches
    })   


def new_page(request):
    return render(request, "encyclopedia/new_page.html", {
        "form": NewPageForm()
    })


def save_new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["Content"]
            util.save_entry(title, content)
            return redirect("encyclopedia:entry_page", title=title)