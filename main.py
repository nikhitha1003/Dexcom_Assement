
from APICommands import verify_content_type, verify_params, endpoint_response

baseURL = "https://api.dexcom.com"
relativeURL = "/info"
e_response = 200
e_pname = 'Dexcom API'
e_di = '00386270000668'
e_pi = '3.1.0.0'
e_pn = "350-0019"
e_name = "api-gateway"
e_name2 = "insulin-service"

a_response = endpoint_response(baseURL, relativeURL, e_response)
if a_response != "FAIL":
    if verify_content_type(a_response, 'json') != "FAIL":
        verify_params(a_response, e_pname, e_di, e_pi, e_pn, e_name, e_name2)
if a_response != "FAIL":
    verify_content_type(a_response, 'xml')
baseURL = "https://sandbox-api.dexcom.com"
print("Next set.......................................................................................................")
a_response = endpoint_response(baseURL, relativeURL, e_response)
if a_response != "FAIL":
    if verify_content_type(a_response, 'json') != "FAIL":
        verify_params(a_response, e_pname, e_di, e_pi, e_pn, e_name, e_name2)
if a_response != "FAIL":
    verify_content_type(a_response, 'xml')
