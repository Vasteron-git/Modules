
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = []
        self.set_file_name(*file_names)
    def set_file_name(self, *new_file_names):
        self.file_names = list(new_file_names)
    def get_all_words(self):
        dict = {}
        all_words = []
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                new_str_line = ""
                for line in file:
                    str_line = line.lower()
                    for i in str_line:
                        if i not in punctuation:
                            new_str_line += i
                dict[file_name] = new_str_line.split()
            return dict
    def find(self, word):
        for name, words in self.get_all_words().items():
            for elem in words:
                if word.lower() == elem:
                    return {name : words.index(elem) + 1}
    def count(self, word):
        for name, words in self.get_all_words().items():
            i = 0
            for elem in words:
                if word.lower() == elem:
                    i += 1
            return {name : i}

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
