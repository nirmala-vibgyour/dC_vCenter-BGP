# BGP Verification via AVI Load Balancer API

This script retrives the **BGP_Profile** through the **/api/vrfcontext** endpoint, thus verifying the BGP settings as found using the same API endpoint, found using **Developer Tools**. 

---

## Objective

- Use the API to confirm BGP configuration: `shutdown`, `local_as`, `ibgp`, and `cloud_ref`.

---

## Requirements

- Python 3.7+
- `requests`, `python-dotenv`, `urllib3` and `os`
- `.env` file with session and environment config
- Access to AVI Load Balancer Controller (e.g., `https://35.200.176.139/`)

---

## Constraints

- No Real BGP Peering Possible
Since the dummy vCenter cloud uses fake values and has no real upstream peer routers, enabling BGP in VRF context results only in a logical configuration — no actual BGP session.

- Dummy vCenter Credentials Cannot Simulate Real Integration
While trying to save a dummy vCenter cloud in the UI, due to backend validation (e.g., during API POST) the connection is failing while using IPs like: 192.0.2.10, 192.0.2.11 or 198.51.100.10 ( the controller is attempting to authenticate or resolve resources)
