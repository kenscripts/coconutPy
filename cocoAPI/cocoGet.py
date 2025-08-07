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


   def requestJson(
                   self,
                   get_endpoint
                   ):
      return self._get(
                       endpoint = get_endpoint
                       )


   def requestFields(
                     self,
                     get_endpoint
                     ):
      return self._get(
                       endpoint = get_endpoint
                       )["data"]["fields"]
