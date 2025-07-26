from django.shortcuts import render
from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry_page(request, title):
    if util.get_entry(title) == None:
        return render(request, 
                      "encyclopedia/error.html",
                      {
                          "title": "Error",
                          "message": "Page not found!"
                      })
    else:
        content = util.get_entry(title)
        html_content = markdown(content)

        context = {
            "title": title,
            "content": html_content
        }
        return render(request, 
                      "encyclopedia/entry_page.html",
                      context)

