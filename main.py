from dotenv import load_dotenv
import requests
import os
import urllib3

# Load .env file
load_dotenv()

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Environment variables
controller = os.getenv("ip")
username = os.getenv("username")
password = os.getenv("password")
version = os.getenv("version")
cloud_uuid = os.getenv("cloud_uuid")

# Login to controller
login_url = f'https://{controller}/login'
login_payload = {'username': username, 'password': password}
login_response = requests.post(login_url, json=login_payload, verify=False, timeout=10)

if login_response.status_code != 200:
    print(f"Login failed: {login_response.status_code}")
    print(login_response.text)
    exit()

print("Login successful")

# Extract session cookies
csrftoken = login_response.cookies.get('csrftoken')
sessionid = login_response.cookies.get('sessionid')

if not csrftoken or not sessionid:
    print("CSRF token or session ID missing.")
    exit()

headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken,
    'X-Avi-Version': version,
    'Referer': f'https://{controller}/',
}

cookies = {
    'csrftoken': csrftoken,
    'sessionid': sessionid
}

# Request VRF contexts tied to the cloud
params = {
    "exclude": "name.in",
    "name.in": "management",
    "cloud_ref.uuid": cloud_uuid,
    "sort": "name",
    "page_size": 30,
    "page": 1,
    "include_name": "true",
}

url = f"https://{controller}/api/vrfcontext/"
resp = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False, timeout=10)

if resp.status_code == 200:
    results = resp.json().get("results", [])
    print(f"VRF Entries Found: {len(results)}")
    for vrf in results:
        print("\n--- VRF ---")
        print("Name:", vrf.get("name"))
        print("Cloud Ref:", vrf.get("cloud_ref"))
        bgp = vrf.get("bgp_profile", {})
        print("BGP Shutdown:", bgp.get("shutdown"))
        print("Local AS:", bgp.get("local_as"))
        print("iBGP:", bgp.get("ibgp"))
else:
    print(f"Failed to fetch VRF context: {resp.status_code}")
    print(resp.text)
