# coding: utf-8

from __future__ import unicode_literals

from datetime import datetime, date
from os.path import basename
import codecs
import re

from processors import PROCESSORS
import iealib


def fixdate(value):
    yy = value[0:2]
    mm = value[2:4]
    dd = value[4:6]
    return "%s/%s/20%s" % (dd, mm, yy)


def date_db_to_dmy(value):
    dt = datetime.strptime(value.lower(), "%d%b")
    dt = dt.replace(2014)
    return dt.strftime("%d/%m/%Y")


class AIRBLK207NotFound(Exception):
    pass


class AirKeyError(KeyError):
    pass


def get_line_proccessor_class(line):
    for proccessor_class in PROCESSORS:
        detect = proccessor_class.detect or r"^%s-" % proccessor_class.__name__
        if re.match(detect, line, re.U):
            return proccessor_class


def process_line(proccessor_class, line, lines):
    # print
    # print line
    # for line in lines:
    #     print line
    p = proccessor_class(line, lines)
    # pprint(p.data)
    # pprint(dict(p.data))
    return p


def get_air_data(filepath):
    data = {}
    fopen = codecs.open(filepath, 'r', 'utf-8')
    contents = fopen.read()
    if not "AIR-BLK207" in contents:
        raise AIRBLK207NotFound

    ilines = (l.strip() for l in contents.splitlines())
    data = {}
    for line in ilines:
        proccessor_class = get_line_proccessor_class(line)

        if proccessor_class is None:
            continue

        #     raise Exception("No proccessor for line: %s" % line)

        lines = []
        # nproccessor_class = None
        # for i in range(proccessor_class.extra_lines):
        #     nline = ilines.next()
        #     nproccessor_class = get_line_proccessor_class(nline)

        #     if nproccessor_class is not None:
        #         break

        #     lines.append(nline)
        p = process_line(proccessor_class, line, lines)
        data.update(p.data)
    return data


def fill_iea_values(ieadata, airdata):
    for key, meta in iealib.KEYS:

        if key == "DatCnf":
            value = date.today().strftime("%d/%m/%Y")

        else:

            default = meta.get("default", "")
            value = default

            if key in ieadata:
                value = ieadata[key]

            elif meta.get('airkey'):
                akey = meta['airkey']
                if akey in airdata:
                    transform = meta.get('transform')
                    value = airdata[akey]
                    if transform == 'fixdate':
                        value = fixdate(value)
                    elif transform == 'date_db_to_dmy':
                        value = date_db_to_dmy(value)
                    else:
                        mask = meta.get("mask")
                        if mask == 'ZZZ.ZZZ.ZZ9,99':
                            value = value.replace(".", ",")

                elif default is None:
                    value = "{{ Missing:%s:%s }}" % (key, akey)
                    # raise AirKeyError(akey)

                else:
                    value = ""

            if value is None:
                value = "{{ Missing:%s }}" % key

        ieadata[key] = value


def generate_iea_content(ieadata, ieavalues):
    content = ";".join(ieavalues)
    return ieadata['IdtArq'], content


def process_air(filepath):
    fname = get_filename(filepath)
    ieadata = {
        'IdtArq': fname,
    }
    airdata = get_air_data(filepath)
    ieafilename = "%s.iea" % fname
    airfilename ="%s.AIR" % fname
    fill_iea_values(ieadata, airdata)
    return airdata, ieadata, ieafilename, airfilename


def get_filename(filepath):
    fname = basename(filepath)
    fname = fname.split(".", 1)[0]
    while fname.startswith("@") or fname.startswith("0"):
        fname = fname[1:]
    return fname
