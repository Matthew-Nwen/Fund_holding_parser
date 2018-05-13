Objective: Parse fund holdings pulled from EDGAR, given ticker or CIK

To run:
1) Install virtual env + program requirements
2) Run the script from the base directory with "python main.py [CIK/Ticker]"
3) Optionally, to parse all 13F forms, add another argument after the target!

Notes:
1) Modern 13F forms have a XML table, but older ones use a left-justified
ASCII table. The script handles and parses both programmatically!
2) The web scraper skips to the archived text document with a url trick.
3) Scraped data outputs onto a csv file with the first row being header info.
4) From my research, CIK requires ten digits or all mutual fund tickers have
five letters, ending in an x. I check for this, but it's really not necessary.

Future Plans:
1) Currently, the optional all parse argument system is crude. I'd update with
a system to find forms from a range or all before/after a period
2) Testing the web scraper proved a little more complex than I had thought. I'd
update the testing with something more substantial.
3) The last bit of the table header for voting authority is a little wordy.
4) There was a bit in the EDGAR spec about a value being stored as an XML attribute,
but I couldn't find any examples from the relevant period. Needs testing.

Thought Process:

So the first thing I need to do is import beautifulsoup4 and requests.
Request can be sent straight to EDGAR, and beautifulsoup4 parses it.
It looks like filtering to 13F is just another parameter, so that's nice.

On a successful request, we either get no matches found or a page with all
the document archive links on them.
1) The no match found seems to be just a h1 header.
2) Finding archive links is a little trickier. I decided to filter with a regex.

I initially tried to go through the links, but I found a shortcut with the url.
It seems one can go straight to the txt file of the archive by replacing the
url ending. From my site testing, it seems to work across examples.

Then, I need to find XML links and parse them into tab spaced text. Luckily,
I'm pretty sure there's a built-in library to handle that...

Parsing the XML was pretty easy by finding the infotable with bs4, but formatting
the data seems like it'll be a little tricky. I'm thinking that instead of using
tabs, I should left justify by a constant amount.

Additionally, I should probably write out to a csv file.

Heard back about the requirements of the scraper--of course I was supposed to
print out to a CSV file--I'll just blame that lapse on graduation coming up.
Luckily that made my output formatting worries pretty easy to calm.

Since I'm confident in my parse of 1.3 XMLs, I'm looking into older versions
as according to the published EDGAR specs. It looks like older XMLs are mostly
the same--just a sharesType as an attribute? Needs looking into.

Otherwise, pre-XML is done in ASCII tables. This might be annoying to parse.

The format is left-justified by the front of a column tag. Thus, I have to find
the justification of the data before parsing the lines of data. Luckily, it works
across all the examples I tested!

Overall, this was a fun project, and I'm confident in the quality of my work.
