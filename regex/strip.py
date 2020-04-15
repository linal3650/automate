import re

def regexstrip(string, _strip=None):
    _strip = r"\A[\s{0}]+|[\s{0}]+\Z".format(re.escape(_strip)) if _strip else r"\A\s+|\s+\Z"
    #print(_strip)
    return re.sub(_strip, '', string)

print(regexstrip(" ([no more stripping']  )  ", " ()[]'"))
# \A[\s\ \(\)\[\]\']+|[\s\ \(\)\[\]\']+\Z
# no more stripping
print(regexstrip(" ([no more stripping']  )  "))
# \A\s+|\s+\Z
# ([no more stripping']  )
