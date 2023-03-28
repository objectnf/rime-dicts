#!/bin/bash
# Vars
VERSION=20230320
FILENAMEEN=enwiki-$VERSION-all-titles-in-ns0
# Download enwiki
wget https://dumps.wikimedia.org/enwiki/$(VERSION)/$(FILENAMEEN).gz
gzip -k -d $FILENAMEEN.gz
# Process enwiki
python3 ./process-enwiki.py $FILENAMEEN
# easy_en: delete yaml header from easy_en.dict.yaml
# Process easy_en
python3 ./process-easyen.py easy_en.dict
# Concat
cat eng.tmp easy_en.tmp | sort -u > endict.tmp
# Final convert
python3 convert.py endict.tmp $VERSION