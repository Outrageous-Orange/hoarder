# Outrageous Orange - Hoarder

Downloads and stores data from various sources.

## Setup

Run the scripts from `cron`, e.g.
```
50 23 * * * cd ~/outrageous-orange/data && ../hoarder/dump-polisen-rss.sh || echo '[Error] Outrageous Orange: Polisen RSS' >&2
50 23 * * * cd ~/outrageous-orange/data && ../hoarder/dump-polisen-api.sh || echo '[Error] Outrageous Orange: Polisen API' >&2
```

## Python Setup
To run the python parts of this repo you need to install python requirements:   

``` python
pip install -r requirements.txt
```

If you are introducing new dependencies, you can generate the `requirements.txt` file, using `pipreqs`:

``` python
sudo -H pip install pipreqs 
pipreqs . --force
```

## Scrap.py

`Scrap.py` is a small script that can scrap a url based on a set of patterns.


### Examples:
**Example 1**: BBC.com
``` sh
./scrap.py -u https://www.bbc.com/ -s "news://a[@class='media__link']/text()" "headline://a[@rev='news|headline']/text()" | jq
```

Which will result:
``` json
{
  "news": [
    "Hundreds missing after Brazil dam collapse",
    "FA Cup: Follow eight games including Man City v Burnley",
    "China’s sweet 700-year-old tradition",
    "The bad spending habits of retirees",
    "Are these musical myths true or false?",
    "Trump backs down to halt painful shutdown",
    "European leaders give Maduro ultimatum",
    "Body of missing Spanish boy found",
    "Jennings falls as England attempt to save game - listen to The Cricket Social",
    "Osaka wins Australian Open final thriller",
    "Cummins helps Australia thrash Sri Lanka",
    "What we know about gut health",
    "Why Scotland loves haggis",
    "Seven Japanese words to live by",
    "How people are 'ghosting' employers",
    "Seven off-the-grid sanctuary escapes",
    "What does a 100kcal snack look like?",
    "The weirdest food trends of the year",
    "A plastic alternative from olives?",
    "Could dancing pandas persuade you to buy new sports shoes?",
    "Hundreds missing after Brazil dam collapse",
    "Hundreds missing after Brazil dam collapse",
    "ICYMI: Snow sculpture and a robot hotel",
    "Anti-Brexit receipts cause stir for...",
    "'I will not give up until I get to the UK'",
    "'Hope I don’t get shot today at school’",
    "Boris Johnson struggles in interview",
    "Ready for the total solar eclipse?",
    "Koalas 'face extinction' in parts of...",
    "Video 'shows Mosul mosque's destruction'",
    "Indonesia's female 'devil wheel' riders",
    "Making a blockbuster in a week",
    "'I will be like my hero Ronaldinho'",
    "'Emiliano is out there somewhere'",
    "Indonesia flash flood sweeps away longhouse",
    "India sends 'lightest satellite' to space",
    "James Bulger film to remain in Oscars",
    "Microsoft's Bing restored in China",
    "Skinny genes the 'secret to staying slim'",
    "Tech Tent: The power of influencers",
    "Expedition targets Shackleton's lost ship",
    "Best image yet of 'space snowman'",
    "'Killed by injustice': The hanging of a British Somali",
    "Could women solve the global pilot shortage?",
    "Why Japan's stations are bathed in blue",
    "The best news photos from the past week",
    "Africa's top shots: Sailors, piercings and mannequins",
    "The purple bus feeding the homeless in Cardiff",
    "Unseen paintings of London's East End",
    "Shots of rare 'super blood wolf moon' eclipse"
  ],
  "big": [
    "Trump backs down to halt painful shutdown",
    "European leaders give Maduro ultimatum",
    "Body of missing Spanish boy found"
  ]
}
```

**Example 2**: polisen.se
``` sh
./scrap.py -u https://polisen.se/aktuellt/handelser/2019/januari/26/26-januari-01.18-narkotikabrott-falun/ -s "headline://div[@class='event-page editorial-content']/h1/text()" "preamble://p[@class='preamble']/text()" "body://div[@class='text-body editorial-html']/p/text()" | jq
```

Which will result:

``` json
{
  "headline": "26 januari 01.18, Narkotikabrott, Falun",
  "body": [
    "Vid kontroll visade  det sig att  han hade en mindre mängd misstänkt narkotika på sig. Detta beslagtogs av polispatrullen.",
    "Mannen är nu misstänkt för ringa narkotibrott."
  ],
  "preamble": "En man i 18-årsåldern misstänkt för narkotikabrott i anslutning till en krog i centrala Falun"
}
```