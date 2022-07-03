# s = "this is My First Python programming class and i am learNING python string and its function"
# 1 . Try to extract data from index one to index 300 with a jump of 3
# 2. Try to reverse a string without using reverse function
# 3. Try to split a string after conversion of entire string in uppercase
# 4. try to convert the whole string into lower case
# 5 . Try to capitalize the whole string
# 6. Try to give an example of expand tab
# 7 . Give an example of strip , lstrip and rstrip

import logging as lg


class string:
    def __init__(self, s):
        self.s = s

    lg.basicConfig(filename="string.log", level=lg.INFO, format='%(levelname)s %(name)s %(asctime)s %(message)s')
    lg.basicConfig(filename="string.log", level=lg.ERROR, format='%(levelname)s %(name)s %(asctime)s %(message)s')
    f = open("string.log", "r+")
    f.seek(0)
    f.truncate()
    try:
        def extract_str(self):
            a = self.s[0:300:3]
            print(a)
            lg.info(a)
    except Exception as e:
        lg.error(e)
    try:
        def reverse_str(self):
            a = self.s[-1:-301:-1]
            lg.info(a)
    except Exception as e:
        lg.error(e)
    try:
        def split_upper_case(self):
            a = str(self.s).upper().split()
            lg.info(a)
    except Exception as e:
        lg.error(e)
    try:
        def lower_case(self):
            a = str(self.s).lower()
            lg.info(a)
    except Exception as e:
        lg.error(e)
    try:
        def capitalize(self):
            a = str(self.s).capitalize()
            lg.info(a)
    except Exception as e:
        lg.error(e)
    try:
        def expand_tab(self):
            a = str(self.s).replace(" ", "")
            b = a.replace("", "\t")
            lg.info(b.expandtabs(2))
    except Exception as e:
        lg.error(e)
    try:
        def strip_text(self):
            a="----"+str(self.s)+"----"
            lg.info(a)
            lg.info(a.strip("-"))
    except Exception as e:
        lg.error(e)
    try:
        def left_strip_text(self):
            a="----"+str(self.s)+"----"
            lg.info(a)
            lg.info(a.lstrip("-"))
    except Exception as e:
        lg.error(e)
    try:
        def right_strip_text(self):
            a="----"+str(self.s)+"----"
            lg.info(a)
            lg.info(a.rstrip("-"))
    except Exception as e:
        lg.error(e)
stat = string("this is My First Python programming class and i am learNING python string and its function")
stat.extract_str()
stat.reverse_str()
stat.split_upper_case()
stat.lower_case()
stat.capitalize()
stat.expand_tab()
stat.strip_text()
stat.left_strip_text()
stat.right_strip_text()
