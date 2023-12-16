from django_filters.rest_framework import FilterSet, BaseInFilter, CharFilter

from .models import Book


class CharFieldInFilter(BaseInFilter, CharFilter):
    pass


class BookFilter(FilterSet):
    authors = CharFieldInFilter(method='filter_authors')

    def filter_authors(self, queryset, name, values):
        print(name, values)
        try:
            return queryset.filter(authors__id__in=values)
        except:
            return queryset.none()
    
    class Meta:
        model = Book
        fields = ('authors',)
