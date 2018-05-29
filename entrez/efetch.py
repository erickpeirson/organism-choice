def process_efetch_result(raw_result):
        """
        Metadata for each article should be stored in its own XML file.
        """
        root = ET.fromstring(raw_result.encode('utf-8'))
        for article in root.findall('PubmedArticle'):
            newTree = ET.ElementTree(element=copy.deepcopy(article))
            pmid = article.find('MedlineCitation/PMID').text

            treePath = build_path(term, year, '%s.xml' % pmid, OPATH, make=True)
            print '\rterm:', term, 'year:', year, 'pmid', pmid, 'to', treePath,
            newTree.write(treePath, encoding='utf-8')
