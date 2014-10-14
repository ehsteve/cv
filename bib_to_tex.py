import bibtexparser
from bibtexparser.bparser import BibTexParser

with open('publications.bib') as bibfile:
    parser = BibTexParser()
    bib_database = bibtexparser.load(bibfile, parser=parser)

print(bib_database.entries[0]['pdfurl'])
def convert_ads_journal_code(code):
    conversion_dict = {'solphys':'Sol. Phys.', 'apj':'ApJ', 'ssr':'Space Sci. Rev.', 'aap':'A&A', 'apjl':'ApJ'}
    return conversion_dict.get(code[1:], code)

with open('publications.md', "w") as markdown_publication:
    markdown_publication.write("Publication List\n")
    markdown_publication.write("================\n")
    current_year = bib_database.entries[0]['year']
    markdown_publication.write(current_year + "\n----\n")
    for entry in bib_database.entries:
        this_year = entry['year']
        print(entry['title'])
        if this_year != current_year:
            current_year = this_year
            markdown_publication.write("\n" + current_year + "\n----\n")
        cleaned_author_list = entry['author'].replace('{', "").replace('}','').replace('~', ' ').replace(' and ', '; ').replace("\t", '')
        publication = convert_ads_journal_code(entry.get('journal', entry.get('booktitle')))

        publication_line = "* "
        if entry.get('adsurl', '') != "":
            publication_line = "%s [%s](%s)" % (publication_line, entry['title'], entry.get('adsurl', ''))
        else:
            publication_line = "%s %s" % (publication_line, entry['title'])

        publication_line = "%s, %s, **%s**, %s" % (publication_line, cleaned_author_list, publication, entry['year'])

        if entry.get('doi', '') != "":
            publication_line = "%s, %s" % (publication_line, entry['doi'])

        if entry.get('pdfurl', '') != '':
            publication_line = "%s, [pdf](%s)" % (publication_line, entry['pdfurl'])

        markdown_publication.write(publication_line + '\n')