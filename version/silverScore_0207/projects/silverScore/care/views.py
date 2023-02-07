from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db import models
from .models import CareRank
from .models import AddressInfo
from django.db.models import Q

# Create your views here.

# generic
# listView
class CareListView(ListView):
    model = CareRank # 사용할 메인 model
    template_name = 'care/care_list.html'  # render할 path
    context_object_name = 'care_list' # 해당의 view로 넘길 객체 이름

    def get_context_data(self, **kwargs):
        context = super(CareListView, self).get_context_data(**kwargs)
        context["address_info"] = AddressInfo.objects.all()
        context["siDo_info"] = AddressInfo.objects.filter(siGunGuCd__gt=0,DongCd__gt=0).order_by('siDoCd','siGunGuCd','DongCd').values()
        return context

    def get_queryset(self):
        return CareRank.objects.order_by('longTermAdminCd')


# deatilView
class CareDetailView(DetailView):
    model = CareRank # 사용할 메인 model
    template_name = 'care/care_detail.html'  # render할 path
    context_object_name = 'detail_info' # 해당의 view로 넘길 객체 이름

    def get_context_data(self, **kwargs):
        context = super(CareListView, self).get_context_data(**kwargs)
        context["address_info"] = AddressInfo.objects.all()
        return context

    def get_queryset(self):
        return super().get_queryset()
    
# 요양원 기본 목록
# def care_list(request):
#     # return HttpResponse("안녕하세요 care 오신것을 환영합니다.")
#     care_list = CareRank.objects.order_by('-ratingDate')
#     address_info = AddressInfo.objects.order_by('id')
#     context = {'care_list': care_list, 'address_info': address_info} # address 추가
#     return render(request, 'care/care_list.html', context)

# # 요양원 상세보기
# def care_detail(request, care_id):
#     care_detail = get_object_or_404(CareRank, pk=care_id)
#     # CareRank.objects.get(id=care_id)
#     context = {'care_detail': care_detail}
#     return render(request, 'care/care_detail.html', context)