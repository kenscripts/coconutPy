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

      # molSearch attributes
      self.mol_res = {}
      self.mol_search_fields = []
      self.get_molResponse() # run automatically


   def get_molResponse(
                       self
                       ):
      """
      Fetches /molecules metadata (e.g. search fields).
      Stores the response and a list of available search fields.
      Automatically run once cocoMol is created.
      """

      self.mol_res = self._get(
                               endpoint = "molecules"
                               )
      self.mol_search_fields = self.mol_res["data"]["fields"]


   def molSearch(
                 self,
                 mol_query
                 ):
      """
      Posts to /molecules/search and returns the json response.
      """

      # validate dtype
      if not isinstance(
                        mol_query, 
                        dict
                        ):
         raise TypeError(
                         "mol_query must be a dictionary of field:value."
                         )

      # validate length
      if len(mol_query) != 1:
         raise ValueError(
                          "mol_query must contain exactly one field:value pair."
                          )

      # validate keys
      field = list(mol_query.keys())[0]
      if field not in self.mol_search_fields:
         raise KeyError(
                        f"Field {mol_query.items()} is not valid. Valid fields are: {self.mol_search_fields}"
                        )

      # build and execute search query
      mol_search_json = self.build_molSearch(
                                             mol_query
                                             )

      # allows for multiple searches with class instance
      return self._post(
                        endpoint = "molecules/search",
                        json_body = mol_search_json
                        )


   def build_molSearch(
                       self,
                       mol_query
                       ):
      """
      Formats mol_query for COCONUT molecule search,
      with molecule properties included.
      """

      field = list(mol_query.keys())[0]
      search_json = {
                     "search": {
                                "filters": [
                                            {
                                             "field" : field,
                                             "operator" : "=",
                                             "value" : mol_query[field]
                                            }
                                           ],
                                "includes": [
                                             {
                                              "relation": "properties"
                                             }
                                            ]
                               }
                    }

      return search_json
