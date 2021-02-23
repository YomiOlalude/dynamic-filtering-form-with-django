from django.shortcuts import render
from .models import *
from django.db.models Q

# Create your views here.


def BootstrapFilterView(request):
    queryset = Journal.objects.all()
    title_contains_query = request.GET.get("title_contains")
    id_exact_query = request.GET.get("title_exact")
    title_or_author_query = request.GET.get("title_or_author")

    if title_contains_query != "" and title_contains_query is not None:
        queryset = queryset.filter(title__icontains=title_contains_query)

    elif id_exact_query != "" and id_exact_query is not None:
        queryset = queryset.filter(id=id_exact_query)

    elif title_or_author_query != "" and title_or_author_query is not None:
        queryset = queryset.filter(views__iexact=title_or_author_query)

    context = {
        "queryset": queryset
    }
    return render(request, "bootstrap_form.html", context )


