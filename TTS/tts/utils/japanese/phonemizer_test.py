import unittest
from .phonemizer import japanese_text_to_phonemes

_TEST_CASES = '''
どちらに行きますか？/dochiraniikimasuka?
今日は温泉に、行きます。/kyo:waoNseNni,ikimasu.
「A」から「Z」までです。/AkaraZmadedesu.
そうですね！/so:desune!
クジラは哺乳類です。/kujirawahonyu:ruidesu.
ヴィディオを見ます。/bidioomimasu.
'''

class TestPhonemizer(unittest.TestCase):

    def test_phonemizer(self):
        for line in _TEST_CASES.strip().split('\n'):
            text, phonemes = line.split('/')
            self.assertEqual(japanese_text_to_phonemes(text), phonemes)

if __name__ == '__main__':
    unittest.main()