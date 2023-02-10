from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db import models
from .models import Care
# from .models import Review
from .models import Address
from django.db.models import Q

# Create your views here.

# generic

# listView
class CareListView(ListView):
    model = Care # 사용할 메인 model
    template_name = 'care/care_list.html'  # render할 path
    context_object_name = 'care_list' # 해당의 view로 넘길 객체 이름

    def get_context_data(self, **kwargs):
        context = super(CareListView, self).get_context_data(**kwargs)
        context["address_info"] = Address.objects.all()
        context["siDo_info"] = Address.objects.filter(siGunGuCd__gt=0, DongCd__gt=0).order_by('siDoCd','siGunGuCd','DongCd').values()
        # self.request.
        return context

    def get_queryset(self):
        return Care.objects.order_by('ratingGrade','-ratingCd')



# deatilView
class CareDetailView(DetailView):
    model = Care # 사용할 메인 model
    template_name = 'care/care_detail.html'  # render할 path
    context_object_name = 'detail_info' # 해당의 view로 넘길 객체 이름

    def get_context_data(self, **kwargs):
        context = super(CareListView, self).get_context_data(**kwargs)
        context["address_info"] = Address.objects.all()
        return context

    def get_queryset(self):
        return super().get_queryset()

