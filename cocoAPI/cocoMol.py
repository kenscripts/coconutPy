from cocoAPI.cocoBase import cocoBase
from cocoAPI.default_search_requests import default_molecules_search_req


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
      self.default_molecule_search_req = default_molecules_search_req


   def Search(
              self,
              resource_endpoint,
              search_query
              ):
      """
      Performs COCONUT search request and returns the json response.
      """
      # build search request
      self.search_req = self._buildSearchReq(
                                             search_query
                                             )
      # execute search request
      return self._paginateData(
                                endpoint = f"{resource_endpoint}/search",
                                json_body = self.search_req
                                )


   def _buildSearchReq(
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
