from strsimpy.levenshtein import Levenshtein


levenshtein = Levenshtein()
print(levenshtein.distance('kiron', 'k$$iron'))
