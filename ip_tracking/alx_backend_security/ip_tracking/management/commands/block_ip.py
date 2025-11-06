from django.core.mangement.base import BaseCommand
from ip_tracking.models import BlockedIP

class Command(BaseCommand):
    help = 'Add an IP address to the blacklist'

    def add_atguments(self, parser):
        parser.add_argument('ip_address', type=str)

    def handle(self, *args, **kwargs):
        ip = kwargs['ip_address']
        BlockedIP.objects.get_or_create(ip_address=ip)
        self.stdout.write(self.style.SUCCESS(f"IP {ip} blocked successfully."))
