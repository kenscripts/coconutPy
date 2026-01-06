class cocoBase:
   """
   Base class for COCONUT API requests.
   """
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
      """
      Performs GET request to the COCONUT API.

      Parameters
      ----------
      endpoint
         COCONUT API endpoint
      params
         GET parameters

      Returns
      -------
      dict
         JSON response from the COCONUT API.
      error
         Raises errors if found
      """
      # build url
      url = f"{self.api_url}/{endpoint}"

      # request
      res = self.session.get(
                             url = url,
                             params = params
                             )

      # check response
      res.raise_for_status()

      # return json response
      return res.json()


   def _post(
             self,
             endpoint,
             json_body
             ):
      """
      Performs POST request to the COCONUT API.

      Parameters
      ----------
      endpoint
         COCONUT API endpoint
      json_body
         JSON body for the POST request

      Returns
      -------
      dict
         JSON response from the COCONUT API.
      error
         Raises errors if found
      """
      # build url
      url = f"{self.api_url}/{endpoint}"

      # request
      res = self.session.post(
                              url = url,
                              json = json_body
                              )

      # check response
      res.raise_for_status()

      # return json response
      return res.json()


   def _paginateData(
                     self,
                     endpoint,
                     json_body
                     ):
      """
      Performs pagination on the data returned from the COCONUT API.

      Parameters
      ----------
      endpoint
         COCONUT API endpoint
      json_body
         JSON body for the POST request

      Returns
      -------
      dict
         Complete results from the COCONUT API.
      error
         Raises errors if found
      """
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
      # create page if not present; page is below search
      json_copy = json_body.copy()
      json_copy.setdefault(
                           "search",
                           {}
                           ) \
               .setdefault(
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