import textwrap
def wrap(string, max_width):
    x=max_width
    s=textwrap.fill(string,x)
    return s
