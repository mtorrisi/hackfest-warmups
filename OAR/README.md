<!-- Copyright 2016 Sci-GaIA Consortium

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. -->


# Warmups for Open Access Repository

This directory shows how to interact with the Invenio API to use the Open Access repository. Warmups are in the langugage-specific directories:

  * curl
  * php

## Search

  * Syntax: `GET /search?p=...&of=...&ot=...&jrec=...&rg=...`
    _e.g._ https://oar.sci-gaia.eu/search?p1=collection:PRESENTATIONSHACKFEST&of=recjson&jrec=1&rg=10

  * Parameters:
    * `p` = pattern (i.e. your query)
    * `of` = output format (e.g. `xm` for MARCXML)
    * `ot` = output tags (e.g. ` ` to get all fields, `100` to get titles only)
    * `jrec` = jump to record ID (e.g. 1 for first hit)
    * `rg` = records-in-groups-of (e.g. 10 hits per page)

      _e.g._ `https://oar.sci-gaia.eu/search?p1=collection:PUBLICATIONSHACKFEST+keyword:Gateway&of=recjson&jrec=1&rg=10`

  * Example: (returning full XML or JSON output)
      * XML output : `https://oar.sci-gaia.eu/search?p1=collection:PRESENTATIONSHACKFEST&of=xm`
      * JSON output : `https://oar.sci-gaia.eu/search?p1=collection:PRESENTATIONSHACKFEST&of=recjson`
      * Search (doi - title) :
        * Search with keywords `https://oar.sci-gaia.eu/search?p1=collection:IMAGESHACKFEST+author:Smith+keyword:Open+keyword:Gateway&of=recjson&ot=title&jrec=1&rg=10`
        * Search with DOI https://oar.sci-gaia.eu/search?p1=doi:10.15169/sci-gaia:1479297245.67&of=xm
        * Search with DOI with JSON output https://oar.sci-gaia.eu/search?p1=doi:10.15169/sci-gaia:1479297245.67&of=recjson

For further information, see https://oar.sci-gaia.eu/help/hacking/search-engine-api

## Submit
