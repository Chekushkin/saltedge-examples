from SaltEdge import SaltEdge
import json

app = SaltEdge('client-id', 'service-secret', 'private.pem', 'public.pem')

url = 'https://www.saltedge.com/api/v2/customers/'
payload = json.dumps({"data":{"identifier":"some_uniq_identifier"}})
response = app.post(url, payload)
data = response.json()
print data