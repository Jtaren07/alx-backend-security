from .models import Requesting
from django.utils.depreciation import MiddlewareMixin
from ipware import get_client_ip


class IPLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, _ = get_client_ip(request)
        if ip is None:
            ip = '0.0.0.0'

        RequestLog.objects.create(
                ip_address=ip,
                path=request.path
        )
