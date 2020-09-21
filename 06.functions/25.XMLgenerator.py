"""
 Write a function, myxml, that allows you to create simple XML output. The output
from the function will always be a string. 
"""

def myxml(tag: str, val: str, **attr):
    attributes = ''
    if attr:
        attributes = ' '.join([f'{k}="{v}"' for k, v in attr.items()])
    return f"<{tag} {attributes}>{val}</{tag}>"

print(myxml('tagname', 'hello', a=1, b=2, c=3))
