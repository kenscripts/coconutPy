from cocoAPI.cocoLog import cocoLog

class cocoSearch:
   def __init__(
                self,
                cocoLog
                ):
      # guards
      if not cocoLog.token:
         raise RuntimeError("cocoLog instance is not authenticated.")

      # attributes
      self.session = cocoLog.session
      self.api_url = cocoLog.api_url
      self.adv_search_req = {
                             "type" : "",
                             "tagType" : "",
                             "query" : "",
                             "limit" : "",
                             "sort" : "",
                             "page" : "",
                             "offset" : ""
                             }


   def advSearch(
                 self,
                 search_type,
                 search_tag = None,
                 tag_query = None,
                 filter_query = None,
                 basic_query = None
                 ):
      """
      Posts to /search endpoint and returns the JSON response.
      Validates input according to COCONUT API rules.
      """

      # Allowed values
      valid_types = {
                     "filters",
                     "tags",
                     "basic"
                     }
      valid_tag_types = {
                         "dataSource",
                         "organisms",
                         "citations"
                         }
      valid_filter_keys = {
                           # Molecular properties
                           "tac", "hac", "mw", "emw", "mrc", "vdwv", "fc",
                           # Chemical properties
                           "alogp", "topopsa", "fcsp3", "np", "qed",
                           # Structural features
                           "rbc", "arc", "hba", "hbd",
                           # Lipinski parameters
                           "lhba", "lhbd", "lro5v",
                           # Sugar-related
                           "cs", "crs", "cls",
                           # Classyfire classifications
                           "class", "subclass", "superclass", "parent",
                           # NP classifier
                           "np_pathway", "np_superclass", "np_class", "np_glycoside"
                           }
      empty_values = [
                      None,
                      "",
                      [],
                      {}
                      ]
 
      
      # validate search_type
      if search_type not in valid_types:
         raise ValueError(
                          f"`search_type` must be one of {valid_types}."
                          )

      if search_type == "tags":
         # validate search_tag
         if search_tag not in valid_tag_types:
            raise ValueError(
                             f"`search_tag` must be one of {valid_tag_types}"
                             )
         # validate tag_query
         if not isinstance(
                           tag_query,
                           list
                           ):
            raise TypeError(
                            "`tag_query` must be a list"
                            )
         # validate empty parameters
         non_empty = {
                      k:v
                      for k,v in {
                                  filter_query,
                                  basic_query
                                  }.items() 
                      if v not in empty_values
                      }
         if non_empty:
            raise ValueError(
                             f"{','.join(non_empty)} must be empty for tag-based searches"
                             )
         # assign tag-based search query
         search_query = tag_query

      elif search_type == "filters":
         # validate empty parameters
         non_empty = {
                      k:v
                      for k,v in {
                                  search_tag,
                                  tag_query,
                                  basic_query
                                  }.items() 
                      if v not in empty_values
                      }
         if non_empty:
            raise ValueError(
                             f"{','.join(non_empty)} must be empty for filter-based searches"
                             )
         # validate filter_query
         if not isinstance(
                           filter_query,
                           dict
                           ):
            raise TypeError(
                            "`filter_query` must be a dictionary"
                            )
         invalid_keys = [
                         k
                         for k in query
                         if k not in valid_filter_keys
                         ]
         if invalid_keys:
            raise KeyError(
                           f"Invalid filter key(s): {invalid_keys}"
                           )
         # assign filter-based search query
         search_query = ''.join(
                                f"{key}...{value}"
                                for key,value in filter_query.items()
                                )

      elif search_type == "basic":
         # validate empty parameters
         non_empty = {
                      k:v
                      for k,v in {
                                  search_tag,
                                  tag_query,
                                  filter_query
                                  }.items() 
                      if v not in empty_values
                      }
         if non_empty:
            raise ValueError(
                             f"{','.join(non_empty)} must be empty for basic searches"
                             )
         # validate basic_query
         if not isinstance(
                           basic_query,
                           str
                           ):
            raise TypeError(
                            "`basic_query` must be a string"
                            )
         # assign basic search query
         search_query = basic_query
 

     adv_search_post = f"{self.api_url}/search"
     curr_pg = 1
     all_data = []
 

     # go through pages
     while True:
        # request
        adv_search_req = {
                          "type": search_type,
                          "tagType": search_tag,
                          "query": search_query,
                          "page": curr_pg,
                          "limit": ""
                          }
        adv_search_res = self.session.post(
                                           url = adv_search_post,
                                           json = adv_search_req
                                           )
        adv_search_res.raise_for_status()
        adv_search_json = adv_search_res.json()

        # request data
        pg_data = adv_search_json.get(
                                      "data", {}
                                      )\
                                 .get(
                                      "data", []
                                      )
        if not pg_data:
            break
        all_data.extend(pg_data)

        # page progress
        per_pg = adv_search_json.get(
                                     "data"
                                     )\
                                .get(
                                     "per_page"
                                     )
        total_hits = adv_search_json.get(
                                         "data"
                                         )\
                                    .get(
                                         "total"
                                         )
        if curr_pg * per_pg >= total_hits:
           break
        curr_pg += 1

     return all_data
