# Search syntax

Kin.Zone comes with a search syntax by with you can modify the categories,
engines, languages and more.  See the {{link('preferences', 'preferences')}} for
the list of engines, categories and languages.

## `!` select engine and category

To set category and/or engine names use a `!` prefix.  To give a few examples:

- search in Wikipedia for **paris**

  - {{search('!wp paris')}}
  - {{search('!wikipedia paris')}}

- search in category **map** for **paris**

  - {{search('!map paris')}}

- image search

  - {{search('!images Wau Holland')}}

Abbreviations of the engines and languages are also accepted.  Engine/category
modifiers are chain able and inclusive.  E.g. with {{search('!map !ddg !wp
paris')}} search in map category and DuckDuckGo and Wikipedia for **paris**.

## `:` select language

To select language filter use a `:` prefix.  To give an example:

- search Wikipedia by a custom language

  - {{search(':fr !wp Wau Holland')}}

## `!!<bang>` external bangs

Kin.Zone supports the external bangs from <a href="https://duckduckgo.com" target="_blank">DuckDuckGo</a>.  To directly jump to a
external search page use the `!!` prefix.  To give an example:

- search Wikipedia by a custom language

  - {{search('!!wfr Wau Holland')}}

Please note, your search will be performed directly in the external search
engine, Kin.Zone cannot protect your privacy on this.

<a href="https://duckduckgo.com" target="_blank">DuckDuckGo</a>: https://duckduckgo.com/bang

## `!!` automatic redirect

When mentioning `!!` within the search query (separated by spaces), you will
automatically be redirected to the first result.  This behavior is comparable to
the "Feeling Lucky" feature from DuckDuckGo.  To give an example:

- search for a query and get redirected to the first result

  - {{search('!! Wau Holland')}}

Please keep in mind that the result you are being redirected to can't become
verified for being trustworthy, Kin.Zone cannot protect your personal privacy
when using this feature.  Use it at your own risk.

## Special Queries

In the {{link('preferences', 'preferences')}} page you find keywords for
_special queries_.  To give a few examples:

- generate a random UUID

  - {{search('random uuid')}}

- find the average

  - {{search('avg 123 548 2.04 24.2')}}

- show _user agent_ of your browser (needs to be activated)

  - {{search('user-agent')}}

- convert strings to different hash digests (needs to be activated)

  - {{search('md5 lorem ipsum')}}
  - {{search('sha512 lorem ipsum')}}
