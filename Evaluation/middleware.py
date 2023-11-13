# Evaluation/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/script/' and not request.session.get('authenticated'):
            return redirect('errorPage')
        
        response = self.get_response(request)
        return response
