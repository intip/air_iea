# coding: utf-8

from __future__ import unicode_literals

from decimal import Decimal
from json import dumps
from os.path import join
import codecs
import shutil

from django.conf import settings

from airlib import process_air
import database

from .models import Processing


def load_file(filepath):
    fobj = open(filepath)
    print Processing.objects.get_or_create(air_file=fobj)


def move_file(filepath, filepath2):
   """
   move file da raiz para a folder de processamento
   """
   shutil.move(filepath, filepath2)

def type_file(filepath):
    """ le o arquivo e define o tipo dele """
    try:
        fobj = open(filepath)
        line = fobj.readline()
        if line:
            type_file = line.split(';')[0]
            if type_file == 'AIR-BLK207':
                return 'hotel'
    except:
        pass
    return 


def process_file(filepath, processing=None):
    airdata, ieadata, ieafilename = process_air(filepath)
    print 'Processing', filepath
    print ieafilename
    print filepath
    filepath = filepath.replace("%s/" % settings.MEDIA_ROOT, "")
    print filepath
    if processing is None:
        processing, nil = Processing.objects.get_or_create(air_file=filepath)
    processing.air_json_data = dumps(airdata)

    update_fields = ['air_json_data']
    for k, v in airdata.items():
        k = "air_%s" % k
        setattr(processing, k, v)
        update_fields.append(k)

    for k, v in ieadata.items():
        if k == 'CodFop' and v.startswith("CC"):
            v = "CC"

        elif k == 'NumCcr' and airdata['GUOPT'] != "FAT":
            v = ieadata['CodFop'][2:19]

        elif k == "TaxFor":
            total = Decimal(airdata['TOTRT_Number'])
            roomrte = Decimal(airdata['ROOMRTE'])
            days = int(airdata['RATEPER'])
            taxfor = total - (roomrte * days)
            v = ("TX%.2f/" % taxfor).replace(".", "")

        elif k == 'ForRep':
            if 'PNRRMK_ForRep' in airdata:
                print 'v', v
                if v == 'CMNET':
                    v = database.get_hotel_code(airdata['HTLNME'])

                elif v == 'TREND':
                    v = 5363

        if k == 'AgtRsv':
            bkagt = v.strip()
            v = database.get_regente_code(bkagt)

        k = "iea_%s" % k
        setattr(processing, k, v)
        update_fields.append(k)

    processing.save()  # update_fields=update_fields)

    print processing.pk,
    print processing,
    print ieafilename
    iea_file = join("output", ieafilename)
    ieafilepath = join(settings.MEDIA_ROOT, iea_file)
    ieafile = codecs.open(ieafilepath, "w", "utf-8")
    ieafile.write(processing.generate_iea_file_contents())
    processing.iea_file = iea_file
    processing.save(update_fields=['iea_file'])
