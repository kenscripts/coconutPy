from cocoAPI.cocoBase import cocoBase
from cocoAPI.default_search_requests import default_molecule_search_req


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
      self.default_search_req = default_molecule_search_req


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
      self.molecule_search_req = self.create_moleculeSearch_req(
                                                                molecule_query
                                                                )

      # execute search query
      return self._paginateData(
                                endpoint = "molecules/search",
                                json_body = self.molecule_search_req
                                )


   def create_moleculeSearch_req(
                                 self,
                                 molecule_query
                                 ):
      """
      Converts molecule_query to json for COCONUT molecule search.
      """

      field = list(molecule_query.keys())[0]
      molecule_search_req = {
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

      return molecule_search_req


   def get_allMolecules(self):
      """
      Retrieves data for all COCONUT molecules.
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
            print(
                  f"Warning: Empty data returned on page {curr_pg}. Pagination stoppedy."
                  )
            break
         all_molecule_data.extend(
                                  pg_data
                                  )

         # progress
         last_pg  = all_molecule_json["last_page"]
         if curr_pg == last_pg:
            break
         curr_pg += 1

      return all_molecule_data
