# Modified from: https://github.com/felixonmars/fcitx5-pinyin-zhwiki/blob/master/convert.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Usage:
#   convert.py input_filename
# input_filename is a file of Wikipedia article titles, one title per line.

import logging
import sys
import codecs

_LOG_EVERY = 1000

MAPPING = {
    "a": "ÀÁÂÃÄÅàáâãäåĀāĂăĄą",
    "ae": "Ææ",
    "ss": "ß",
    "c": "ÇçĆćĈĉĊċČč",
    "d": "ÐðĎďĐđ",
    "e": "ÈÉÊËèéêëĒēĔĕĖėĘęĚě",
    "f": "ſ",
    "g": "ĜĝĞğĠġĢģ",
    "h": "ĤĥĦħ",
    "i": "ÌÎÎÏìíîïĨĩĪīĬĭĮįİı",
    "j": "Ĵĵ",
    "ij": "Ĳĳ",
    "k": "Ķķĸ",
    "l": "ĹĺĻļĽľĿŀŁł",
    "n": "ÑñŃńŅņŇňŉŊŋ",
    "o": "ÒÓÔÕÖØòóôõöøŌōŎŏŐő",
    "oe": "Œœ",
    "th": "Þþ",
    "r": "ŔŕŖŗŘř",
    "s": "$ŚśŜŝŞşŠš",
    "t": "ŢţŤťŦŧ",
    "u": "ÙÚÛÜùúûüŨũŪūŬŭŮůŰűŲų",
    "w": "Ŵŵ",
    "x": "×",
    "y": "ÝýÿŶŷŸ",
    "z": "ŹźŻżŽž"
}

# 1080000/3
MAXLINE = 360000

logging.basicConfig(level=logging.INFO)


def log_count(count):
    logging.info(f"{count} words generated")


def make_output(word, input):
    return "\t".join([word, input])

def new_file(filenum, version):
    f = codecs.open("endict_part" + str(filenum) + ".dict.yaml", mode="w", encoding="UTF-8")
    f.write("---\nname: endict_part" + str(filenum) + "\nversion: \"" + str(version) + "\"\nsort: by_weight\n...\n\n")
    return f

def main():
    # Line and file counting
    result_count = 0
    filenum = 1
    version = sys.argv[2]

    # Open file
    with codecs.open(sys.argv[1], encoding="UTF-8") as f:
        for line in f:
            # Split file
            if result_count % MAXLINE == 0:
                if 'new_f' in locals():
                    new_f.write("\n")
                    new_f.close()
                new_f = new_file(filenum, version)
                filenum += 1
            line_stroke = ""
            for i in range(len(line)):
                skip = False
                # Replace Latin Characters
                for key, val in MAPPING.items():
                    if line[i] in val:
                        line_stroke += key
                        skip = True
                        break
                # Keep . and -
                if line[i] in "-.":
                        skip = True
                if not skip:
                    line_stroke += line[i]
            # Count +1
            result_count += 1
            # Remove tailing space
            line = line.strip()
            line_stroke = line_stroke.strip()
            # No stroke. e.g.: -----
            if len(line_stroke) == 0:
                continue
            new_f.write(make_output(line, line_stroke) + "\n")
            # Dict has three styles of one word: Like this, This and THIS
            if len(line) >= 2:
                line = line[0].upper() + line[1:]
                line_stroke = line_stroke[0].upper() + line_stroke[1:]
                new_f.write(make_output(line, line_stroke) + "\n")
            line = line.upper()
            line_stroke = line_stroke.upper()
            new_f.write(make_output(line, line_stroke) + "\n")
            if result_count % _LOG_EVERY == 0:
                log_count(result_count)
    log_count(result_count)
    new_f.close()


if __name__ == "__main__":
    main()
