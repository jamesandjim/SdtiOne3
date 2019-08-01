from django.shortcuts import render
from django.views import View

# Create your views here.


class Register_list(View):
    def get(self, request):
        return render(request, 'register_list.html')