# coding: utf-8

from collections import OrderedDict
import re


class Processor(object):
    detect = None
    ignore = ""
    keys = []
    keysre = None

    def __init__(self, line, lines=[]):
        self.lines = lines
        self.raw = line
        self.line = line[len(self.ignore):].strip(";")
        self.data = OrderedDict()
        self.update_data(self.line, self.keys)

    def update_data(self, line, keys):

        def process_re(re_):
            # print repr(self.keysre)
            # print repr(line)
            m = re.match(re_, line, re.U)
            try:
                d = m.groupdict()
            except AttributeError, exc:
                print self.__class__.__name__
                print 're', repr(re_)
                print 'line', repr(self.line)
                raise exc
            for k in sorted(d, key=m.span):
                # print k
                self.data[k] = d[k]

        if isinstance(self.keysre, (tuple, list)):
            re_ = r''
            for index, r in enumerate(self.keysre):
                re_ += r
                process_re(re_)
        elif self.keysre:
            process_re(self.keysre)

        elif self.keys:
            for index, part in enumerate(line.split(";")[:len(keys)]):
                # pprint(part)
                key = keys[index]
                if isinstance(key, tuple):
                    s = 0
                    for k, length in key:
                        self.data[k] = part[s: s + length]
                        s += length
                else:
                    self.data[key] = part


class D(Processor):
    detect = r"^D-"
    keysre = detect + \
        r"(?P<PNRDTE>\d{6})"


class RMCL(Processor):
    detect = r"^RM\*CL\."
    keysre = detect + \
        r"(?P<PNRRMK_CodCli>\w{0,127})"


class RMRD(Processor):
    detect = r"^RM\*RD\."
    keysre = detect + \
        r"(?P<PNRRMK_RsvDir>\w{0,127})"


class RMSG(Processor):
    detect = r"^RM\*SG\."
    keysre = detect + \
        r"(?P<PNRRMK_CodSgl>\w{0,127})"


class RMSL(Processor):
    detect = r"^RM\*SL\."
    keysre = detect + \
        r"(?P<PNRRMK_NomSol>[\w\/\s]{0,127})"


class RMFC(Processor):
    detect = r"^RM\*FC\."
    keysre = detect + \
        r"(?P<PNRRMK_FilCli>\w{0,127})"


class RMPR(Processor):
    detect = r"^RM\*PR\."
    keysre = detect + \
        r"\s*\d+\ \/\ (?P<PNRRMK_ForRep>\w+)"
        #r"(?P<PNRRMK_DadCnf>\w+)\s*" \

class RMAC(Processor):
    detect = r"^RM\*AC\."
    keysre = detect + \
        r"(?P<PNRRMK_AutCli>[\w\/\s]{0,127})"


class RMCC(Processor):
    detect = r"^RM\*CC\."
    keysre = detect + \
        r"(?P<PNRRMK_CcuPax>[\w\.]{0,127})"


class RMET1(Processor):
    detect = r"^RM\*ET1\."
    keysre = detect + \
        r"(?P<PNRRMK_CodEt1>\w{0,127})"


class RMET2(Processor):
    detect = r"^RM\*ET2\."
    keysre = detect + \
        r"(?P<PNRRMK_CodEt2>\w{0,127})"


class RMET3(Processor):
    detect = r"^RM\*ET3\."
    keysre = detect + \
        r"(?P<PNRRMK_CodEt3>\w{0,127})"


class RMTC(Processor):
    detect = r"^RM\*TC\."
    keysre = detect + \
        r"(?P<PNRRMK_VlrTch>\w{0,127})"


class RMMP(Processor):
    detect = r"^RM\*MP\."
    keysre = detect + \
        r"(?P<PNRRMK_MatFun>\w{0,127})"


class I(Processor):
    keysre = r"^" \
        r"(?P<MSGTAG>.{2})" \
        r"(?P<GCPSGR>\d{3})" \
        r";" \
        r"(?P<PSGRNBR>\d{1,2})" \
        r"(?P<PSGRNME>[\w\/\s]{2,64})"


