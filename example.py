import requests
import datetime
import time
import uuid
from requests.packages import urllib3
urllib3.disable_warnings()

api_url = "https://api.letusorder.it/v1/"

s = requests.Session()
s.verify = False

order_data = {
    "slug": "pizza-stupig-9-1-2015-" + uuid.uuid4().hex[:6],
    "master": "tw@example.com",
    "description": "Pizza Domingo 9.1.15",
    "deadline": (datetime.datetime.now() + datetime.timedelta(days=1)).isoformat(),
}
r = s.post(api_url + "orders/", data=order_data)
order = r.json()
print(order)

# because throttling
time.sleep(1)

## orderitem

orderitem_data = {
    "slug": uuid.uuid4(),
    "user_email": "jarus@example.com",
    "item_identifier": "große Schinken/Pilze/Paprika-Pizza",
    "count": 1,
    "amount": 1050,
    "order": order.get('id')
}
r = s.post(api_url + "orderitems/", data=orderitem_data)
orderitem = r.json()

print(orderitem)
