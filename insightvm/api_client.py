import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

class InsightVMClient:
    def __init__(self):
        self.base_url = settings.INSIGHTVM_CONFIG['BASE_URL']
        self.auth = HTTPBasicAuth(
            settings.INSIGHTVM_CONFIG['USERNAME'],
            settings.INSIGHTVM_CONFIG['PASSWORD']
        )
        self.session = requests.Session()
        self.session.auth = self.auth
        self.session.headers.update({'Content-Type': 'application/json'})

    def get_sites(self):
        response = self.session.get(f"{self.base_url}/sites")
        response.raise_for_status()
        return response.json()['resources']

    def get_site_details(self, site_id):
        response = self.session.get(f"{self.base_url}/sites/{site_id}")
        response.raise_for_status()
        return response.json()

    def get_site_assets(self, site_id):
        response = self.session.get(f"{self.base_url}/sites/{site_id}/assets")
        response.raise_for_status()
        return response.json()['resources']
    
    def get_asset_vulnerabilities(self, asset_id):
        response = self.session.get(f"{self.base_url}/assets/{asset_id}/vulnerabilities")
        response.raise_for_status()
        return response.json()['resources']
    
    # Add more methods as needed
