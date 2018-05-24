from rest_framework.exceptions import APIException


class NoRateFoundException(APIException):
    status_code = 404
    default_detail = 'No rate found for the given range'
    default_code = 'not_found'


class InvalidRangeException(APIException):
    status_code = 400
    default_detail = 'The specified range is invalid. Ensure start time is before end time'
    default_code = 'bad_request'
