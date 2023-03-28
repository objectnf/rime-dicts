import codecs
import sys
import re

latin = re.compile('^[a-zA-Z\u00C0-\u017F$\.\-]+$')

def main():
    new_f = codecs.open('easy_en.tmp', mode='w', encoding='UTF-8')
    with codecs.open(sys.argv[1], encoding='UTF-8') as f:
        for line in f:
            new_line = line
            new_line = new_line.replace('–', '-')
            substr = new_line.split('\t')
            for sub in tuple(substr):
                if latin.match(sub):
                    new_f.write(sub.lower() + '\n')
    new_f.close()

if __name__ == '__main__':
    main()