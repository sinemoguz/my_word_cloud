from keywordutil import *
from loggerinitializer import *


class WordCloudBuilder(object):
    def __init__(self, file_path, matcher_pattern, keyword_count):
        self.__file_path = file_path
        self.__matcher_pattern = matcher_pattern
        self.__keyword_count = keyword_count

    def build(self):
        keyword_dict = KeywordUtil.parse_from_input(self.__file_path, self.__matcher_pattern)
        selected_keyword_list = KeywordUtil.limit_dictionary_with_max(keyword_dict, self.__keyword_count)
        print(selected_keyword_list.__len__())


def main():
    initialize_logger()
    word_cloud_builder = WordCloudBuilder("PaperKeywords_TR.txt", "(.*)\t(.*)\t(.*)", 100)
    word_cloud_builder.build()

if __name__ == '__main__':
    main()
