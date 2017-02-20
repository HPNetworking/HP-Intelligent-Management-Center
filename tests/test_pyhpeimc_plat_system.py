# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.system module.

"""

from unittest import TestCase

from pyhpeimc.plat.system import *
from test_machine import auth


class TestGet_system_vendors(TestCase):
    def test_get_system_vendors_type(self):
        vendors = get_system_vendors(auth.creds, auth.url)
        self.assertIs(type(vendors), list)

    def test_get_system_vendors_content(self):
        vendors = get_system_vendors(auth.creds, auth.url)
        self.assertIs(len(vendors[0]), 8)
        self.assertIn('link', vendors[0])
        self.assertIn('preDefined', vendors[0])
        self.assertIn('name', vendors[0])
        self.assertIn('contact', vendors[0])
        self.assertIn('iconId', vendors[0])
        self.assertIn('id', vendors[0])
        self.assertIn('description', vendors[0])
        self.assertIn('phone', vendors[0])


# get_system_category
class TestGet_system_category(TestCase):
    def testGet_system_category_type(self):
        categories = get_system_category(auth.creds, auth.url)
        self.assertIs(type(categories), list)

    def testGet_system_category_content(self):
        categories = get_system_category(auth.creds, auth.url)
        self.assertIs(len(categories[0]), 9)
        self.assertIn('link', categories[0])
        self.assertIn('topoIconId', categories[0])
        self.assertIn('preDefined', categories[0])
        self.assertIn('name', categories[0])
        self.assertIn('iconId', categories[0])
        self.assertIn('id', categories[0])
        self.assertIn('isDefaultDisplay', categories[0])
        self.assertIn('displayId', categories[0])
        self.assertIn('priority', categories[0])


# get_system_device_models
class TestGet_system_device_models(TestCase):
    def test_get_system_device_models_type(self):
        device_models = get_system_device_models(auth.creds, auth.url)
        self.assertIs(type(device_models), list)

    def test_get_system_device_models_content(self):
        device_models = get_system_device_models(auth.creds, auth.url)
        self.assertIs(len(device_models[0]), 14)
        self.assertIn('sysOid', device_models[0])
        self.assertIn('preDefined', device_models[0])
        self.assertIn('name', device_models[0])
        self.assertIn('categoryId', device_models[0])
        self.assertIn('defaultTopoIconId', device_models[0])
        self.assertIn('deviceVersion', device_models[0])
        self.assertIn('description', device_models[0])
        self.assertIn('defaultIconId', device_models[0])
        self.assertIn('seriesId', device_models[0])
        self.assertIn('dfield', device_models[0])
        self.assertIn('link', device_models[0])
        self.assertIn('id', device_models[0])
        self.assertIn('virtualDeviceName', device_models[0])
        self.assertIn('applicationName', device_models[0])


# get_system_series
class TestGet_system_series(TestCase):
    def test_get_system_series_type(self):
        series = get_system_series(auth.creds, auth.url)
        self.assertIs(type(series), list)

    def test_get_system_series_content(self):
        series = get_system_series(auth.creds, auth.url)
        self.assertIs(len(series[0]), 6)
        self.assertIn('link', series[0])
        self.assertIn('preDefined', series[0])
        self.assertIn('name', series[0])
        self.assertIn('id', series[0])
        self.assertIn('vendorId', series[0])
        self.assertIn('description', series[0])


# Section deals with device authentication templates. Get and Set functions available apply to
# IMC 7.3 and later

class TestGet_Telnet_Template(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_telnet_template_type(self):
        template = get_telnet_template(auth.creds, auth.url)
        self.assertIs(type(template), list)

    def test_get_telnet_template_content(self):
        template = get_telnet_template(auth.creds, auth.url)
        self.assertIn('id', template[0])
        self.assertIn('type', template[0])
        self.assertIn('name', template[0])
        self.assertIn('authType', template[0])
        self.assertIn('userName', template[0])
        self.assertIn('userPassword', template[0])
        self.assertIn('superPassword', template[0])
        self.assertIn('authTypeStr', template[0])
        self.assertIn('timeout', template[0])
        self.assertIn('retries', template[0])
        self.assertIn('port', template[0])
        self.assertIn('version', template[0])
        self.assertIn('creator', template[0])
        self.assertIn('accessType', template[0])
        self.assertIn('operatorGroupStr', template[0])
        self.assertIn('link', template[0])


