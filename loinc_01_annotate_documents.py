# Imports ######################################################################
import json
import pysolr
import requests
import scispacy

# Functions ####################################################################
def post_annotate(text, api_key, ontology="LOINC"):
    url = "http://data.bioontology.org/annotator?ontologies" + ontology
    data = {'apikey':api_key, 'text':text}
    res = requests.post(url, data = data)
    return json.loads(res.text)
    

# Constants #################################################################### 
API_KEY = "33e71ab2-159a-4a13-82f6-0ed8ff73ca9f"

# Main #########################################################################
text = "Melanoma is a malignant tumor of melanocytes which are found predominantly in skin but also in the bowel and the eye."
#res = annotate(text)

solr = pysolr.Solr('http://192.168.1.36:8983/solr/')
result = solr.search('full_text:coronavirus')
txt = [r['full_text'] for r in result]
txt_0 = txt[0][0]

X = post_annotate(txt_0, API_KEY)
