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
         - If key is 'page' or 'limit', field should be None.
   
      Returns
      -------
      dict
         Updated molecule search request.
      """
      # check validation
      if not isinstance(
                        search_query,
                        list
                        ):
         raise TypeError(
                         "`search_query` must be a list of [key, field, value]"
                         )
      # search_template
      search_query_req = copy.deepcopy(
                                       self.default_molecule_search_req
                                       )
      for entry in search_query:
         # use key to determine length of subkeys and if it matches with list len
         # len(default_search_req["key"]) == sum(x is not None for x in my_list[minus 1st key])
         # if sum(item) == 2
         #query_search_req["search"]["key"]["value"]
         # if sum(item) == 3
         #query_search_req["search"]["subkey"]["value"]
         if not isinstance(
                           entry,
                           (list, tuple)
                           ) or len(entry) != 3:
            raise ValueError(
                             "Each entry must be a 3-element list: [key, field, value]"
                             )
         key, field, value = entry
         if key in ["filters", "sorts", "selects"]:
            if key == "filters":
               search_query_req["search"].setdefault(
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
               search_query_req["search"].setdefault(
                                                     "sorts",
                                                     []
                                                     ).append(
                                                              {
                                                               "field": field,
                                                               "direction": value
                                                               }
                                                              )
            elif key == "selects":
               search_query_req["search"].setdefault(
                                                     "selects", []
                                                     ).append(
                                                              {
                                                               "field": field
                                                               }
                                                              )

         else:
            # simple key like "page", "limit"
            search_query_req["search"][key] = value
         print(search_query_req)
      return search_query_req


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


   def set_fieldValue(
                      key_dictionary,
                      field, 
                      value
                      ):
      for entry in key_dictionary:
         if entry["field"] == field:
            entry["value"] = value
            return
