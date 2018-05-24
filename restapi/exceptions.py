from rest_framework.exceptions import APIException


class NoRateFoundException(APIException):
    status_code = 404
    default_detail = 'No rate found for the given range'
    default_code = 'not_found'
