import json
from dicttoxml import dicttoxml
from restapi.views import RateQuery
from django.test import TestCase

class TimeRangeTest(TestCase):

    def test_post_json(self):
        data = {'start': '2015-07-01T07:00:00Z', 'end': '2015-07-01T12:00:00Z'}
        response = self.client.post(
            '/api/rate/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,  200)
        self.assertTrue(response.json, 1750)

    def test_post_xml(self):
        data = {'start': '2015-07-01T07:00:00Z', 'end': '2015-07-01T12:00:00Z'}
        response = self.client.post(
            '/api/rate/', data=dicttoxml(data), content_type='application/xml')
        self.assertEqual(response.status_code,  200)
        self.assertTrue(response.json, 1750)

    def test_post_invalid_data(self):
        data = {'start': '2015-07-01T07:00:00Z'}
        response = self.client.post(
            '/api/rate/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,  400)

    def test_post_invalid_data_not_times(self):
        data = {'start': 'abc123', 'end': 'abc123'}
        response = self.client.post(
            '/api/rate/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,  400)

    def test_post_missing_range(self):
        data = {'start': '2015-07-01T01:00:00Z', 'end': '2015-07-01T12:00:00Z'}
        response = self.client.post(
            '/api/rate/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code,  404)

    def test_get(self):
        data = {'start': '2015-07-01T07:00:00Z', 'end': '2015-07-01T12:00:00Z'}
        response = self.client.get('/api/rate/', data=data)
        self.assertEqual(response.status_code,  200)
        self.assertTrue(response.json, 1750)

    def test_get_invalid_data(self):
        data = {'start': '2015-07-01T07:00:00Z'}
        response = self.client.get(
            '/api/rate/', data=data, content_type='application/json')
        self.assertEqual(response.status_code,  400)

    def test_get_missing_range(self):
        data = {'start': '2015-07-01T01:00:00Z', 'end': '2015-07-01T12:00:00Z'}
        response = self.client.get(
            '/api/rate/', data=data, content_type='application/json')
        self.assertEqual(response.status_code,  404)
