"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Charles Smith
Date:   03 December 2020
"""

import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")

    result = currency.before_space("0.863569 Euros")
    introcs.assert_equals('0.863569',result)

    result = currency.before_space("Hello  Euros")
    introcs.assert_equals('Hello',result)

    result = currency.before_space("0.863569 Euros ")
    introcs.assert_equals('0.863569',result)

    result = currency.before_space(" 0.863569")
    introcs.assert_equals('',result)


def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    result = currency.after_space("0.863569 Euros")
    introcs.assert_equals('Euros',result)

    result = currency.after_space("Hello  Euros")
    introcs.assert_equals(' Euros',result)

    result = currency.after_space("Hello Euros ")
    introcs.assert_equals('Euros ',result)

    result = currency.after_space("HelloEuros ")
    introcs.assert_equals('',result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',result)

    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',result)

    result = currency.first_inside_quotes("'AB' 'BC' \"E\'F\"")
    introcs.assert_equals('E\'F',result)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")

    result = currency.get_src('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)

    result = currency.get_src('{"success":false,"src":  "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")

    result = currency.get_dst('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success":false,"src":"","dst":  "","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)

    result = currency.get_dst('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',result)

    result = currency.get_dst('{"success":false,"src":  "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")
