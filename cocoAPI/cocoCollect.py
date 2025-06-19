from cocoAPI.cocoBase import cocoBase

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
      self.get_collectionRequestJson() # run automatically


   def get_collectionRequestJson(
                                 self
                                 ):
      """
      GET method for COCONUT collections resource.
      """
      self.collection_get_json = self._get(
                                           endpoint = "collections"
                                           )

      self.collection_search_fields = self.collection_get_json["data"]["fields"]


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
      self.collection_search_json = self.create_collectSearch_req(
                                                                  collection_query
                                                                  )
 
      # execute search query
      return self._post(
                        endpoint = "collections/search",
                        json_body = self.collection_search_json
                        )


   def create_collectionSearch_req(
                                   self,
                                   collection_query
                                   ):
      """
      Converts collection_query to json for COCONUT collection search.
      """

      field = list(collection_query.keys())[0]
      collection_search_json = {
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

      return collection_search_json


   def get_allCollections(self):
      """
      Retrieves information for all COCONUT collections.
      """
      # page info
      curr_pg = 1
      limit = 50
  
      all_collection_data = []
      while True:
         # request
         all_collection_req = {
                               "search": {
                                          "filters": [],
                                          "page": curr_pg,
                                          "limit": limit
                                          }
                               }
         all_collection_json = self._post(
                                          endpoint = "collections/search",
                                          json_body = all_collection_req
                                          )

         # data
         pg_data = all_collection_json.get(
                                           "data",
                                           []
                                           )
         if not pg_data:
            break
         all_collection_data.extend(
                                    pg_data
                                    )

         # progress
         total = all_collection_json.get(
                                         "total",
                                         len(all_collection_data)
                                         )
         if curr_pg * limit >= total:
            break
         curr_pg += 1

      return all_collection_data
