import nltk
from nltk import tokenize, ChartParser, CFG, word_tokenize
from nltk.tree import Tree
from nltk.tokenize.treebank import TreebankWordTokenizer

# "which"をつかまえる
SAMPLE_1 = 'Where is the parcel which arrived this morning?'
# チャンク用
SAMPLE_2 = '"Michael and John is reading a booklet in a library of Jakarta"'

SAMPLE_3 = 'The little bear saw the fine fat trout in the brook.'


def print_if_has_in(pos, sentence):
    for p in pos:
        if p[1] == 'IN':
            print(p[0])
            print(sentence)
            return


def execute(text: str):
    groucho_grammer = CFG.fromstring("""
    S -> NP VP
    PP -> P NP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    Det -> 'an' | 'my'
    N -> 'elephant' | 'pajamas'
    V -> 'shot'
    P -> 'in'
    """)
    parser = ChartParser(groucho_grammer)

    tokens = word_tokenize(text=SAMPLE_3)
    print(type(tokens))
    print(tokens)
    for tree in parser.parse(
            tokens=[
                'The',
                'little',
                'bear',
                'saw',
                'the',
                'fine',
                'fat',
                'trout',
                'in',
                'the',
                'brook',
            ]):
        print(tree)


# text = open('sample.txt').read()
execute(text=SAMPLE_2)
