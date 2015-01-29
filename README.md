**ORCID info from Python**

*pyORCIDrefs.py* = Get ORCID publications using ORCID REST xml output using Python

Outputs: your output file with the references and the original xml file from ORCID

Command line:

> python pyORCIDrefs.py "[your ORCID]" > "[outputfile]"


Example with my ORCID:

> python pyORCIDrefs.py "0000-0002-5628-2268" > "0000-0002-5628-2268refs.txt"

- The references in the output file are in general in BibTeX format.
- There is no error checkings in the first version.



*python pyORCIDdoi.py* = Get DOI list for your ORCID publications

Command line:

> python pyORCIDdoi.py "[your ORCID]" > "[outputfile]"


Example with my ORCID:

> python pyORCIDdoi.py "0000-0002-5628-2268" > "0000-0002-5628-2268doi.txt"

(RNASA-IMEDIR, Computer Science Faculty, University of A Coruna, Spain)
