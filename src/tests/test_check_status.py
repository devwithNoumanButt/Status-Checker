import pytest
from Status_checker.check_status import check_status

def test_check_status():
    "Test the check status functionality on google.com"

    status_code = check_status('https://www.google.com')

    assert status_code == 200