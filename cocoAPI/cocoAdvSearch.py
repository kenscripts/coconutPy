from cocoAPI.cocoBase import cocoBase
from cocoAPI import default_search_requests
import copy


class cocoAdvSearch(
                    cocoBase
                    ):
   """
   Class for performing advanced searches against COCONUT database.
   """
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)

      # default search request body
      self.adv_mol_search_info = default_search_requests.adv_mol_search_info
      self.adv_mol_search_types = [
                                   "tags",
                                   "filters",
                                   "basic"
                                   ]
      self.default_adv_mol_search_req = self.adv_mol_search_info["search"]


   def _checkAdvSearchQuery(
                            self,
                            adv_search_query
                            ):
      """
      Performs several checks on adv_search_query to ensure correct format.

      Parameters
      ----------
      adv_search_query
         List of entries, where each entry has format [`type`, `tag|filter`, `value`]

      Returns
      -------
      error
         Raises errors if found
      """
      # check input structure
      if not isinstance(
                        adv_search_query,
                        list
                        ) or not all(
                                     isinstance(
                                                entry,
                                                list
                                                ) and len(entry) == 3
                                     for entry in adv_search_query
                                     ):
         raise TypeError(
                         "`adv_search_query` must be a list of [`type`, `tag|filter`, `value`]"
                         )

      # data
      valid_types = self.adv_mol_search_types
      valid_tags = self.adv_mol_search_info["tags"]
      valid_filters = self.adv_mol_search_info["filters"]
      search_types = []

      # go through entries
      for entry in adv_search_query:
         curr_search_type = entry[0]
         curr_tag_filter = entry[1]
         curr_search_value = entry[2]
         search_types.append(
                             curr_search_type
                             )

         # check type
         if curr_search_type not in valid_types:
            raise ValueError(
                             f"Invalid type: {curr_search_type}. Valid types are: {valid_types}"
                             )

         # check tag
         if curr_search_type == "tags":
            if curr_tag_filter not in valid_tags:
               raise ValueError(
                                f"Invalid tag: {curr_tag_filter}. Valid tags are: {valid_tags}"
                                )

         # check filters
         if curr_search_type == "filters":
            if curr_tag_filter not in valid_filters:
               raise ValueError(
                                f"Invalid filter: {curr_tag_filter}. Valid filters are: {valid_filters}"
                                )

         # check basic query
         if curr_search_type == "basic":
            if curr_tag_filter is not None:
               raise TypeError(
                               "For basic query, tag/filter must be of type None"
                               )
            if not isinstance(
                              curr_search_value,
                              str
                              ):
               raise TypeError(
                               "basic query must be a string of name, SMILES, InChI, or InChI key"
                               )

      # check type count
      if len(
             set(
                 search_types
                 )
             ) > 1:
         raise ValueError(
                          f"Only one type of advanced search allowed, either tag-based, filter-based, or basic."
                          )
      if search_types.count("basic") > 1:
         raise ValueError(
                          f"Only one basic query allowed at the same time"
                          )
      if search_types.count("tags") > 1:
         raise ValueError(
                          f"Only one tag-based query allowed at the same time"
                          )


   def build_AdvSearchReq(
                          self,
                          adv_search_query
                          ):
      """
      Builds advanced search request from a list of entries, where each entry has format [`type`, `tag|filter`, `value`].

      Parameters
      ----------
      adv_search_query
         List of entries, where each entry has format [`type`, `tag|filter`, `value`]

      Returns
      -------
      dict
         Advanced search request.
      """
      # check input 
      self._checkAdvSearchQuery(
                                adv_search_query
                                )

      # get search template
      # copy to avoid modifying default search req
      self.adv_mol_search_req = copy.deepcopy(
                                              self.default_adv_mol_search_req
                                              )

      # build search request
      filter_search = None
      filter_query = []
      for entry in adv_search_query:
         curr_search_type = entry[0]
         curr_tag_filter = entry[1]
         curr_search_value = entry[2]

         # build filter-based query
         if curr_search_type == "filters":
            filter_search = True
            self.adv_mol_search_req["type"] = curr_search_type
            filter_query.append(
                                f"{curr_tag_filter}:{curr_search_value}"
                                )

         # build tag-based query
         if curr_search_type == "tags":
            self.adv_mol_search_req["type"] = curr_search_type
            self.adv_mol_search_req["tagType"] = curr_tag_filter
            self.adv_mol_search_req["query"] = curr_search_value
            break

         # build basic query
         if curr_search_type == "basic":
            self.adv_mol_search_req["query"] = curr_search_value
            break

      # build filter-based query
      if filter_search:
         self.adv_mol_search_req["query"] = " ".join(
                                                     filter_query
                                                     )


   def run_AdvSearchReq(
                        self
                        ):
      """
      Runs advanced search request and returns the json response.

      Returns
      -------
      dict
         Complete results from advanced search request.
      """
      # input
      # assign page if not specified
      if not self.adv_mol_search_req.get("page"):
         self.adv_mol_search_req["page"] = 1

      # paginate
      all_data = []
      while True:
         # progress
         curr_pg = self.adv_mol_search_req["page"]

         # request
         adv_search_json = self._post(
                                      endpoint = "search",
                                      json_body = self.adv_mol_search_req
                                      )

         # data
         pg_data = adv_search_json.get(
                                       "data", {}
                                       )\
                                  .get(
                                       "data", []
                                       )
         if not pg_data:
            print(
                  f"Warning: Empty data returned on page {curr_pg}. Pagination stopped."
                  )
            break
         all_data.extend(
                         pg_data
                         )

         # update progress
         per_pg = adv_search_json.get(
                                      "data"
                                      )\
                                 .get(
                                      "per_page"
                                      )
         total_recs = adv_search_json.get(
                                          "data"
                                          )\
                                     .get(
                                          "total"
                                          )
         curr_recs = curr_pg * per_pg
         print(
               f"Retrieved {curr_recs} of {total_recs} records",
               end = "\r",
               flush = True
               )

         # check progress
         if curr_recs >= total_recs:
            break
         self.adv_mol_search_req["page"] += 1

      return all_data