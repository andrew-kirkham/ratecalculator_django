# /usr/bin/python
from rest_framework.exceptions import APIException


class NoRateFoundException(APIException):
    """
    404 exception for no rates found
    """

    status_code = 404
    default_detail = 'No rate found for the given range'
    default_code = 'not_found'


class InvalidRangeException(APIException):
    """
    400 exception for an invalid range from the user
    """

    status_code = 400
    default_detail = 'The specified range is invalid. Ensure start time is before end time'
    default_code = 'bad_request'
