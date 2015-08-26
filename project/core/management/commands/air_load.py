# coding: utf-8

from __future__ import unicode_literals

from glob import glob
from os.path import join, isdir, isfile, exists

from django.conf import settings
from django.core.management.base import BaseCommand

from airlib import AIRBLK207NotFound, AirKeyError
from core.tasks import process_file
path_hotel = settings.PATH_HOTEL

class Command(BaseCommand):
    help = "Carrega os arquivos Processing para o sistema."

    def handle_dir(self, path):
        paths = glob(join(path, "*.*"))
        for path in paths:
            process_file(path)

    def handle_file(self, filepath):
        try:
            process_file(filepath)

        except AIRBLK207NotFound, exc:
            print exc
            pass

        except AirKeyError, exc:
            print exc
            pass

    def handle(self, *args, **options):
        if args:
            for arg in args:
                if exists(arg):
                    if isfile(arg):
                        self.handle_file(arg)
                    elif isdir(arg):
                        self.handle_dir(arg)
        else:
            self.handle_dir(path_hotel)
