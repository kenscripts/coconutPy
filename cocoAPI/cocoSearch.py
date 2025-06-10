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


#   def advSearch(
#                 self,
#                 search_type,
#                 search_tag,
#                 search_query
#                 ):
#      """
#      Posts to /organisms/search and returns the json response.
#      """
#
#      # get response
#      adv_search_post = f"{self.api_url}/search"
#      adv_search_req = {
#                        "type" : search_type,
#                        "tagType" : search_tag,
#                        "query" : search_query,
#                        }
#      adv_search_res = self.session.post(
#                                         url = adv_search_post,
#                                         json = adv_search_req
#                                         )
#      adv_search_res.raise_for_status()
#
#      # return response as json
#      return adv_search_res.json()


   def advSearch(
                 self,
                 search_type,
                 search_tag,
                 search_query
                 ):
     """
     Posts to /search and returns all paginated results as a list.
     """
 
     adv_search_post = f"{self.api_url}/search"
     curr_pg = 1
     all_data = []
 
     while True:
        # request
        adv_search_req = {
                          "type": search_type,
                          "tagType": search_tag,
                          "query": search_query,
                          "page": curr_pg
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
        print(curr_pg,per_pg,total_hits)
        if curr_pg * per_pg >= total_hits:
           break
        curr_pg += 1

     return all_data
