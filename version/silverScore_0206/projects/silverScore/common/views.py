from django.shortcuts import render

# Create your views here.

def index(request):
    # care_list = CareRank.objects.order_by('-ratingDate')
    # context = {'care_list': care_list}
    return render(request, 'common/main.html')