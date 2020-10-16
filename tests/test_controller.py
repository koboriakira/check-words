from my_dictionary.controller import analyse, add_word_list


# def test_execute():
#     text = 'That is the house that house room.'
#     actual = analyse(text=text)
#     expect = {
#         'morphied_word_dict': {
#             'house': 2,
#             'be': 1,
#             'room': 1},
#         'ngsl_word_list': [
#             'be',
#             'house',
#             'room'],
#         'not_ngsl_word_list': []}

#     assert actual == expect

def test_add_word_list():
    url = 'https://example.com/dir/entry/'
    ngsl_words = ['the']
    not_ngsl_words = ['tightend']
    add_word_list(
        url=url,
        ngsl_words=ngsl_words,
        not_ngsl_words=not_ngsl_words)
    assert False
