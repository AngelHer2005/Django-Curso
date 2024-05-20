from django.utils import timezone

class SesionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'session') and request.session.get('logged_in'):
                if not request.session.get('last_visit'):
                    request.session['last_visit'] = str(timezone.now())
        response = self.get_response(request)
        return response