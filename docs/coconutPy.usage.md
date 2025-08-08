# Load Package
```
from cocoAPI.cocoPy import cocoPy
```

# Login to COCONUT Database
To get login credentials, sign up on [COCONUT](https://coconut.naturalproducts.net/login).  \n
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


# Get COCONUT Resource Details
Retrieve resource details including fields
```
coco.get.searchFields(
                      get_endpoint = "properties"
                      )
```


# Search COCONUT Resources
Input is a list of lists. Each sub list specifies the `search key`, `field`, and `value`.
```
coco.mol.Search(
                [
                 ["filters","name","Ferutidin"],
                 ["selects","standard_inchi_key",None]
                 ]
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
