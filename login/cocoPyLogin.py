import requests
from typing import Optional, Dict, Any
API_BASE = "https://coconut.naturalproducts.net/api"


class cocoLog:
    def __init__(
                 self
                 ):
       self.api_url = API_BASE.rstrip("/")
       self.session = requests.Session()
       self.logSession = None
       self.token = None
    def login(
              self,
              email,
              password
              ) -> Dict[str, Any]:
       """
       Log in to the COCONUT API and return the response JSON.
       On success, stores the token and sets the Authorization header.
       """
       login_post = f"{self.api_url}/auth/login"
       login_json = {
                     "email" : email,
                     "password" : password
                     }
       self.logSession = self.session.post(
                                           url = login_post,
                                           json = login_json
                                           )
       self.logSession.raise_for_status() # check
       self.token = self.logSession.json().get(
                                               "access_token"
                                               )
       if self.token:
          self.session.headers.update(
                                      {
                                       "Authorization": f"Bearer {self.token}"
                                       }
                                      )
    def logout(
               self
               ) -> Dict[str, Any]:
       """
       Log out from the COCONUT API. Returns the response JSON.
       Clears stored token and Authorization header.
       """
       if not self.token:
          raise RuntimeError("not logged in")
       logout_get = f"{self.api_url}/auth/logout"
       self.logSession = self.session.get(
                                          url = logout_get
                                          )
       self.logSession.raise_for_status() # check
       self.session.headers.pop(
                                "Authorization",
                                None
                                )
       self.token = None
