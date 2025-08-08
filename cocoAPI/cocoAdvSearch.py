from cocoAPI.cocoBase import cocoBase
from cocoAPI import default_search_requests


class cocoAdvSearch(
                    cocoBase
                    ):
   def __init__(
                self,
                cocoLog
                ):
      # inherits session, api_url
      super().__init__(cocoLog)
      # default search request body
      self.adv_mol_search_info = default_search_requests.adv_mol_search_info
      self.advSearch_req = self.adv_mol_search_info["search"]


   def update_advSearch_req(
                            self,
                            search_type = None,
                            tag_query = None,
                            filter_query = None,
                            basic_query = None
                            ):
      """
      Posts to advanced molecule search endpoint and returns the JSON response.
      """

      empty_values = [
                      None,
                      "",
                      [],
                      {}
                      ]


      # determine which query types are non-empty
      non_empty_queries = [
                           query
                           for query in (
                                         tag_query,
                                         filter_query,
                                         basic_query
                                         )
                           if query
                           ]
      if len(non_empty_queries) > 1:
         raise ValueError(
                          f"Only one of `tag_query`, `filter_query`, or `basic_query` can be used per search."
                          )
 
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      # Taq-Based Search
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      if tag_query is not None:
         # validate tag search dtype
         if not isinstance(
                           tag_query,
                           dict
                           ):
            raise TypeError(
                            f"`tag_query` must be a dictionary with one key from {self.advSearch_tag_keys}"
                            )

         # tag must contain exactly one key-value pair
         if len(tag_query) != 1:
            raise ValueError(
                             "`tag_query` must contain exactly one key-value pair"
                             )

         # validate tag search keys
         invalid_tag_keys = [
                             k
                             for k in tag_query
                             if k not in self.advSearch_tag_keys
                             ]
         if invalid_tag_keys:
            raise KeyError(
                           f"Invalid tag key(s): {invalid_tag_keys}. Valid keys are: {self.advSearch_tag_keys}"
                           )

         # validate tag search value
         tag_type = next(
                         iter(
                              tag_query
                              )
                         )
         tag_value = tag_query[tag_type]
         if not isinstance(
                           tag_value,
                           list
                           ):
            raise TypeError(
                            f"Invalid tag search value. Must be a list of query terms"
                            )

         # build tag search query
         self.advSearch_req.update(
                                   {
                                    "type" : search_type,
                                    "tagType" : tag_type,
                                    "query" : ",".join(
                                                       tag_query[tag_type]
                                                       )
                                    }
                                   )

      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      # Filter-Based Search
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      elif filter_query is not None:
         # validate filter search dtype
         if not isinstance(
                           filter_query,
                           list
                           ):
            raise TypeError(
                            "`filter_query` must be a list of dictionaries with keys from {self.advSearch_filter_keys}"
                            )

         # validate filter search dictionaries
         # build filter search query
         invalid_filter_keys = []
         filter_query_strings = []
         for d in filter_query:
            if not isinstance(d, dict):
               raise TypeError(
                               "Each item in `filter_query` must be a dictionary."
                               )
            single_queries = []
            for k,v in d.items():
               if k not in self.advSearch_filter_keys:
                  invalid_filter_keys.append(k)
               else:
                  single_queries.append(
                                        f"{k}:{v}"
                                        )
            if single_queries:
               filter_query_strings.append(
                                           " ".join(
                                                    single_queries
                                                    )
                                           )
         if invalid_filter_keys:
            raise KeyError(
                           f"Invalid filter key(s): {invalid_filter_keys}. Valid keys are: {self.advSearch_filter_keys}"
                           )

         # build filter search query
         self.advSearch_req.update(
                                   {
                                    "type" : search_type,
                                    "query": " OR ".join(
                                                         filter_query_strings
                                                         )
                                    }
                                   )

      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      # Basic Search
      #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      elif basic_query is not None:
         # validate basic search dtype
         if not isinstance(
                           basic_query,
                           str
                           ):
            raise TypeError(
                            "`basic_query` must be a string of name, SMILES, InChI, or InChI key"
                            )

         # build filter search query
         self.advSearch_req.update(
                                   {
                                    "query": basic_query
                                    }
                                   )
 

   def advSearch(
                 self
                 ):
      # input
      # assign page if not specified
      if not self.advSearch_req.get("page"):
         self.advSearch_req["page"] = 1

      # paginate
      all_data = []
      while True:
         # progress
         curr_pg = self.advSearch_req["page"]

         # request
         adv_search_json = self._post(
                                      endpoint = "search",
                                      json_body = self.advSearch_req
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
         curr_pg += 1

      return all_data


   def clear_advSearch_req(
                           self
                           ):
      self.advSearch_req = {
                            "type" : "",
                            "tagType" : "",
                            "query" : "",
                            "limit" : "",
                            "sort" : "",
                            "page" : "",
                            "offset" : ""
                            }
