# coding: utf-8

from django.core.files import File
from django.test import TestCase

from .models import Processing


class ConsistencyTestCase(TestCase):

    def setUp(self):
        self.iea_filepath = "core/assets/15148200.iea"
        self.air_filepath = "core/assets/15148200.JUL"
        self.pro = pro = Processing()
        pro.air_file.save("15148200.JUL",
                          File(open(self.air_filepath)))
        pro.reprocess()

    def tearDown(self):
        self.pro.air_file.delete()

    def test_iea_codfop(self):
        self.assertEqual(self.pro.iea_CodFop, "CC")
        self.assertEqual(self.pro.iea_NumCcr, "AX376433680911004")

    def test_iea_autcli(self):
        self.assertEqual(self.pro.iea_AutCli, "DIRETORIA EAESP")

    def test_iea_ccupax(self):
        self.assertEqual(self.pro.iea_CcuPax, "018.006.001.00029")

    def test_iea_taxfor(self):
        self.assertEqual(self.pro.iea_TaxFor, "TX2060/")

    def test_iea_dadcnf(self):
        self.assertEqual(self.pro.iea_DadCnf, "98670348")

    def test_iea_forrep(self):
        self.assertEqual(self.pro.iea_ForRep, 12345)

    def test_iea_agtrsv(self):
        self.assertEqual(self.pro.generate_iea_file_contents().split(";"),
                         open(self.iea_filepath).read().split(";"))
