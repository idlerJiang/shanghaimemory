import ahocorasick


def build_actree(wordlist):
    actree = ahocorasick.Automaton()
    for index, word in enumerate(wordlist):
        actree.add_word(word, (index, word))
    actree.make_automaton()
    return actree


def censore(content):
    with open("Tencent.txt", "r", encoding='UTF-8') as f:
        wordlist = [word.lower() for word in f.read().splitlines()]
    actree = build_actree(wordlist=wordlist)
    sent = content.lower()
    sent_cp = sent
    for i in actree.iter(sent):
        sent_cp = sent_cp.replace(i[1][1], "**")
        print("检测到屏蔽词：", i[1][1])
    return sent_cp


if __name__ == '__main__':
   censore("content")
