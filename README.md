# BDBSA Data Demo

This repository contains a very small subset of the BDBSA data encoded in RDF and adheres to the TERN Ontology.

## Summary

The dataset contains the description of the top-level BDBSA `RDFDataset` with a single `subset` `RDFDataset` with the ID `project-472`. These instances contain the metadata description about the dataset. A relationship to the `creator` (Department for Environment and Water, South Australian Government) also exists.

A single `Site` with the identifier `RAW00301-217370` exists with some descriptions about it described with the `Attribute` class. Its geometry is also described via the `hasGeometry` relationship linking to a centroid `Point`. Relevant regions of interest are also linked by the site via the `sfWithin` relationship. This denotes that the site is physically within the listed regions.

The `Site` has a single `SiteVisit` with the identifier `405136`. During this `SiteVisit`, 8 observations were made towards 3 features of interest. Each observation provides the property that was observed via the `observedProperty` relationship and the result of each observation is linked via the `hasSimpleResult` relationship. The time when the observation was made as well as the procedure used is also shown via the `resultDateTime` and `usedProcedure` relationships respectively.

Each observation is linked to the `FeatureOfInterest` via the `hasFeatureOfInterest` relationship. A `FeatureOfInterest` is simply the _thing_ that is having its property observed. The type of _thing_ it is, is denoted by the `featureType` relationship.

## View the data in Ontodia

The data in this repository is made available via Ontodia at https://ternaustralia.github.io/bdbsa-data-demo/.

## SPARQL endpoint

The data is also made available via a SPARQL endpoint at https://graphdb.tern.org.au/repositories/bdbsa_data_demo.

If you'd like to view it, you can use this SPARQL client at https://yasgui.triply.cc/ and query the SPARQL endpoint mentioned above.

Here's an example query fetching all sites and their properties and values:

```sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX tern: <https://w3id.org/tern/ontologies/tern/>
SELECT * WHERE {
    ?site a tern:Site .
    ?site ?p ?o .
} LIMIT 100
```
