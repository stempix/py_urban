from private.test_runner import test_runner

def single_root_words(root_word, *other_words):
    same_words = list()
    for word in other_words:
        if word.casefold() in root_word.casefold() or root_word.casefold() in word.casefold():
            same_words.append(word)
    return same_words

# Test data
test_data = (
    ['rich', 'richest', 'orichalcum', 'cheers', 'riches'],  # Test 1
    ['Disablement', 'Able', 'Mable', 'Disable', 'Bagel'],   # Test 2
    ['', 'One', 'Two', 'Three'],                            # Test 3
    [' ', ' One', 'Two ', 'Three', 'Fo ur'],                # Test 4
    ['Word', '', '', ''],                                   # Test 5
    ['Word'],                                               # Test 6
)
# Test expected results
test_expect = (
    ['richest', 'orichalcum', 'riches'],    # Test 1
    ['Able', 'Disable'],                    # Test 2
    ['One', 'Two', 'Three'],                # Test 3
    [' One', 'Two ', 'Fo ur'],              # Test 4
    ['', '', ''],                           # Test 5
    [],                                     # Test 6
)

test_runner(test_data, test_expect, single_root_words)