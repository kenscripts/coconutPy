from cocoAPI.cocoBase import cocoBase


class cocoSearch(
                 cocoBase
                 ):
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)


   def allRecords(
                  self,
                  resource,
                  pg_limit = 25
                  ):
      # request json 
      all_collection_req = {
                            "search": {
                                       "filters": [],
                                       "page": 1,
                                       "limit": pg_limit
                                       }
                            }
      # request data
      all_collection_data = self._paginateData(
                                               endpoint = f"{resource}/search",
                                               json_body = all_collection_req
                                               )
      return all_collection_data
