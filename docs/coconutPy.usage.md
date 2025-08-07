# Load
```
from cocoAPI.cocoPy import cocoPy
```

# Login
Enter email and password to login.
This can be done manually or by saving credentials to env
```
# get email and password from env 
EMAIL = os.getenv(
                  "COCONUT_EMAIL"
                  )
PSSWD = os.getenv(
                  "COCONUT_PASSWORD"
                  )

# login
coco = cocoPy(
              email = EMAIL,
              password = PSSWD
              )
```


# Get
Retrieve resource details including fields
```
coco.get.searchFields(
                      get_endpoint = "properties"
                      )
```

# Search
coco.mol.Search(
                [
                 ["filters","name","Ferutidin"],
                 ["selects","standard_inchi_key",None]
                 ]
                )


# Advanced Search
## Tag-based (organisms)
coco.search.update_advSearch_req(
                                 search_type = "tags",
                                 tag_query = {
                                              "organisms" : [
                                                             "Ferula"
                                                             ]
                                              }
            
                                 )
coco.search.advSearch()
                                 

## Filter-based[kk
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

