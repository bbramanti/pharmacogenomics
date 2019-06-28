import operator
import pprint

search_terms = ["University", "university", "Universitat"]
with open('affiliations.csv', 'r') as inputfile:
    final = {}
    # read each entry of affiliations file
    for line in inputfile:
        split = line.rstrip().split(",")
        for el in split:
            # if entry contains any of the search terms, update dictionary
            if any(x in el for x in search_terms):
                if el.strip() in final:
                    final[el.strip()] += 1
                else:
                    final[el.strip()] = 1
            # only need one university per entry, move to next entry
            break
    # create sorted printout [University_Name, Total # of Appearances]
    sorted_d = sorted(final.items(), key=operator.itemgetter(1), reverse=True)
    pprint.pprint(sorted_d)
