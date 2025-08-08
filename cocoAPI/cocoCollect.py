from cocoAPI.cocoBase import cocoBase
from cocoAPI.default_search_requests import default_collections_search_req

class cocoCollect(
                  cocoBase
                  ):
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)

      # request attributes
      self.default_search_req = default_collections_search_req


   def collectionSearch(
                        self,
                        collection_query
                        ):
      """
      Performs COCONUT collection search and returns the json response.
      """
      # validate dtype
      if not isinstance(
                        collection_query,
                        dict
                        ):
         raise TypeError(
                         "collection_query must be a dictionary of field:value."
                         )
      # validate length
      if len(collection_query) != 1:
         raise ValueError(
                          "collection_query must contain exactly one field:value pair."
                          )
      # validate keys
      field = list(
                   collection_query.keys()
                   )[0]
      if field not in self.collection_search_fields:
         raise KeyError(
                        f"{field} is not a valid field. Valid fields are: {self.collection_search_fields}"
                        )
      # build search query
      self.collection_search_req = self.create_collectionSearch_req(
                                                                    collection_query
                                                                    )
      # execute search query
      return self._paginateData(
                                endpoint = "collections/search",
                                json_body = self.collection_search_req
                                )


   def create_collectionSearch_req(
                                   self,
                                   collection_query
                                   ):
      """
      Converts collection_query to json for COCONUT collection search.
      """
      field = list(collection_query.keys())[0]
      collection_search_req = {
                               "search": {
                                          "filters": [
                                                      {
                                                       "field" : field,
                                                       "operator" : "=",
                                                       "value" : collection_query[field]
                                                       }
                                                      ]
                                          }
                               }

      return collection_search_req
