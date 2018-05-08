Objective: Parse fund holdings pulled from EDGAR, given ticker or CIK

So the first thing I need to do is import beautifulsoup4 and requests.
Request can be sent straight to EDGAR, and beautifulsoup4 parses it.
It looks like filtering to 13F is just another parameter, so that's nice.

On a successful request, we either get no matches found or a page with all
the document archive links on them.
1) The no match found seems to be just a h1 header.
2) Finding archive links is a little trickier. I can filter out links, but...

Then, I need to find XML links and parse them into tab spaced text.
