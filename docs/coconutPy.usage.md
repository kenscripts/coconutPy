from cocoAPI.cocoPy import cocoPy

# login
coco = cocoPy(
              email = "<>",
              password = "<>"
              )


# molecule search
MOL_QUERY = {
             "name":"Ferutidin"
             }
coco.mol.molSearch(
                   MOL_QUERY
                   )


# advanced search (tag-based; organisms)
coco.search.update_advSearch_req(
                                 search_type = "tags",
                                 tag_query = {
                                              "organisms" : [
                                                             "Ferula"
                                                             ]
                                              }
            
                                 )
coco.search.advSearch()
                                 

# advanced search (filter-based)
coco.search.update_advSearch_req(
                                 search_type = "filters",
                                 filter_query = [
                                                 {
                                                  "mw" : "500..1000",
                                                  "np_pathway" : "Alkaloids"
                                                  }
                                                 ]
                                 )
coco.search.advSearch()


# search all collections
coco.collect.get_allCollections()

# Get Class
Return search fields available for each resource.
```
coco.get.searchFields(
                      get_endpoint = "properties"
                      )
```
