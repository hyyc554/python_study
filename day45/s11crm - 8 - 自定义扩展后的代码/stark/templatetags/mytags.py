# -*- coding: utf-8 -*-
from types import FunctionType
from django import template

register = template.Library()


@register.inclusion_tag('stark/list_tag.html')
def get_list_tag(self):
    queryset = self.model_class.objects.all().order_by(*self.get_order_by())
    list_display = self.list_display

    header_list = []
    if list_display:
        for name_or_func in list_display:
            if isinstance(name_or_func, FunctionType):
                verbose_name = name_or_func(self, header=True)
            else:
                verbose_name = self.model_class._meta.get_field(name_or_func).verbose_name
            header_list.append(verbose_name)
    else:
        header_list.append(self.model_class._meta.model_name)

    body_list = []
    for row in queryset:
        row_list = []
        if not list_display:
            row_list.append(row)
            body_list.append(row_list)
            continue
        for name_or_func in list_display:
            if isinstance(name_or_func, FunctionType):
                val = name_or_func(self, row=row)
            else:
                val = getattr(row, name_or_func)
            row_list.append(val)
        body_list.append(row_list)
    return {'header_list': header_list, 'body_list': body_list}
