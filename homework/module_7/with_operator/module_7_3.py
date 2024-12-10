class WordsFinder:

    __PUNCTUATION_SIGNS = (',', '.', '=', '!', '?', ';', ':', '-')

    def __init__(self, *file_names):
        self.file_names = []
        for file in file_names:
            self.file_names.append(file)

    def __erase_punctuation(self, text):
        for sign in self.__PUNCTUATION_SIGNS:
            text = text.replace(sign, ' ')
        return text

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file_words = []
                for line in file:
                    file_words.extend(self.__erase_punctuation(line).split())
                all_words[file_name] = file_words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word_positions = dict()
        for file_name, words in all_words.items():
            for word_idx in range(len(words)):
                if words[word_idx].casefold() == word.casefold():
                    word_positions[file_name] = word_idx + 1
                    break
        return word_positions

    def count(self, word):
        all_words = self.get_all_words()
        word_counts = dict()
        for file_name, words in all_words.items():
            word_cnt = 0
            for file_word in words:
                if word.casefold() == file_word.casefold():
                    word_cnt += 1
            word_counts[file_name] = word_cnt
        return word_counts

# Форматирование вывода
bold_start = "\033[1m"
green_text = "\033[32m"
blue_text = "\033[34m"
res_set = "\033[0m"

print(f"{bold_start}{green_text}Тестирование файла 'test_file.txt': {res_set}")
finder1 = WordsFinder('test_file.txt')
print(f'{blue_text}\t', finder1.get_all_words())
print(f'\t', finder1.find('TEXT'))
print(f'\t', finder1.count('teXT'), f'{res_set}')

print(f"{bold_start}{green_text}Тестирование файла 'Mother Goose - Monday’s Child.txt': {res_set}")
finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(f'{blue_text}\t', finder2.get_all_words())
print(f'\t', finder2.find('Child'))
print(f'\t', finder2.count('Child'), f'{res_set}')

print(f"{bold_start}{green_text}Тестирование файла 'Rudyard Kipling - If.txt': {res_set}")
finder3 = WordsFinder('Rudyard Kipling - If.txt')
print(f'{blue_text}\t', finder3.get_all_words())
print(f'\t', finder3.find('if'))
print(f'\t', finder3.count('if'), f'{res_set}')

print(f"{bold_start}{green_text}Тестирование файла 'Walt Whitman - O Captain! My Captain!.txt': {res_set}")
finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(f'{blue_text}\t', finder4.get_all_words())
print(f'\t', finder4.find('captain'))
print(f'\t', finder4.count('captain'), f'{res_set}')

print(f"{bold_start}{green_text}Тестирование всех файлов единовременно: {res_set}")
finder5 = WordsFinder(
    'test_file.txt',
    'Mother Goose - Monday’s Child.txt',
    'Rudyard Kipling - If.txt',
    'Walt Whitman - O Captain! My Captain!.txt'
)
print(f'{blue_text}\t', finder5.get_all_words())
print(f'\t', finder5.find('the'))
print(f'\t', finder5.count('the'), f'{res_set}')