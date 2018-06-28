from django.shortcuts import render, redirect, reverse
from django.views import View
from orgs.models import OrgInfo


# Create your views here.
class OrgListView(View):
    def get(self, request):
        # 拿到所有的数据
        all_orgs = OrgInfo.objects.all()
        return render(request, 'orgs/org-list.html', {
            'all_orgs': all_orgs
        })
