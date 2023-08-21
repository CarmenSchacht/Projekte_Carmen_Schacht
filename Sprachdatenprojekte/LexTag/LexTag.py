import nltk
corp = nltk.corpus.ConllCorpusReader('.', 'tiger_release_aug07.corrected.16012013.conll09',
                                     ['ignore', 'words', 'ignore', 'ignore', 'pos'],
                                     encoding='utf-8')
import random

#Source: https://github.com/ptnplanet/NLTK-Contributions
tagged_sents = list(corp.tagged_sents())
random.shuffle(tagged_sents)

# set a split size: use 90% for training, 10% for testing
split_perc = 0.1
split_size = int(len(tagged_sents) * split_perc)
train_sents, test_sents = tagged_sents[split_size:], tagged_sents[:split_size]

from ClassifierBasedGermanTagger.ClassifierBasedGermanTagger import ClassifierBasedGermanTagger
tagger = ClassifierBasedGermanTagger(train=train_sents)


def evaluate(self, gold):
    return self.accuracy(gold)



def accuracy(self, gold):
    """
    Score the accuracy of the tagger against the gold standard.
    Strip the tags from the gold standard text, retag it using
    the tagger, then compute the accuracy score.

    :param gold: The list of tagged sentences to score the tagger on.
    :type gold: list(list(tuple(str, str)))
    :rtype: float
    """

    tagged_sents = self.tag_sents(untag(sent) for sent in gold)
    gold_tokens = list(chain.from_iterable(gold))
    test_tokens = list(chain.from_iterable(tagged_sents))
    return accuracy(gold_tokens, test_tokens)

print(tagger.tag(['Das', 'ist', 'ein', 'einfacher', 'Test']))