class UHHL(Processor):
    detect = r"^U-.*HHL"
    keysre = (
        r"^",
        r"(?P<MSGTAG>.{2})",
        r"(?P<TTONBR>\d{3})",
        r"(?P<TKTIND>\w{1})",
        r";",
        r"(?P<SEGNBR>\d{3})",
        r"HHL",
        r" ",
        r"(?P<AIRCDE>\w{2,4})",
        r" ",
        r"(?P<STATUS>\w{2})",
        r"(?P<NBRRMS>\d{2})",
        r";",
        r"(?P<PNRSTAT>\w{4})",
        r" ",
        r"(?P<INDTE>\w{5})",
        r";",
        r"(?P<OUTDTE>\w{5})",
        r";",
        r"(?P<AIRPT>\w{0,5})",
        r";",
        r"(?P<CDETRAN>[\w,\s]{0,17})",
        r";",
        r"(?P<SIPPRM>\d{1})",
        r"(?P<SIPPRM_CodAph>.{0,6})",
        r";",
        r"(?P<RATEIND>.{0,1})",
        r";",
        r"(?P<CURRCDE>\w{3})",
        r"(?P<LCURRCDE>\w{3})",
        r";",
        r"(?P<ROOMRTE>[\d,.]{2,10})",
        r"\+",
        r"(?P<DATERTE>\w{5})",
        r"\+",
        r"(?P<RATEPER>\d{2})",
        r".*CF-(?P<PNRRMK_DadCnf>\w+);"
        r".*;FM-;",
        r"G-(?P<GUOPT>\w{0,31})",
        r";",
        r".*;SF-;\*\*-;",
        r"(?P<HTLNME>[\w,\s,\*]{0,40})",
        r";",
        r".*",
        r"TTL-BRL(?P<TOTRT_Number>[\d,.]{2,10});",
    )


class MUC1A(Processor):
    detect = r"^MUC1A "
    keys = (
        (
            ("CTYID", 3),
            ("AIRCDE", 3),
            ("RECLOC", 6),
            ("PNRENV", 3),
        ),
        (
            ("TOTPSG", 2),
            ("AIRPSG", 2),
            ("NHPNR", 1),
        ),
        "IDBKG",
        "BKGAGCY",
        "IDFIRST",
        "OWNAGY",
        "IDENTCO",
        "CURAGCY",
        "IDENTT",
        "TKTAGCY",
        "OFFID",
        "CPNID",
        "IDENTT2",
        "TKTAGCY2",
        "OFFID2",
        "CPNID2",
        "IDENTT3",
        "TKTAGCY3",
        "OFFID3",
        "CPNID3",
        "IDENTT4",
        "TKTAGCY4",
        "OFFID4",
        "CPNID4",
        "IDENTT5",
        "TKTAGCY5",
        "OFFID5",
        "CPNID5",
        "ACCTNUM",
        "ORDNUM",
        "ERSP",
        (
            ("NSPNR", 28),
            ("NSAIR", 3),
            ("NSRECLOC", 6),
        ),
    )


class C(Processor):
    keysre = r"^" \
        r"(?P<MSGTAG>.{2})" \
        r"(?P<SVCCAR>\w{4})" \
        r"(?P<TKTIND>.{1})" \
        r" " \
        r"(?P<BKAGT>[\w,\s]{1,8})" \

# r"-" \
# r"(?P<TKTAGT>[\w,\s]{1,8})" \
# r"-" \
# r"(?P<PRCDE>.{1})" \
# r"-" \
# r"(?P<FCMI>\w{1})" \
# r"(?P<JRNYTYPE>\w{4})" \
# r"(?P<JRNYCODE>\w{4})" \
# r"(?P<PSURCHG>\w{4})"


def get_all_subclasses(cls):
    all_subclasses = []
    direct_subclasses = cls.__subclasses__()
    all_subclasses.extend(direct_subclasses)
    for subclass in direct_subclasses:
        all_subclasses.extend(get_all_subclasses(subclass))
    return all_subclasses


PROCESSORS = get_all_subclasses(Processor)
