
from django.core.management import BaseCommand, CommandError

from cameradaemon.image_process_main import ImageChannelsManager


class Command(BaseCommand):
    help = (
        "Run background process to handle camera streaming."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--max-camera', '-m', nargs='?',
            help='Max number of cameras to be monitored.',
        )

    def handle(self, **options):
        # Execute the command and exit.
        ImageChannelsManager.main(**options)

