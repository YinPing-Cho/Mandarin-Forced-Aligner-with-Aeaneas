import re
def splittext(title):
    checklist=['。', '！', '？', '\n']
    with open(title, 'r', encoding="utf8") as istr:
        with open(title.replace('.txt', '_split.txt'), 'w', encoding="utf8") as ostr:
            for line in istr:
                line = re.sub(' ', '', line)
                line = re.sub('　', '', line)
                before = []
                for index, word in enumerate(line):
                    before.append(word)
                    nextword = line[(index + 1) % len(line)]
                    if (word in checklist and nextword != '」') or (word == '」' and line[index-1] in checklist):
                        if len(before) < 2:
                            continue
                        foo = ''
                        for w in before:
                            foo += w
                        if word != '\n':
                            foo += '\n'
                        before.clear()
                        ostr.write(str(foo))