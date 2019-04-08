#надо повторить словари и csv
import re

#1
with open ('test2_mystem.xml', encoding='utf-8') as fh:
    file = fh.read()

st = re.search(
    r'<se>\n(.+)\n</se>',
    file,
    flags=re.DOTALL 
)

with open ('answer.txt', 'w', encoding='utf-8') as fh:
    x = st.group(1).splitlines()
    fh.write(str(len(x)))

#2
import collections

with open ('test2_mystem.xml', encoding='utf-8') as fh:
    file = fh.read()

gr_found = re.findall(
    r"""gr="(.+?)" """,
    file
)
with open ('answer.txt', 'w', encoding='utf-8') as fh:
    counter = collections.Counter(gr_found)
    for key in counter:
        fh.write(key)
        fh.write('\t')
        fh.write(str(counter[key]))
        fh.write('\n')

#3
import csv
with open ('test2_mystem.xml', encoding='utf-8') as fh:
    file = fh.read()

found = re.findall(
        r"""lex="(.+?)" gr="A=(?:.*?)жен(?:.*?)" """,
        file
)

with open ('answer.txt', 'w', encoding='utf-8') as fh:
    for word in found:
        fh.write(word)
        fh.write(' ')
