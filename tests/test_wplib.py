#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path

NUMBER_OF_VALID_COUNTRIES = 249


@pytest.fixture(scope='module')
def csv_file():
    from wpgpDownload.utils.misc import csv_file
    return csv_file()


@pytest.fixture(scope='module')
def csv_signature():
    from wpgpDownload.utils import misc
    return misc.CSV_SIGNATURE


# noinspection SpellCheckingInspection
def test_wplib_builin_md5_signature(csv_file):
    from wpgpDownload.utils.misc import md5_digest
    md5 = md5_digest(csv_file)
    assert md5 == '2f991750498cfc38180a804ace383c06'


# noinspection SpellCheckingInspection
def test_wplib_dl_ftp_md5_signature():
    from wpgpDownload import wpFtp
    ftp = wpFtp()

    assert ftp.csv_signature == '2f991750498cfc38180a804ace383c06'


# noinspection SpellCheckingInspection
def test_wplib_compare_signatures():
    from wpgpDownload import wpFtp
    ftp = wpFtp()

    assert csv_signature() == ftp.csv_signature


# noinspection SpellCheckingInspection
def test_wplib_isos():
    from wpgpDownload import Countries

    c = Countries
    assert len(c) == NUMBER_OF_VALID_COUNTRIES
    assert c.get(531).__repr__() == "Country(numeric='531', alpha3='CUW', name='Curacao')"
    assert c.get('GRC').__repr__() == "Country(numeric='300', alpha3='GRC', name='Greece')"
    assert c.get('United States').__repr__() == "Country(numeric='840', alpha3='USA', name='United States')"


# noinspection SpellCheckingInspection
def test_wplib_dl():
    from wpgpDownload import wpFtp

    ftp = wpFtp()
    assert ftp is not None


# noinspection SpellCheckingInspection
def test_wplib_dl_fail_bad_hostname():
    from wpgpDownload import wpFtp
    server = "ftp.worldpop.org2.uk"

    with pytest.raises(ValueError,
                       match=r'Could not reach FTP server. Please check if FTP server address is correct'):
        ftp = wpFtp(server)
