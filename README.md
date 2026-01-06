# coconutPy
![GitHub repo size](https://img.shields.io/github/repo-size/kenscripts/coconutPy?style=flat)  
A Python wrapper for the [COCONUT](https://coconut.naturalproducts.net/) natural product database REST API. All responses are retrieved as JSON.


# Install
```
# from github
pip install git+https://github.com/kenscripts/coconutPy.git`
```

# Quick Start
```
# import
import os
from cocoAPI import cocoPy

# save login credenitals as env variables
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

# molecule search
res = coco.mol.search(
                      [
                       ["filters", "name", "caffeine"]
                       ]
                      )
print(res)
```

# Usage
See [docs](https://github.com/kenscripts/coconutPy/blob/main/docs/coconutPy.usage.md)


# Database Citations
COCONUT Paper:  
Venkata Chandrasekhar, Kohulan Rajan, Sri Ram Sagar Kanakam, Nisha Sharma, Viktor Weißenborn, Jonas Schaub, Christoph Steinbeck, 
COCONUT 2.0: a comprehensive overhaul and curation of the collection of open natural products database, Nucleic Acids Research, 2024;, gkae1063, 
https://doi.org/10.1093/nar/gkae1063

COCONUT Software:  
Venkata, C., Kanakam, S. R. S., Sharma, N., Schaub, J., Steinbeck, C., & Rajan, K. (2024).
COCONUT (Version v0.0.1 - prerelease) [Computer software].
https://doi.org/10.5281/zenodo.13283949