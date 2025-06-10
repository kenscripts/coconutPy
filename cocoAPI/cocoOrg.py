from cocoAPI.cocoLog import cocoLog

class cocoOrg:
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
      self.org_get_res= {}
      self.org_search_fields = []
      self.get_orgResponse() # run automatically
      self.org_search_req = {
                             "search": {
                                        "scopes": [],
                                        "filters": [
                                                    {
                                                     "field": "name",
                                                     "operator": "=",
                                                     "value": ""
                                                     },
                                                    {
                                                     "field": "iri",
                                                     "operator": "=",
                                                     "value": ""
                                                     },
                                                    {
                                                     "field": "rank",
                                                     "operator": "=",
                                                     "value": ""
                                                     },
                                                    {
                                                     "field": "molecule_count",
                                                     "operator": "=",
                                                     "value": ""
                                                     }
                                                   ],
                                        "sorts": [
                                                  {
                                                   "field": "name",
                                                   "direction": "desc"
                                                   },
                                                  {
                                                   "field": "iri",
                                                   "direction": "desc"
                                                   },
                                                  {
                                                   "field": "rank",
                                                   "direction": "desc"
                                                   },
                                                  {
                                                   "field": "molecule_count",
                                                   "direction": "desc"
                                                   }
                                                  ],
                                        "selects": [
                                                    {
                                                     "field": "name"
                                                     },
                                                    {
                                                     "field": "iri"
                                                     },
                                                    {
                                                     "field": "rank"
                                                     },
                                                    {
                                                     "field": "molecule_count"
                                                     }
                                                    ],
                                        "includes": [],
                                        "aggregates": [],
                                        "instructions": [],
                                        "gates": [
                                                  "create",
                                                  "update",
                                                  "delete"
                                                  ],
                                        "page": 1,
                                        "limit": 10
                                        }
                     }


   def get_orgResponse(
                       self
                       ):
      """
      Fetches /organisms metadata (e.g. search fields).
      Stores the response and a list of available search fields.
      Automatically run once cocoOrg is created.
      """
      # get response
      org_get = f"{self.api_url}/organisms"
      org_get_res = self.session.get(
                                     url = org_get
                                     )
      org_get_res.raise_for_status()

      # set response as attributes
      self.org_get_res = org_get_res.json()
      self.org_search_fields = self.org_get_res["data"]["fields"]


   def orgSearch(
                 self,
                 org_query_df
                 ):
      """
      Posts to /organisms/search and returns the json response.
      """
      # guards
      #if not isinstance(
      #                  org_query_df,
      #                  dict
      #                  ):
      #   raise TypeError("org_query_df must be a dictionary of field:value.")
      #if len(org_query) != 1:
      #   raise ValueError("org_query must contain exactly one field:value pair.")
      #field = list(org_query.keys())[0]
      #if field not in self.org_search_fields:
      #   raise KeyError(
      #                  f"Field {org_query.items()} is not valid.Valid fields are: {self.org_search_fields}"
      #                  )


      # get response
      org_search_post = f"{self.api_url}/organisms/search"
      self.update_orgSearch(
                            org_query_df
                            )
      org_search_res = self.session.post(
                                         url = org_search_post,
                                         json = self.org_search_req
                                         )
      org_search_res.raise_for_status()

      # return response as json
      return org_search_res.json() # allows for multiple searches with class instance


   def update_orgSearch(
                        self,
                        org_query_df
                        ):
      """
      Updates organism search request using values in org_query_df.
      """

      #field = list(org_query.keys())[0]
      #search_json = {
      #               "search": {
      #                          "filters": [
      #                                      {
      #                                       "field" : field,
      #                                       "operator" : "=",
      #                                       "value" : org_query[field]
      #                                       }
      #                                      ],
      #                          }
      #               }
      #return search_json
      #search_filter = [
      #                 {
      #                  "field": key,
      #                  "operator": "=",
      #                  "value": value
      #                  }
      #                  for key, value in org_query.items()
      #                 ]
      for i,row in org_query_df.iterrows():
         key = row["search_key"]
         field = row["field"]
         value = row["value"]
         for item in self.org_search_req["search"][key]:
            if item.get("field") == field:
               item["value"] = value
