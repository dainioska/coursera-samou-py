import sys
import requests

url = sys.argv[1]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

except requests.Timeout:
    print("klaida timeout, url: ", url)
except requests.HTTPError as err:
    code = err.response.status_code
    print("klaida url: {0}, code: {1}".format(url, code))
except requests.RequestException:
    print("klaida  del ulr: ", url)
else:    
    print(response.content)

