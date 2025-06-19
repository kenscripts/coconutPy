from cocoAPI.cocoBase import cocoBase

class cocoMol(
              cocoBase
              ):
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)

      # request attributes
      self.get_moleculeRequestJson() # run automatically


   def get_moleculeRequestJson(
                               self
                               ):
      """
      GET method for COCONUT molecules resource.
      """
      self.molecule_get_json = self._get(
                                         endpoint = "molecules"
                                         )
      self.molecule_search_fields = self.molecule_get_json["data"]["fields"]


   def moleculeSearch(
                      self,
                      molecule_query
                      ):
      """
      Performs COCONUT molecule search and returns the json response.
      """

      # validate dtype
      if not isinstance(
                        molecule_query, 
                        dict
                        ):
         raise TypeError(
                         "molecule_query must be a dictionary of field:value."
                         )

      # validate length
      if len(molecule_query) != 1:
         raise ValueError(
                          "molecule_query must contain exactly one field:value pair."
                          )

      # validate keys
      field = list(
                   molecule_query.keys()
                   )[0]
      if field not in self.molecule_search_fields:
         raise KeyError(
                        f"{field} is not a valid field. Valid fields are: {self.molecule_search_fields}"
                        )

      # build search query
      self.molecule_search_json = self.create_moleculeSearch_req(
                                                                 molecule_query
                                                                 )

      # execute search query
      return self._post(
                        endpoint = "molecules/search",
                        json_body = self.molecule_search_json
                        )


   def create_moleculeSearch_req(
                                 self,
                                 molecule_query
                                 ):
      """
      Converts molecule_query to json for COCONUT molecule search.
      """

      field = list(molecule_query.keys())[0]
      molecule_search_json = {
                              "search": {
                                         "filters": [
                                                     {
                                                      "field" : field,
                                                      "operator" : "=",
                                                      "value" : molecule_query[field]
                                                     }
                                                    ],
                                         "includes": [
                                                      {
                                                       "relation": "properties"
                                                      }
                                                     ]
                                        }
                              }

      return molecule_search_json


   def get_allCollections(self):
      """
      Retrieves information for all COCONUT molecules.
      """
      # page info
      curr_pg = 1
      limit = 50

      all_molecule_data = []
      while True:
         # request
         all_molecule_req = {
                             "search": {
                                        "filters": [],
                                        "page": curr_pg,
                                        "limit": limit
                                        }
                             }
         all_molecule_json = self._post(
                                        endpoint = "molecules/search",
                                        json_body = all_molecule_req
                                        )

         # data
         pg_data = all_molecule_json.get(
                                         "data",
                                         []
                                         )
         if not pg_data:
            break
         all_molecule_data.extend(
                                  pg_data
                                  )

         # progress
         total = all_molecule_json.get(
                                       "total",
                                       len(all_molecule_data)
                                       )
         if curr_pg * limit >= total:
            break
         curr_pg += 1

      return all_molecule_data
