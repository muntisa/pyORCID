# pyORCIDtex = get ORCID publication as Latex refereces
# Author: Cristian R Muntenu (University of A Coruna, Spain)
# Contact: muntisa@gmail.com

import urllib,sys
import xml.etree.ElementTree as ET

# Get ORCID REST output as XML file for a specific ORCID
def GetORCIDxml(myORCID):
    src = 'http://pub.orcid.org/v1.1/%s/orcid-works'
    urllib.urlretrieve(src % myORCID, myORCID+'.xml')
    return

# Convert XML to TEX format of ORCID publication file
def ORCIDcitations(myORCID):

    GetORCIDxml(myORCID) # Get XML file with ORCID publications
    
    tree = ET.parse(myORCID+".xml") # get the XML tree
    root = tree.getroot()           # fix the root
    
    # get all publications from the tree
    publis = root.findall('.//{http://www.orcid.org/ns/orcid}orcid-work')
    sOut="" # output text string
    for p in publis:
        # for each publication get the citation
        pWork_citation= p.find('{http://www.orcid.org/ns/orcid}work-citation')
        sOut+=(pWork_citation[1].text).strip()
        sOut+="\n\n" # print citation!
        print sOut.encode('UTF-8')
    return 

####################################################
# MAIN
####################################################

if __name__ == "__main__":
    print sys.argv[1]
    ORCIDcitations(sys.argv[1])


