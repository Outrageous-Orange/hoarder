#!/bin/sh

dir="rss/$(date -I)"
mkdir -p "$dir"

while read loc1 loc2
do
	file="$dir/$loc1.rss"
	echo "$file"
	url="https://polisen.se/aktuellt/rss/$loc1/handelser-rss---$loc2/"
	curl -sS "$url" >"$file"
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

tar="$dir.tar.gz"
tar czf "$tar" -C "$dir" . && echo "==> $tar" && rm -r "$dir"
