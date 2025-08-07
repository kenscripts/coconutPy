from cocoAPI.cocoBase import cocoBase

class cocoOrg(
              cocoBase
              ):
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)

      # request attributes
      self.default_search_req = {}


   def organismSearch(
                      self,
                      organism_query
                      ):
      """
      Performs COCONUT organism search and returns the json response.
      """

      # validate dtype
      if not isinstance(
                        organism_query,
                        dict
                        ):
         raise TypeError(
                         "organism_query must be a dictionary of field:value."
                         )

      # validate length
      if len(organism_query) != 1:
         raise ValueError(
                          "organism_query must contain exactly one field:value pair."
                          )

      # validate keys
      field = list(
                   organism_query.keys()
                   )[0]
      if field not in self.organism_search_fields:
         raise KeyError(
                        f"{field} is not a valid field. Valid fields are: {self.organism_search_fields}"
                        )

      # build search query
      self.organism_search_json = self.create_organismSearch_req(
                                                                 organism_query
                                                                 )
 
      # execute search query
      return self._post(
                        endpoint = "organisms/search",
                        json_body = self.organism_search_json
                        )


   def create_organismSearch_req(
                                 self,
                                 organism_query
                                 ):
      """
      Converts organism_query to json for COCONUT organism search.
      """

      field = list(organism_query.keys())[0]
      organism_search_json = {
                              "search": {
                                         "filters": [
                                                     {
                                                      "field" : field,
                                                      "operator" : "=",
                                                      "value" : organism_query[field]
                                                      }
                                                     ]
                                         }
                              }

      return organism_search_json
