# Load Package
```
import os
from cocoAPI.cocoPy import cocoPy
```

# Login to COCONUT Database
To get login credentials, sign up on [COCONUT](https://coconut.naturalproducts.net/login).


Enter email and password to login. This can be done manually or by saving credentials to ENVIRONMENT variable
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


# Get COCONUT Resource Details
COCONUT resources include: `citations`, `collections`, `molecules`, `organisms`, `properties`, and `reports`.

To retrive resource details:
```
coco.get.resourceJson(
                      resource_endpoint = "properties"
                      )
```

To retrieve resource fields
```
coco.get.resourceFields(
                        resource_endpoint = "properties"
                        )
```


# Search COCONUT Resources
Input is a list of entries. Each entry is a list of the format [`key`,`field`,`value`].


To find keys for resource:
```
# molecules resource
coco.search.default_molecules_search_req["search"].keys()
```

To find fields for resource:
```
# molecules resource
coco.get.resourceFields(
                        resource_endpoint = "molecules"
                        )
```

Perform search:
```
# molecules search
# save search query as variable for readability
mol_search_query = [
                    ["filters","name","Ferutidin"],
                    ["selects","standard_inchi_key",None] # selects key doesn't have values
                    ]
coco.search.Search(
                   resource_endpoint = "molecules",
                   search_query = mol_search_query
                   )
```


# Advanced Search For COCONUT Resources
## Tag-Based Advanced Search 
```
# organisms example
coco.search.update_advSearch_req(
                                 search_type = "tags",
                                 tag_query = {
                                              "organisms" : [
                                                             "Ferula"
                                                             ]
                                              }
            
                                 )

coco.search.advSearch()
```


## Filter-Based Advanced Search
```
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
```
