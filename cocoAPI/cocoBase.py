class cocoBase:
   def __init__(
                self,
                cocoLog
                ):

      # login attributes
      self.session = cocoLog.session
      self.api_url = cocoLog.api_url

      # login check
      if not cocoLog.token:
         raise RuntimeError(
                            "Authentication required. Please log in using cocoLog"
                            )


   def _get(
            self,
            endpoint,
            params = None
            ):
      url = f"{self.api_url}/{endpoint}"
      res = self.session.get(
                             url = url,
                             params = params
                             )
      res.raise_for_status()
      return res.json()


   def _post(
             self,
             endpoint,
             json_body = None
             ):
      url = f"{self.api_url}/{endpoint}"
      res = self.session.post(
                              url = url,
                              json = json_body
                              )
      res.raise_for_status()
      return res.json()
