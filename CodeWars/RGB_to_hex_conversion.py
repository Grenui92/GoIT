def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    return "{0:02x}{1:02x}{2:02x}".format(r, g, b).upper()
print(rgb(-20, 275, 125))
#00FF7D