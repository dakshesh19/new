from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# s1 = "Dakshesh"
# s2 = "Dakshesh Kashyap"
# print ("FuzzyWuzzy Ratio: ", fuzz.ratio(s1, s2))
# print ("FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2))
# print ("FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2))
# print ("FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2))
# print ("FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2),'\n\n')


# Str_A = 'FuzzyWuzzy is a lifesaver!'
# Str_B = 'fuzzy wuzzy is a LIFE SAVER.' 
# ratio = fuzz.ratio(Str_A.lower(), Str_B.lower())
# print('Similarity score: {}'.format(ratio))


# query = 'dakshesh'
# choices = ['dakshesh', 'daksh', 'daksgesg'] 
# print ("List of ratios: ")
# print (process.extract(query, choices), '\n')
# print ("Best among the above list: ",process.extractOne(query, choice


x = "i want a margarita pizza"
pizza_name = { 
    "margarita" : "100",
    "fresh pan" : "150",
    "veggie special" : "200",
    "farmhouse" : "250"
}

query = x
choices = pizza_name.keys()
print (process.extractOne(query, choices)[0])