import re
# String 

str = """

tood: Fuck all codes

todo: Open my notebook"

todo: Learn js.

fixme: this function doesn't work

"""



m = re.match('ptr', str)

print(m)