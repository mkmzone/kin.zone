# About 

Kin.Zone is a <a href="https://en.wikipedia.org/wiki/Metasearch_engine" target="_blank">metasearch engine</a> based on SearXNG, aggregating the results of other
{{link('search engines', 'preferences')}} while not storing information about
its users.

Kin.Zone and SearXNG projects are driven by an open community, join on Matrix if
you have questions or just want to chat about SearXNG at <a href="https://matrix.to/#/#searxng:matrix.org" target="_blank">#searxng:matrix.org</a>

Make Kin.Zone and SearXNG better.

- You can improve Kin.Zone and SearXNG translations at <a href="https://translate.codeberg.org/projects/searxng/" target="_blank">Weblate</a>.
- Track development, send contributions, and report issues at <a href="https://github.com/mkmzone/kin.zone" target="_blank">Kin.Zone Source Code</a> or <a href="https://github.com/searxng/searxng/" target="_blank">SearXNG Source Code</a>.
- To get further information, visit SearXNG's project documentation at <a href="https://docs.searxng.org/" target="_blank">SearXNG docs</a>.

## Why use it?

- Kin.Zone may not offer you as personalized results as Google, but it doesn't
  generate a profile about you.
- Kin.Zone doesn't care about what you search for, never shares anything with a
  third-party, and it can't be used to compromise you.
- Kin.Zone is free software, the code is 100% open, and everyone is welcome to
  make it better.

If you do care about privacy, want to be a conscious user, or otherwise believe
in digital freedom, make Kin.Zone or SearXNG your default search engine or run it on your
own server!

## How do I set it as the default search engine?

Kin.Zone and SearXNG supports <a href="https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md" target="_blank">OpenSearch</a>.  For more information on changing your default
search engine, see your browser's documentation:

- <a href="https://support.mozilla.org/en-US/kb/add-or-remove-search-engine-firefox" target="_blank">Firefox</a>
- <a href="https://support.microsoft.com/en-us/help/4028574/microsoft-edge-change-the-default-search-engine" target="_blank">Microsoft Edge</a> - Behind the link, you will also find some useful instructions
  for Chrome and Safari.
- <a href="https://www.chromium.org/tab-to-search" target="_blank">Chromium</a>-based browsers only add websites that the user navigates to without
  a path.

When adding a search engine, there must be no duplicates with the same name.  If
you encounter a problem where you cannot add the search engine, you can either:

- remove the duplicate (default name: Kin.Zone or SearXNG) or
- contact the owner to give the instance a different name than the default.

## How does it work?

Kin.Zone is a fork of SearXNG, which is also a fork from the well-known <a href="https://github.com/searx/searx" target="_blank">searx</a> <a href="https://en.wikipedia.org/wiki/Metasearch_engine" target="_blank">metasearch engine</a> which was
inspired by the <a href="https://beniz.github.io/seeks/" target="_blank">Seeks project</a>.  It provides basic privacy by mixing your
queries with searches on other platforms without storing search data.  Kin.Zone and SearXNG
can be added to your browser's search bar; moreover, it can be set as the
default search engine.

The {{link('stats page', 'stats')}} contains some useful anonymous usage
statistics about the engines used.

## How can I make it my own?

Kin.Zone and SearXNG appreciates your concern regarding logs, so take the code from the <a href="https://github.com/mkmzone/kin.zone" target="_blank">Kin.Zone sources</a> or the
<a href="https://github.com/searxng/searxng/" target="_blank">SearXNG sources</a> and run it yourself!

Add your instance to this <a href="https://searx.space/" target="_blank">list of public
instances</a> to help other people
reclaim their privacy and make the internet freer.  The more decentralized the
internet is, the more freedom we have!


[SearXNG sources]: {{GIT_URL}}
[#searxng:matrix.org]: https://matrix.to/#/#searxng:matrix.org
[SearXNG docs]: {{get_setting('brand.docs_url')}}
[searx]: https://github.com/searx/searx
[metasearch engine]: https://en.wikipedia.org/wiki/Metasearch_engine
[Weblate]: https://translate.codeberg.org/projects/searxng/
[Seeks project]: https://beniz.github.io/seeks/
[OpenSearch]: https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md
[Firefox]: https://support.mozilla.org/en-US/kb/add-or-remove-search-engine-firefox
[Microsoft Edge]: https://support.microsoft.com/en-us/help/4028574/microsoft-edge-change-the-default-search-engine
[Chromium]: https://www.chromium.org/tab-to-search
