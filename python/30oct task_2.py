# Convert to Dict JSON Response and Print and Booking Id
# AND checkin and Checkout Data
import json

api_response = {
            "bookingid": 2384,
            "booking": {
                        "firstname": "PRAMOD",
                        "lastname": "Dutta",
                        "totalprice": 432,
                         "depositpaid": False,
                         "bookingdates": {
                                "checkin": "2022-01-01",
                                "checkout": "2022-01-01"
                                        },
                        "additionalneeds": "Lunch"
                         }
            }
print(api_response)
print(type(api_response))
print(api_response.get('bookingid'))
print(api_response['booking']['bookingdates'])
b=json.dumps(api_response)
print(b)
print(type(b))
