import re


class RegExHelper(object):
    def __init__(self, match_string):
        self.__match_string = match_string
        self.__rematch = None

    def match(self, regexp):
        self.__rematch = re.match(regexp, self.__match_string)
        return bool(self.__rematch)

    def group(self, i):
        if self.__rematch.group(i) is None:
            return ""
        else:
            return self.__rematch.group(i)

    def get_last_string(self):
        return self.__match_string
