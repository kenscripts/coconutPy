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

      # search attributes
      self.collection_request_json = {}
      self.get_collectionRequest_json() # run automatically


   def get_collectionRequest_json(
                                  self
                                  ):
      """
      Fetches /collection metadata (e.g. search fields).
      Automatically run once cocoCollect is created.
      """

      self.collection_request_json = self._get(
                                               endpoint = "collections"
                                               )

      self.collection_search_fields = self.collection_request_json["data"]["fields"]


   def collectSearch(
                     self,
                     collection_query
                     ):
      """
      Posts to /molecules/search and returns the json response.
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
      field = list(collection_query.keys())[0]
      if field not in self.collection_search_fields:
         raise KeyError(
                        f"Field {collection_query.items()} is not valid. Valid fields are: {self.collection_search_fields}"
                        )

      # build and execute search query
      collection_search_json = self.create_collectSearch_req(
                                                             collection_query
                                                             )
 
      # allows for multiple searches with class instance
      return self._post(
                        endpoint = "collections/search",
                        json_body = collection_search_json
                        )

   def create_collectSearch_req(
                                self,
                                collection_query
                                ):
      """
      Formats collection_query for COCONUT molecule search,
      with molecule properties included.
      """

      field = list(collection_query.keys())[0]
      search_json = {
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

      return search_json


   def get_all_collections(self):
      endpoint = f"{self.api_url}/collections/search"
      all_data = []
      page = 1
      limit = 50
  
      while True:
         payload = {
                    "search": {
                               "filters": [],
                               "page": page,
                               "limit": limit
                               }
                    }

         res = self.session.post(url=endpoint, json=payload)
         res.raise_for_status()
         res_json = res.json()

         page_data = res_json.get("data", [])
         if not page_data:
            break
 
         all_data.extend(page_data)
 
         total = res_json.get("total", len(all_data))
         if page * limit >= total:
            break
 
         page += 1

      return all_data

