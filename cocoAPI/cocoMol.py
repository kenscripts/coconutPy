from cocoAPI.cocoBase import cocoBase
from cocoAPI.default_search_requests import default_molecule_search_req
import copy


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
      self.default_molecule_search_req = default_molecule_search_req


#   def moleculeSearch(
#                      self,
#                      molecule_query
#                      ):
#      """
#      Performs COCONUT molecule search and returns the json response.
#      """
#
#      # validate dtype
#      if not isinstance(
#                        molecule_query, 
#                        dict
#                        ):
#         raise TypeError(
#                         "molecule_query must be a dictionary of field:value."
#                         )
#
#      # validate length
#      if len(molecule_query) != 1:
#         raise ValueError(
#                          "molecule_query must contain exactly one field:value pair."
#                          )
#
#      # validate keys
#      field = list(
#                   molecule_query.keys()
#                   )[0]
#      if field not in self.molecule_search_fields:
#          raise KeyError(
#                         f"{field} is not a valid field. Valid fields are: {self.molecule_search_fields}"
#                         )
#
#      # build search query
#      self.molecule_search_req = self.build_searchReq(
#                                                      molecule_query
#                                                      )
#
#      # execute search query
#      return self._paginateData(
#                                endpoint = "molecules/search",
#                                json_body = self.molecule_search_req
#                                )


#   def create_moleculeSearch_req(
#                                 self,
#                                 molecule_query
#                                 ):
#      """
#      Converts molecule_query to json for COCONUT molecule search.
#      """
#
#      field = list(molecule_query.keys())[0]
#      molecule_search_req = {
#                             "search": {
#                                        "filters": [
#                                                    {
#                                                     "field" : field,
#                                                     "operator" : "=",
#                                                     "value" : molecule_query[field]
#                                                    }
#                                                   ],
#                                        "includes": [
#                                                     {
#                                                      "relation": "properties"
#                                                     }
#                                                    ]
#                                       }
#                             }
#
#      return molecule_search_req


   def build_searchReq(
                       self,
                       search_query
                       ):
      """
      Builds search request using query list of specified actions.

      Parameters
      ----------
      search_query: list of [key, field, value]
         Each entry modifies the 'search' body of the request.
         - If key is 'filters', 'sorts', or 'selects', field is used.
         - If key is does not have field then field should be None.
   
      Returns
      -------
      dict
         Search request.
      """
      # check validation
      if not isinstance(
                        search_query,
                        list
                        ):
         raise TypeError(
                         "`search_query` must be a list of [key, field, value]"
                         )
      # init search_request
      search_req = {
                    "search": {}
                    }
      for entry in search_query:
         if not isinstance(
                           entry,
                           (list, tuple)
                           ) or len(entry) != 3:
            raise ValueError(
                             "Each entry must be a 3-element list: [key, field, value]"
                             )
         key, field, value = entry
         if key in ["filters", "sorts", "selects"]:
            if field is None:
                raise ValueError(
                                 f"`{key}` requires a field"
                                 )
            if key == "filters":
               search_req["search"].setdefault(
                                               "filters",
                                               []
                                               ).append(
                                                        {
                                                         "field": field,
                                                         "operator": "=",
                                                         "value": value
                                                         }
                                                        )
            elif key == "sorts":
               # add check for value
               search_req["search"].setdefault(
                                               "sorts",
                                               []
                                               ).append(
                                                        {
                                                         "field": field,
                                                         "direction": value
                                                         }
                                                         )
            elif key == "selects":
               # add check to make sure value is None
               search_req["search"].setdefault(
                                               "selects", []
                                               ).append(
                                                        {
                                                         "field": field
                                                         }
                                                        )
         else:
            if field is not None:
               raise ValueError(
                                f"`{key}` doesn't require a field. field should be None"
                                )
            # simple key like "page", "limit"
            search_req["search"][key] = value
      return search_req


   def Search(
              self,
              search_query
              ):
      """
      Performs COCONUT search request and returns the json response.
      """
      # build search request
      self.search_req = self.build_searchReq(
                                             search_query
                                             )
      # execute search request
      return self._paginateData(
                                endpoint = "molecules/search",
                                json_body = self.search_req
                                )
