import operator
import pprint
import pycountry
from geotext import GeoText

with open('affiliations.csv', 'r') as inputfile:
    final = {}
    for line in inputfile:
        places = GeoText(line)
        if (places.countries != []):
            # GeoText was able to locate a country within the line
            # list could contain multiple countries, remove duplicates
            countries = set(places.countries)
            # add elements to dictionary
            for el in countries:
                if el in final:
                    final[el] += 1
                else:
                    final[el] = 1
        else:
            # GeoText not able to locate countries
            # either no country in text, or they use an abbreviation
            # like US for United States
            country_mentions = set(places.country_mentions.keys())
            countries = []
            for country in country_mentions:
                # convert something like U.S. to United States
                country_data = pycountry.countries.get(alpha_2=country)
                countries.append(country_data.name)
            countries = set(countries)
            # add elements to dictionary
            for el in countries:
                if el in final:
                    final[el] += 1
                else:
                    final[el] = 1
    # create sorted printout [Country, Total # of Appearances]
    sorted_d = sorted(final.items(), key=operator.itemgetter(1), reverse=True)
    pprint.pprint(sorted_d)
