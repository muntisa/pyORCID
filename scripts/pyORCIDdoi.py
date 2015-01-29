# pyORCIDdoi = get DOI of your ORCID publications
# Author: Cristian R Muntenu (University of A Coruna, Spain)
# Contact: muntisa@gmail.com

# Usage:
# python pyORCIDdoi.py "[your ORCID]" > "[outputfile]"

# Example with my ORCID:
# python pyORCIDdoi.py "0000-0002-5628-2268" > "0000-0002-5628-2268doi.txt"

import urllib,sys
import xml.etree.ElementTree as ET

# Get ORCID REST output as XML file for a specific ORCID
def GetORCIDxml(myORCID):
    src = 'http://pub.orcid.org/v1.1/%s/orcid-works'
    urllib.urlretrieve(src % myORCID, myORCID+'.xml')
    return

# Convert XML to TEX format of ORCID publication file
def ORCIDdoi(myORCID):

    GetORCIDxml(myORCID) # Get XML file with ORCID publications
    
    tree = ET.parse(myORCID+".xml") # get the XML tree
    root = tree.getroot()           # fix the root
    
    # get all publications from the tree
    publis = root.findall('.//{http://www.orcid.org/ns/orcid}orcid-work')
    sOut="" # output text string
    for p in publis:
        # for each publication get the DOI
        try:
            pDOI= p.find('{http://www.orcid.org/ns/orcid}work-external-identifiers')
            sOut+= pDOI[0][1].text
        except:
            # if there is no DOI, get the citation
            pWork_citation= p.find('{http://www.orcid.org/ns/orcid}work-citation')
            sOut+=(pWork_citation[1].text).strip()
            # in addition, get the URL if exists!
            pURL= p.find('{http://www.orcid.org/ns/orcid}url')
            if pURL!= None:
                sOut+= (pURL.text).strip()
        sOut+="\n"
    # print the entire results
    print sOut.encode('UTF-8')
    return 

####################################################
# MAIN
####################################################

if __name__ == "__main__":
    print sys.argv[1]
    ORCIDdoi(sys.argv[1])


