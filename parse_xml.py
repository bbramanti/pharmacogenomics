import re


def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


with open('pubmed.xml', 'r') as inputfile:
    append = False
    authorList = False
    affiliation = ""
    for line in inputfile:
        # found opening AuthorList Tag, set flag
        if "<AuthorList CompleteYN=\"Y\">" in line:
            authorList = True

        # found the first affiliation tag
        if authorList and "<Affiliation>" in line:
            # we have drilled down to proper level
            # set append flag to start collecting the information
            append = True

        # found the end of the affiliation
        if authorList and "</Affiliation>" in line:
            affiliation += line.strip()
            append = False
            authorList = False
            # clean up the affiliation, remove tags
            clean = remove_html_tags(affiliation)
            print (clean)
            affiliation = ""

        # found closing AuthorList Tag, return flag to False
        if "</AuthorList>" in line:
            authorList = False

        # append flag is set, add to the affiliation
        if append:
            affiliation += line.strip()
