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
Here is a search example for molecules:
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
Here is a search example for properties:
```
# save search query as variable for readability
prop_search_query = [
                     ["filters","lipinski_rule_of_five_violations","0"],
                     ["filters","np_classifier_pathway","Terpenoids"],
                     ["selects","np_classifier_superclass",None],
                     ["limit",None,50] # a limit of >50 not allowed by COCONUT API
                     ]
# properties search
coco.search.Search(
                   resource_endpoint = "properties",
                   search_query = prop_search_query
                   )
```

### Search Example (Collections)
Here is a search example for collections to identify plant collections:
```
# get fields for collections resource
coco.get.resourceFields(
                        resource_endpoint = "collections"
                        )

# get all records for collections resource
for coll in coco.search.allRecords(
                                   resource_endpoint = "collections"
                                   ):
   # find collections that mention plants
   if "plant" in coll["description"]:
      print(
            coll["title"]
            )
```

# Advanced Search For COCONUT Molecules Resource
### Input
Input is a list of entries. Each entry is a list of the following format: [`type`, `tag|filter`,`value`].

### Types, Tags, Filters
To find accepted types:
```
coco.advSearch.adv_mol_search_types
```
To find accepted tags:
```
coco.advSearch.adv_mol_search_info["tags"]
```
To find accepted filters:
```
coco.advSearch.adv_mol_search_info["filters"]
```

### Tag-Based Advanced Search
First build the advanced search request:
```
coco.advSearch.build_AdvSearchReq(
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
{'type': 'tags', 'tagType': 'organisms', 'query': 'Ferula', 'limit': '', 'sort': '', 'page': '', 'offset': ''}

# modify page limit
coco.advSearch.adv_mol_search_req["limit"] = 50 # a limit of >50 not allowed by COCONUT API

# preview
coco.advSearch.adv_mol_search_req
# returns 
{'type': 'tags', 'tagType': 'organisms', 'query': 'Ferula', 'limit': 50, 'sort': '', 'page': '', 'offset': ''}
```

Run the advanced search query:
```
coco.advSearch.run_AdvSearchReq()
```

### Filter-Based Advanced Search (Single Filter)
First build the advanced search request:
```
coco.advSearch.build_AdvSearchReq(
                                  [
                                   ["filters","np_pathway","Alkaloids"]
                                   ]
                                  )
```

Run the advanced search query:
```
coco.advSearch.run_AdvSearchReq()
```

### Filter-Based Advanced Search (Multiple Filters)
First build the advanced search request:
```
coco.advSearch.build_AdvSearchReq(
                                  [
                                   ["filters","np_pathway","Alkaloids"],
                                   ["filters","mw","500..1000"]
                                   ]
                                  )

# preview
coco.advSearch.adv_mol_search_req
# returns
{'type': 'filters', 'tagType': 'organisms', 'query': 'np_pathway:Alkaloids mw:500..1000', 'limit': '', 'sort': '', 'page': '', 'offset': ''}
```

Run the advanced search query:
```
coco.advSearch.run_AdvSearchReq()
```

### Basic Advanced Search
First build the advanced search request:
```
coco.advSearch.build_AdvSearchReq(
                                  [
                                   ["basic",None,"REFJWTPEDVJJIY-UHFFFAOYSA-N"]
                                   ]
                                  )
```

Run the advanced search query:
```
coco.advSearch.run_AdvSearchReq()
```
