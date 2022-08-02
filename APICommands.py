import requests
import json
# Verify actual response and expected response are match
# input values Base url, End point, Response
def endpoint_response(base_url, relative_url, expected_response):
    actual_response = requests.get(base_url + relative_url)
    if actual_response.status_code == expected_response:
        print("PASS : Actual response is equal to expected response i.e., {}".format(expected_response))
        return actual_response
    else:
        print("FAIL : Actual response {} don't match with expected response {}".format(actual_response.status_code,
                                                                                       expected_response))
        return "FAIL"

# Verify actual Content_type and expected ContentType 
# Input values return value of endpoint_response, Media type
def verify_content_type(response, media_type):
    if response.headers['Content-Type'].count(media_type) != 1:
        print("FAIL : Actual Content-Type {} is not equal to expected media type i.e., {}".format(
            response.headers['Content-Type'], media_type))
        return "FAIL"
    else:
        print("PASS: Actual Content-Type is equal to expected media type i.e., {}".format(media_type))
        return "PASS"

# Verify the param are as expected
# Input values return value of endpoint_response, UDI / Device Identifier,UDI / Production Identifier,Part Number (PN),Sub-Components Name, Sub-Components Name
def verify_params(response, expected_pname, expected_di, expected_pi, expected_pn, expected_name, expected_name2):
    params = response.json();
    for temp in params:
        if temp['Product Name'] == expected_pname:
            if temp['UDI / Device Identifier'] == expected_di:
                print("PASS: Expected UDI / Device Identifier is equal to expected Device Identifier i.e., {}".format(
                    expected_di))
            else:
                print(
                    "FAIL : Expected UDI / Device Identifier {} is not equal to expected Device Identifier i.e., {}".format(
                        temp['UDI / Device Identifier'], expected_di))
            if temp['UDI / Production Identifier']['Version'] == expected_pi:
                print(
                    "PASS: Expected UDI / Production Identifier is equal to expected Production Identifier i.e., {}".format(
                        expected_pi))
            else:
                print(
                    "FAIL : Expected UDI / Production Identifier {} is not equal to expected Production Identifier i.e., {}".format(
                        temp['UDI / Production Identifier']['Version'], expected_pi))
            if temp['UDI / Production Identifier']['Part Number (PN)'] == expected_pn:
                print(
                    "PASS: Expected UDI / Part Number (PN) is equal to expected Production Identifier i.e., {}".format(
                        expected_pn))
            else:
                print(
                    "FAIL : Expected UDI / Part Number (PN) {} is not equal to expected Production Identifier i.e., {}".format(
                        temp['UDI / Production Identifier']['Part Number (PN)'],
                        expected_pn))
            if temp['UDI / Production Identifier']['Sub-Components'][0]['Name'] == expected_name:
                print("PASS: Expected Sub-Components Name is equal to expected Production Identifier i.e., {}".format(
                    expected_name))
            else:
                print(
                    "FAIL : Expected Sub-Components Name {} is not equal to expected Production Identifier i.e., {}".format(
                        temp['UDI / Production Identifier']['Sub-Components'][0]['Name'],
                        expected_name))
            if temp['UDI / Production Identifier']['Sub-Components'][0]['Name'] == expected_name2:
                print("PASS: Expected Sub-Components Name is equal to expected Production Identifier i.e., {}".format(
                    expected_name2))
            else:
                print(
                    "FAIL : Expected Sub-Components Name {} is not equal to expected Production Identifier i.e., {}".format(
                        temp['UDI / Production Identifier']['Sub-Components'][0]['Name'],
                        expected_name2))

