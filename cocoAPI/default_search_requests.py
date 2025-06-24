default_collection_search_req = {
                                 "search": {
                                            "scopes": [],
                                            "filters": [
                                                        {
                                                         "field": "title",
                                                         "operator": "=",
                                                         "value": ""
                                                         },
                                                        {
                                                         "field": "description",
                                                         "operator": "=",
                                                         "value": ""
                                                         },
                                                        {
                                                         "field": "identifier",
                                                         "operator": "=",
                                                         "value": ""
                                                         },
                                                        {
                                                         "field": "url",
                                                         "operator": "=",
                                                         "value": ""
                                                         }
                                                        ],
                                            "sorts": [
                                                      {
                                                       "field": "title",
                                                       "direction": "desc"
                                                       },
                                                      {
                                                       "field": "description",
                                                       "direction": "desc"
                                                       },
                                                      {
                                                       "field": "identifier",
                                                       "direction": "desc"
                                                       },
                                                      {
                                                       "field": "url",
                                                       "direction": "desc"
                                                       }
                                                      ],
                                            "selects": [
                                                        {
                                                         "field": "title"
                                                         },
                                                        {
                                                         "field": "description"
                                                         },
                                                        {
                                                         "field": "identifier"
                                                         },
                                                        {
                                                         "field": "url"
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


default_molecule_search_req = {
                               "search": {
                                          "scopes": [],
                                          "filters": [
                                                      {
                                                       "field": "standard_inchi",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "standard_inchi_key",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "canonical_smiles",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "sugar_free_smiles",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "identifier",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "name",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "cas",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "iupac_name",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "murko_framework",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "structural_comments",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "name_trust_level",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "annotation_level",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "variants_count",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "status",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "active",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "has_variants",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "has_stereo",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "is_tautomer",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "is_parent",
                                                       "operator": "=",
                                                       "value": ""
                                                       },
                                                      {
                                                       "field": "is_placeholder",
                                                       "operator": "=",
                                                       "value": ""
                                                       }
                                                      ],
                                          "sorts": [
                                                    {
                                                     "field": "standard_inchi",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "standard_inchi_key",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "canonical_smiles",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "sugar_free_smiles",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "identifier",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "name",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "cas",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "iupac_name",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "murko_framework",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "structural_comments",
                                                     "direction": "desc"
                                                     },
                                                    {
                                                     "field": "name_trust_level",
                                                     "direction": "desc"
                                                     },
                                                     {
                                                      "field": "annotation_level",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "variants_count",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "status",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "active",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "has_variants",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "has_stereo",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "is_tautomer",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "is_parent",
                                                      "direction": "desc"
                                                      },
                                                     {
                                                      "field": "is_placeholder",
                                                      "direction": "desc"
                                                      }
                                                     ],
                                          "selects": [
                                                       {
                                                        "field": "standard_inchi"
                                                        },
                                                       {
                                                        "field": "standard_inchi_key"
                                                        },
                                                       {
                                                        "field": "canonical_smiles"
                                                        },
                                                       {
                                                        "field": "sugar_free_smiles"
                                                        },
                                                       {
                                                        "field": "identifier"
                                                        },
                                                       {
                                                        "field": "name"
                                                        },
                                                       {
                                                        "field": "cas"
                                                        },
                                                       {
                                                        "field": "iupac_name"
                                                        },
                                                       {
                                                        "field": "murko_framework"
                                                        },
                                                       {
                                                        "field": "structural_comments"
                                                        },
                                                       {
                                                        "field": "name_trust_level"
                                                        },
                                                       {
                                                        "field": "annotation_level"
                                                        },
                                                       {
                                                        "field": "variants_count"
                                                        },
                                                       {
                                                        "field": "status"
                                                        },
                                                       {
                                                        "field": "active"
                                                        },
                                                       {
                                                        "field": "has_variants"
                                                        },
                                                       {
                                                        "field": "has_stereo"
                                                        },
                                                       {
                                                        "field": "is_tautomer"
                                                        },
                                                       {
                                                        "field": "is_parent"
                                                        },
                                                       {
                                                        "field": "is_placeholder"
                                                        }
                                                       ],
                                          "includes": [
                                                        {
                                                         "relation": "properties"
                                                         }
                                                        ],
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


default_organism_search_req = {
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
