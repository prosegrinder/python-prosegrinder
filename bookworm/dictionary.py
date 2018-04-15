# -*- coding: utf-8 -*-

import re

import cmudict

from bookworm import Word


class Dictionary:
    """A reference containing Words."""

    # See: https://en.wikipedia.org/wiki/List_of_Unicode_characters
    RE_WORD = re.compile(
        "[\\w’'\u0391-\u03ce\u0400-\u0481\u048a-\u04ff]+")

    RE_NUMERIC = re.compile("^[+-]{0,1}\\d{1,3}(?:[,]\\d{3})*(?:[.]\\d*)*$")

    # See: http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/
    RE_VOWELS = re.compile('[^aeiouy]+')

    # See: http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/
    RE_SUB_SYLLABLES = [
        re.compile('cial'),
        re.compile('tia'),
        re.compile('cius'),
        re.compile('cious'),
        re.compile('uiet'),
        re.compile('gious'),
        re.compile('geous'),
        re.compile('priest'),
        re.compile('giu'),
        re.compile('dge'),
        re.compile('ion'),
        re.compile('iou'),
        re.compile('sia$'),
        re.compile('.che$'),
        re.compile('.ched$'),
        re.compile('.abe$'),
        re.compile('.ace$'),
        re.compile('.ade$'),
        re.compile('.age$'),
        re.compile('.aged$'),
        re.compile('.ake$'),
        re.compile('.ale$'),
        re.compile('.aled$'),
        re.compile('.ales$'),
        re.compile('.ane$'),
        re.compile('.ame$'),
        re.compile('.ape$'),
        re.compile('.are$'),
        re.compile('.ase$'),
        re.compile('.ashed$'),
        re.compile('.asque$'),
        re.compile('.ate$'),
        re.compile('.ave$'),
        re.compile('.azed$'),
        re.compile('.awe$'),
        re.compile('.aze$'),
        re.compile('.aped$'),
        re.compile('.athe$'),
        re.compile('.athes$'),
        re.compile('.ece$'),
        re.compile('.ese$'),
        re.compile('.esque$'),
        re.compile('.esques$'),
        re.compile('.eze$'),
        re.compile('.gue$'),
        re.compile('.ibe$'),
        re.compile('.ice$'),
        re.compile('.ide$'),
        re.compile('.ife$'),
        re.compile('.ike$'),
        re.compile('.ile$'),
        re.compile('.ime$'),
        re.compile('.ine$'),
        re.compile('.ipe$'),
        re.compile('.iped$'),
        re.compile('.ire$'),
        re.compile('.ise$'),
        re.compile('.ished$'),
        re.compile('.ite$'),
        re.compile('.ive$'),
        re.compile('.ize$'),
        re.compile('.obe$'),
        re.compile('.ode$'),
        re.compile('.oke$'),
        re.compile('.ole$'),
        re.compile('.ome$'),
        re.compile('.one$'),
        re.compile('.ope$'),
        re.compile('.oque$'),
        re.compile('.ore$'),
        re.compile('.ose$'),
        re.compile('.osque$'),
        re.compile('.osques$'),
        re.compile('.ote$'),
        re.compile('.ove$'),
        re.compile('.pped$'),
        re.compile('.sse$'),
        re.compile('.ssed$'),
        re.compile('.ste$'),
        re.compile('.ube$'),
        re.compile('.uce$'),
        re.compile('.ude$'),
        re.compile('.uge$'),
        re.compile('.uke$'),
        re.compile('.ule$'),
        re.compile('.ules$'),
        re.compile('.uled$'),
        re.compile('.ume$'),
        re.compile('.une$'),
        re.compile('.upe$'),
        re.compile('.ure$'),
        re.compile('.use$'),
        re.compile('.ushed$'),
        re.compile('.ute$'),
        re.compile('.ved$'),
        re.compile('.we$'),
        re.compile('.wes$'),
        re.compile('.wed$'),
        re.compile('.yse$'),
        re.compile('.yze$'),
        re.compile('.rse$'),
        re.compile('.red$'),
        re.compile('.rce$'),
        re.compile('.rde$'),
        re.compile('.ily$'),
        re.compile('.ely$'),
        re.compile('.des$'),
        re.compile('.gged$'),
        re.compile('.kes$'),
        re.compile('.ced$'),
        re.compile('.ked$'),
        re.compile('.med$'),
        re.compile('.mes$'),
        re.compile('.ned$'),
        re.compile('.[sz]ed$'),
        re.compile('.nce$'),
        re.compile('.rles$'),
        re.compile('.nes$'),
        re.compile('.pes$'),
        re.compile('.tes$'),
        re.compile('.res$'),
        re.compile('.ves$'),
        re.compile('ere$')
    ]

    # See: http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/
    RE_ADD_SYLLABLES = [
        re.compile('ia'),
        re.compile('riet'),
        re.compile('dien'),
        re.compile('ien'),
        re.compile('iet'),
        re.compile('iu'),
        re.compile('iest'),
        re.compile('io'),
        re.compile('ii'),
        re.compile('ily'),
        re.compile('.oala$'),
        re.compile('.iara$'),
        re.compile('.ying$'),
        re.compile('.earest'),
        re.compile('.arer'),
        re.compile('.aress'),
        re.compile('.eate$'),
        re.compile('.eation$'),
        re.compile('[aeiouym]bl$'),
        re.compile('[aeiou]{3}'),
        re.compile('^mc'),
        re.compile('ism'),
        re.compile('^mc'),
        re.compile('asm'),
        re.compile('([^aeiouy])1l$'),
        re.compile('[^l]lien'),
        re.compile('^coa[dglx].'),
        re.compile('[^gq]ua[^auieo]'),
        re.compile('dnt$')
    ]

    def __init__(self, cache=None):
        self._cmudict = cmudict.dict()
        self._cache = cache

    def _syllable_count(self, word):
        syllables = 0
        if word in self._cmudict:
            phones = self._cmudict[word][0]
            # There's a more Pythonic way of doing this.
            for phone in phones:
                syllables += len(re.sub("[^012]", "", phone))
        else:
            syllables = self._heuristic_syllable_count(word)
        return syllables

    def _heuristic_syllable_count(self, word):
        # See: http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/
        parts = re.split(Dictionary.RE_VOWELS, word)
        valid_parts = []
        for part in parts:
            if part != '':
                valid_parts.append(part)
        syllables = 0

        for regex in Dictionary.RE_ADD_SYLLABLES:
            match = 0 if re.match(regex, word) is None else 1
            syllables += match
        for regex in Dictionary.RE_SUB_SYLLABLES:
            match = 0 if re.match(regex, word) is None else 1
            syllables -= 1

        syllables = 1 if syllables == 0 else syllables

        return syllables

    def _is_numeric(self, word):
        return re.match(Dictionary.RE_NUMERIC, word)

    def get_word(self, word):
        pass