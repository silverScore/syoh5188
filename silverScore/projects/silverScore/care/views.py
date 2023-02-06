from django.shortcuts import render, get_object_or_404
from .models import CareRank

# Create your views here.

# 요양원 기본 목록
def care_list(request):
    # return HttpResponse("안녕하세요 care 오신것을 환영합니다.")
    care_list = CareRank.objects.order_by('-ratingDate')
    context = {'care_list': care_list}
    return render(request, 'care/care_list.html', context)

# 요양원 상세보기
def care_detail(request, care_id):
    care_detail = get_object_or_404(CareRank, pk=care_id)
    # CareRank.objects.get(id=care_id)
    context = {'care_detail': care_detail}
    return render(request, 'care/care_detail.html', context)