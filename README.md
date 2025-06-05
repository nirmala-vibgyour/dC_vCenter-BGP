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
