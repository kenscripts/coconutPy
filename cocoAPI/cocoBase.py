class cocoBase:
   def __init__(
                self,
                cocoLog
                ):
      # login attributes
      self.session = cocoLog.session
      self.api_url = cocoLog.api_url
      # login check
      if not cocoLog.token:
         raise RuntimeError(
                            "Authentication required. Please log in using cocoLog"
                            )


   def _get(
            self,
            endpoint,
            params = None
            ):
      url = f"{self.api_url}/{endpoint}"
      res = self.session.get(
                             url = url,
                             params = params
                             )
      res.raise_for_status()
      return res.json()


   def _post(
             self,
             endpoint,
             json_body
             ):
      url = f"{self.api_url}/{endpoint}"
      res = self.session.post(
                              url = url,
                              json = json_body
                              )
      res.raise_for_status()
      return res.json()


   def _paginateData(
                     self,
                     endpoint,
                     json_body
                     ):
      # checks
      if not isinstance(
                        json_body,
                        dict
                        ):
         raise TypeError(
                         "`json_body` must be a dictionary."
                         )
      # pagination input
      # create copy to modify page
      # create page if not present
      json_copy = json_body.copy()
      json_copy.setdefault(
                           "page",
                           1
                           )
      # paginate
      all_data = []
      while True:
         # progress
         curr_pg = json_copy["search"]["page"]
         # request
         response = self._post(
                               endpoint = endpoint,
                               json_body = json_copy
                               )
         # data
         pg_data = response.get(
                                "data",
                                []
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
         last_pg = response["last_page"]
         print(
               f"Retrieved page {curr_pg} of {last_pg}.",
               end = "\r",
               flush = False
               )
         # check progress
         if curr_pg == last_pg:
            break
         json_copy["search"]["page"] += 1
      return all_data
