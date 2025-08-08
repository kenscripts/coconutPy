from cocoAPI.cocoBase import cocoBase
from cocoAPI import default_search_requests


class cocoSearch(
                 cocoBase
                 ):
   """
   Class for performing searches against COCONUT database.
   """
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)

      # default search request body
      self.default_citations_search_req = default_search_requests.default_citations_search_req
      self.default_collections_search_req = default_search_requests.default_collections_search_req
      self.default_molecules_search_req = default_search_requests.default_molecules_search_req
      self.default_organisms_search_req = default_search_requests.default_organisms_search_req
      self.default_properties_search_req = default_search_requests.default_properties_search_req
      self.default_reports_search_req = default_search_requests.default_reports_search_req


   def Search(
              self,
              resource_endpoint,
              search_query
              ):
      """
      Performs COCONUT search request and returns the json response.
      """
      # check search request
      self._checkSearchQuery(
                             resource_endpoint = resource_endpoint,
                             search_query = search_query
                             )
      # build search request
      self.search_req = self._buildSearchReq(
                                             resource_endpoint = resource_endpoint,
                                             search_query = search_query
                                             )
      # execute search request
      return self._paginateData(
                                endpoint = f"{resource_endpoint}/search",
                                json_body = self.search_req
                                )


   def _checkSearchQuery(
                         self,
                         resource_endpoint,
                         search_query
                         ):
      # check input structure
      if not isinstance(
                        search_query,
                        list
                        ) or not all(
                                     isinstance(
                                                entry, list
                                                ) and len(entry) == 3 
                                     for entry in search_query
                                     ):
         raise TypeError(
                         "`search_query` must be a list of [key, field, value]"
                         )
      # use default search request to get keys & fields
      attr_name = f"default_{resource_endpoint}_search_req"
      resource_search_req = getattr(
                                    self,
                                    attr_name, 
                                    None
                                    )
      # check keys
      resource_keys = resource_search_req["search"].keys()
      if not all(
                 entry[0] in resource_keys
                 for entry in search_query
                 ):
         raise ValueError(
                          f"keys must be a one of: {resource_keys}"
                          )
      # check fields
      resource_fields = list(
                             self._get(
                                       endpoint = resource_endpoint
                                       )["data"]["fields"]
                             )
      resource_fields.append(
                             None
                             )
      if not all(
                 entry[1] in resource_fields
                 for entry in search_query
                 ):
         raise ValueError(
                          f"fields must be a one of: {resource_fields}"
                          )
      # check values
      for entry in search_query:
         if entry[0] == "select":
            if not isinstance(
                              entry[2],
                              None
                              ):
               raise ValueError(
                                f"for select entry, value must be None"
                                )
         if entry[0] == "page" or entry[0] == "limit":
            if not isinstance(
                              entry[1],
                              None
                              ):
               raise ValueError(
                                f"for `page` or `limit` key, field must be None"
                                )
            if not isinstance(
                              entry[2],
                              int
                              ):
               raise ValueError(
                                f"for `page` or `limit` key, value must be integer"
                                )

      
   def _buildSearchReq(
                       self,
                       resource_endpoint,
                       search_query
                       ):
      """
      Builds search request using query list of specified actions. Checks input.

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


   def allRecords(
                  self,
                  resource,
                  pg_limit = 25
                  ):
      # request json 
      all_collection_req = {
                            "search": {
                                       "filters": [],
                                       "page": 1,
                                       "limit": pg_limit
                                       }
                            }
      # request data
      all_collection_data = self._paginateData(
                                               endpoint = f"{resource}/search",
                                               json_body = all_collection_req
                                               )
      return all_collection_data
