import codecs
import sys
import re

replace_char = [
    '_', ',', '!', '！', '\"', '“', '”', '，', '‘', '’', ';', ':', '/', '\\', 
    '：', '~', '～', '`', '=', '?', '(', ')', '（', '）', '%'
]

latin = re.compile('^[a-zA-Z\u00C0-\u017F$\.\-]+$')

def main():
    new_f = codecs.open('eng.tmp', mode='w', encoding='UTF-8')
    with codecs.open(sys.argv[1], encoding='UTF-8') as f:
        for line in f:
            new_line = line
            for rep in tuple(replace_char):
                new_line = new_line.replace(rep, ' ')
                new_line = new_line.replace('–', '-')
            substr = new_line.split(' ')
            for sub in tuple(substr):
                sub_line = sub.strip('.$')
                if latin.match(sub_line):
                    new_f.write(sub_line.lower() + '\n')
    new_f.close()

if __name__ == '__main__':
    main()