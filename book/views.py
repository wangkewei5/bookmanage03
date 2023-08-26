from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class SetSession(View):
    def get(self, request):
        # request.session = self.SessionStore(session_key)
        request.session['name'] = 'wkw05'
        return HttpResponse('haha')
