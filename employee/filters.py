import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    post = django_filters.CharFilter(field_name='post', lookup_expr='iexact')
    employee_name = django_filters.CharFilter(field_name='employee_name',lookup_expr='iexact' )
    id = django_filters.RangeFilter(field_name='id')

    class Meta:
        model = Employee
        fields =['post', 'employee_name', 'id']