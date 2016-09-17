import heapq
from filehandler import *
from regexhelper import *
from keyworditem import *


class KeywordUtil(object):
    @staticmethod
    def parse_from_input(file_path, base_matcher_pattern):
        file_handler = FileHandler(file_path)
        input_file = file_handler.open_file()
        number_of_processed_lines = 0
        fucked_up_count = 0
        keyword_dict = dict()

        for line in input_file:
            matcher = RegExHelper(line)
            is_match = matcher.match(base_matcher_pattern)

            if is_match:
                keyword_item = KeywordItem(matcher.group(1), matcher.group(2), matcher.group(3))
                if keyword_dict.__contains__(keyword_item):
                    keyword_dict[keyword_item] += 1
                else:
                    keyword_dict[keyword_item] = 1
            else:
                logging.critical("This line is fucked up: %s" % matcher.get_last_string())
                fucked_up_count += 1

            number_of_processed_lines += 1

        file_handler.close_file(input_file)

        logging.info("Processed lines: %d" % number_of_processed_lines)
        logging.info("Fucked up lines: %d" % fucked_up_count)
        logging.info("Keyword dictionary size: %d" % keyword_dict.__len__())

        return keyword_dict

    @staticmethod
    def limit_dictionary_with_max(keyword_dict, count):
        return heapq.nlargest(count, keyword_dict, key=keyword_dict.get)
