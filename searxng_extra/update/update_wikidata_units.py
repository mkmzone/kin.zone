#!/usr/bin/env python
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Fetch units from :origin:`searx/engines/wikidata.py` engine.

Output file: :origin:`searx/data/wikidata_units.json` (:origin:`CI Update data
...  <.github/workflows/data-update.yml>`).

"""

import json
import collections

# set path
from os.path import join

from searx import searx_dir
from searx.engines import wikidata, set_loggers
from searx.data import data_dir

DATA_FILE = data_dir / 'wikidata_units.json'

set_loggers(wikidata, 'wikidata')

# the response contains duplicate ?item with the different ?symbol
# "ORDER BY ?item DESC(?rank) ?symbol" provides a deterministic result
# even if a ?item has different ?symbol of the same rank.
# A deterministic result
# see:
# * https://www.wikidata.org/wiki/Help:Ranking
# * https://www.mediawiki.org/wiki/Wikibase/Indexing/RDF_Dump_Format ("Statement representation" section)
# * https://w.wiki/32BT
# * https://en.wikibooks.org/wiki/SPARQL/WIKIDATA_Precision,_Units_and_Coordinates#Quantities
#   see the result for https://www.wikidata.org/wiki/Q11582
#   there are multiple symbols the same rank
SARQL_REQUEST = """
SELECT DISTINCT ?item ?symbol ?tosi ?tosiUnit
WHERE
{
  ?item wdt:P31/wdt:P279 wd:Q47574 .
  ?item p:P5061 ?symbolP .
  ?symbolP ps:P5061 ?symbol ;
           wikibase:rank ?rank .
  OPTIONAL {
    ?item p:P2370 ?tosistmt .
    ?tosistmt psv:P2370 ?tosinode .
    ?tosinode wikibase:quantityAmount ?tosi .
    ?tosinode wikibase:quantityUnit ?tosiUnit .
  }
  FILTER(LANG(?symbol) = "en").
}
ORDER BY ?item DESC(?rank) ?symbol
"""

_wikidata_url = "https://www.wikidata.org/entity/"


def get_data():
    results = collections.OrderedDict()
    response = wikidata.send_wikidata_query(SARQL_REQUEST)
    for unit in response['results']['bindings']:
        name = unit['item']['value'].replace(_wikidata_url, '')
        symbol = unit['symbol']['value']
        si_name = unit.get('tosiUnit', {}).get('value', '').replace(_wikidata_url, '')
        to_si_factor = unit.get('tosi', {}).get('value', '')
        if name not in results:
            # ignore duplicate: always use the first one
            results[name] = {
                'symbol': symbol,
                'si_name': si_name if si_name else None,
                'to_si_factor': float(to_si_factor) if to_si_factor else None,
            }
    return results


def get_wikidata_units_filename():
    return join(join(searx_dir, "data"), "")


if __name__ == '__main__':
    with DATA_FILE.open('w', encoding="utf8") as f:
        json.dump(get_data(), f, indent=4, sort_keys=True, ensure_ascii=False)
