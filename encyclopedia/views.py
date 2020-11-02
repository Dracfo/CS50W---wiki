from markdown2 import Markdown
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# Get and return the desired wiki entry
def wiki(request, title):  
    # Get the entry from the url
    entry = util.get_entry(title)

    # Check if the entry exists
    if not entry:
        return render(request, "encyclopedia/entry.html", {
            "entry": "ERROR: Requested File Not Found",
            "title": "ERROR"
        })

    # Convert the markdown entry to html
    markdowner = Markdown()
    html = markdowner.convert(entry)

    # Else return the requested page
    return render(request, "encyclopedia/entry.html", {
        "entry": html,
        "title": title
    })


def search(request):
    return render(request, "encyclopedia/search.html")