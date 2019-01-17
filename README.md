# Outrageous Orange - Hoarder

Downloads and stores data from various sources.

## Setup

Run the scripts from `cron`, e.g.
```
50 23 * * * cd ~/outrageous-orange/data && ../hoarder/dump-polisen-rss.sh || echo '[Error] Outrageous Orange: Polisen RSS' >&2
50 23 * * * cd ~/outrageous-orange/data && ../hoarder/dump-polisen-api.sh || echo '[Error] Outrageous Orange: Polisen API' >&2
```
