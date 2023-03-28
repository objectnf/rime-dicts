# Modified from https://github.com/felixonmars/fcitx5-pinyin-zhwiki/blob/master/Makefile

VERSION=20230320
FILENAMEZH=zhwiki-$(VERSION)-all-titles-in-ns0
FILENAMEEN=enwiki-$(VERSION)-all-titles-in-ns0
FILENAMEJP=jawiki-$(VERSION)-all-titles-in-ns0

colon := :
$(colon) := :

all: build

build: zhwiki.dict enwiki.dict jawiki.dict

download:
	wget https://dumps.wikimedia.org/zhwiki/$(VERSION)/$(FILENAMEZH).gz
	wget https://dumps.wikimedia.org/enwiki/$(VERSION)/$(FILENAMEEN).gz
	wget https://dumps.wikimedia.org/jawiki/$(VERSION)/$(FILENAMEJP).gz

extract: download
	gzip -k -d $(FILENAMEZH).gz
	gzip -k -d $(FILENAMEEN).gz
	gzip -k -d $(FILENAMEJP).gz

zhwiki.dict:
    python3 ./convert.py $(FILENAMEZH) > zhwiki.raw.tmp
	sort -u zhwiki.raw.tmp > zhwiki.raw
	rm -f zhwiki.raw.tmp
	sed 's/[ ][ ]*/\t/g' zhwiki.raw > zhwiki.rime.raw
	echo -e '---\nname: zhwiki\nversion: "$(VERSION)"\nsort: by_weight\n...\n' >> zhwiki.dict.yaml
	cat zhwiki.rime.raw >> zhwiki.dict.yaml
