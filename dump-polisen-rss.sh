#!/bin/sh

while read loc1 loc2
do

	dir="rss/$loc1"
	mkdir -p "$dir"

	file="$dir/$(date -I).xml.gz"
	printf "%-40s " "$file"

	[ -f "$file" ] && echo 'Exists' && continue

	url="https://polisen.se/aktuellt/rss/$loc1/handelser-rss---$loc2/"
	curl -sS "$url" | gzip > "$file" && echo 'Downloaded'

done \
<<LOCATIONS
blekinge         blekinge
dalarna          dalarna
gotland          gotland
gavleborg        gavleborg
halland          halland
jamtland         jamtland
jonkopings-lan   jonkoping
kalmar-lan       kalmar-lan
kronoberg        kronoberg
norrbotten       norrbotten
skane            skane
stockholms-lan   stockholms-lan
sodermanland     sodermanland
uppsala-lan      uppsala-lan
varmland         varmland
vasterbotten     vasterbotten
vasternorrland   vasternorrland
vastmanland      vastmanland
vastra-gotaland  vastra-gotaland
orebro-lan       orebro-lan
ostergotland     ostergotland
LOCATIONS
