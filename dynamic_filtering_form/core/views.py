from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.


def BootstrapFilterView(request):
    queryset = Journal.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get("title_contains")
    id_exact_query = request.GET.get("title_exact")
    title_or_author_query = request.GET.get("title_or_author")
    view_count_min = request.GET.get("view_count_min")
    view_count_max = request.GET.get("view_count_max")
    publish_date_min = request.GET.get("publish_date_min")
    publish_date_max = request.GET.get("publish_date_max")
    category = request.GET.get("category")
    reviewed = request.GET.get("reviewed")
    not_reviewed = request.GET.get("not_reviewed")

    def is_valid_queryparam(param):
        return param != "" and param is not None

    if is_valid_queryparam(title_contains_query):
        queryset = queryset.filter(title__icontains=title_contains_query)

    elif is_valid_queryparam(id_exact_query):
        queryset = queryset.filter(id=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        queryset = queryset.filter(Q(title__icontains=title_or_author_query) |
                                   Q(author__name__icontains=title_or_author_query)).distinct()

    if is_valid_queryparam(view_count_min):
        queryset = queryset.filter(views__gt=view_count_min)

    if is_valid_queryparam(view_count_max):
        queryset = queryset.filter(views__lt=view_count_max)

    if is_valid_queryparam(publish_date_min):
        queryset = queryset.filter(publish_date__gt=publish_date_min)

    if is_valid_queryparam(publish_date_max):
        queryset = queryset.filter(publish_date__lt=publish_date_max)

    if is_valid_queryparam(category) and category != "Choose...":
        queryset = queryset.filter(categories__name=category)

    if reviewed:
        queryset = queryset.filter(reviewed=True)

    elif not_reviewed:
        queryset = queryset.filter(reviewed=False)

    context = {
        "queryset": queryset,
        "categories": categories,
    }
    return render(request, "bootstrap_form.html", context )


