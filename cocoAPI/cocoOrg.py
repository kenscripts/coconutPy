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
      self.get_organismRequestJson() # run automatically
      self.default_search_req = {}


   def get_organismRequestJson(
                               self
                               ):
      """
      GET method for COCONUT organisms resource.
      """
      self.organism_get_json = self._get(
                                         endpoint = "organisms"
                                         )

      self.organism_search_fields = self.organism_get_json["data"]["fields"]


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


   def get_allOrganisms(self):
      """
      Retrieves information for all COCONUT organisms.
      """
      # page info
      curr_pg = 1
      limit = 50
  
      all_organism_data = []
      while True:
         # request
         all_organism_req = {
                             "search": {
                                        "filters": [],
                                        "page": curr_pg,
                                        "limit": limit
                                        }
                             }
         all_organism_json = self._post(
                                        endpoint = "organisms/search",
                                        json_body = all_organism_req
                                        )

         # data
         pg_data = all_organism_json.get(
                                         "data",
                                         []
                                         )
         if not pg_data:
            break
         all_organism_data.extend(
                                  pg_data
                                  )

         # progress
         total = all_organism_json.get(
                                       "total",
                                       len(all_organism_data)
                                       )
         if curr_pg * limit >= total:
            break
         curr_pg += 1

      return all_organism_data
