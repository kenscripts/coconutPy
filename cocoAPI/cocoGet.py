from cocoAPI.cocoBase import cocoBase

class cocoGet(
              cocoBase
              ):
   """
   Class for COCONUT get requests.
   """
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)


   def resourceJson(
                    self,
                    resource_endpoint
                    ):
      return self._get(
                       endpoint = resource_endpoint
                       )


   def resourceFields(
                      self,
                      resource_endpoint
                      ):
      return self._get(
                       endpoint = resource_endpoint
                       )["data"]["fields"]
