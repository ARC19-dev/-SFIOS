from core import *
import re
# String 

txt = "todo: Hell Yeah"
str = """

tood: Fuck all codes

todo: Open my notebook"

todo: Learn js.

fixme: this function doesn't work

"""



m = re.findall("(.*):(.*)", str)
# m = re.findall("todo:(.*)", str)

print(m)
# if m:
    # print(m[0])

def search(texts):
    for text in texts:
        for line in text:
            a = re.split("\s", line)
            if 'todo' and ':' in a[:2]:
                print(a[2:-1])


# search(str)
