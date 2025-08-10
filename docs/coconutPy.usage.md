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
### Input
Input is a list of entries. Each entry is a list of the format [`key`,`field`,`value`].

### Keys and Fields
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

### Search Example (Molecules)
Perform search. Here is a search for molecules:
```
# save search query as variable for readability
mol_search_query = [
                    ["filters","name","Ferutidin"],
                    ["selects","standard_inchi_key",None] # selects key doesn't have values
                    ]
# molecules search
coco.search.Search(
                   resource_endpoint = "molecules",
                   search_query = mol_search_query
                   )
```

### Search Example (Properties)
Perform search. Here is a search for properties:
```
# save search query as variable for readability
# a limit of >50 not allowed by COCONUT API
prop_search_query = [
                     ["filters","lipinski_rule_of_five_violations","0"],
                     ["filters","np_classifier_pathway","Terpenoids"],
                     ["selects","np_classifier_superclass",None],
                     ["limit",None,50]
                     ]
# properties search
coco.search.Search(
                   resource_endpoint = "properties",
                   search_query = prop_search_query
                   )
```


# Advanced Search For COCONUT Molecules Resource
### Input
Input is a list of entries. Each entry is a list of the following format: [type,tag/filter,value].

### Tag-Based Advanced Search
First build the advanced search request:
```
# tag-based example
coco.advSearch.build_AdvSearchQuery(
                                    [
                                     ["tags","organisms","Ferula"]
                                     ]
                                    )
```

Preview and further modify the advanced search query:
```
# preview
coco.advSearch.adv_mol_search_req
# returns

# modify page limit
# preview
# returns 
```

Run the advanced search query:
```
coco.advSearch.run_AdvSearchReq()
```

### Filter-Based Advanced Search
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

### Basic Advanced Search
