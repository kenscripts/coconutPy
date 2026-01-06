import requests
API_BASE = "https://coconut.naturalproducts.net/api"


class cocoLog:
    def __init__(
                 self
                 ):
       self.api_url = API_BASE.rstrip("/")
       self.session = requests.Session()
       self.logSession = None # store json response
       self.token = None


    def login(
              self,
              email,
              password
              ):
       """
       Log in to the COCONUT API and return the response JSON.
       On success, stores the token and sets the Authorization header.

       Parameters
       ----------
       email
         Email address for COCONUT account
       password
         Password for COCONUT account

       Returns
       -------
       dict
         JSON response from the COCONUT API.
       """
       # build login request
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
               ):
       """
       Log out from the COCONUT API. Returns the response JSON.
       Clears stored token and Authorization header.
       """
       # validate login
       if not self.token:
          raise RuntimeError("not logged in")

       # initiate logout
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
