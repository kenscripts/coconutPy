from cocoAPI.cocoLog import cocoLog

class cocoMol:
   def __init__(
                self,
                cocoLog
                ):
      if not cocoLog.token:
         raise RuntimeError("cocoLog instance is not authenticated.")

      self.session = cocoLog.session
      self.api_url = cocoLog.api_url
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

      mol_get = f"{self.api_url}/molecules"
      mol_get_res = self.session.get(
                                     url = mol_get
                                     )
      mol_get_res.raise_for_status()
      self.mol_res = mol_get_res.json()
      self.mol_search_fields = self.mol_res["data"]["fields"]


   def molSearch(
                 self,
                 mol_query
                 ):
      """
      Posts to /molecules/search and returns the json response.
      """

      if not isinstance(
                        mol_query, 
                        dict
                        ):
         raise TypeError("mol_query must be a dictionary of field:value.")

      if len(mol_query) != 1:
         raise ValueError("mol_query must contain exactly one field:value pair.")

      field = list(mol_query.keys())[0]
      if field not in self.mol_search_fields:
         raise KeyError(
                        f"Field {mol_query.items()} is not valid.Valid fields are: {self.mol_search_fields}"
                        )

      mol_search_post = f"{self.api_url}/molecules/search"
      mol_search_json = self.build_molSearch(
                                             mol_query
                                             )
      mol_search_res = self.session.post(
                                         url = mol_search_post,
                                         json = mol_search_json
                                         )
      mol_search_res.raise_for_status()

      return mol_search_res.json() # allows for multiple searches with class instance


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
