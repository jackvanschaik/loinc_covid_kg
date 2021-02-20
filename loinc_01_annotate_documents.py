import urllib.request, urllib.error, urllib.parse
import json
import os
from pprint import pprint

API_KEY = "33e71ab2-159a-4a13-82f6-0ed8ff73ca9f"

def get_json(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

def annotate(text, rest_url = "http://data.bioontology.org", ontology = "LOINC"):
    text_parsed = urllib.parse.quote(text)
    result = get_json(rest_url + "/annotator?text=" + text_parsed + "&ontologies=" + ontology)
    return(result)

text = "Melanoma is a malignant tumor of melanocytes which are found predominantly in skin but also in the bowel and the eye."
res = annotate(text)

res
