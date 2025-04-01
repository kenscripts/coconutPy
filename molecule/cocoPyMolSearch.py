from typing import Dict, Any
from login.cocoPyLogin import cocoLog  # import the login class

class cocoMolSearch:
        def __init__(self, api: cocoLog):
                    if not api.token:
                                    raise RuntimeError("cocoLog instance is not authenticated.")
                                        self.session = api.session
                                                self.api_url = api.api_url

                                                    def search(self, criteria: Dict[str, Any]) -> Dict[str, Any]:
                                                                search_url = f"{self.api_url}/molecules/search"
                                                                        response = self.session.post(url=search_url, json=criteria)
                                                                                response.raise_for_status()
                                                                                        return response.json()



# get all search fields
# pass search fields to function
# let user construct their own query
# rest of fields remain blank or are not included
