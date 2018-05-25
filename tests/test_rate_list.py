# /usr/bin/python

from django.test import TestCase
from restapi.views.rate_list import RateList


rate_list = RateList()

class RateListTest(TestCase):

    def test_rate_list(self):
        response = self.client.get('/api/list/')
        self.assertEquals(200, response.status_code)
        self.assertTrue('rates' in response.json() > 0)
