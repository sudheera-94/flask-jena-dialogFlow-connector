# Import this to query the rdf in jena fuseki server
from SPARQLWrapper import SPARQLWrapper, JSON

# Import queries from this file
from SparqlQueries import *


# input :- Intent
# output :- answer
# Gets the intent, runs the correct query and passes the answer
def intentQueryMatcher(intent):
    sparql = SPARQLWrapper("http://localhost:3030/ds/query")
    sparql.setReturnFormat(JSON)

    if intent == "generalIntent-aboutCoronaIntent":
        sparql.setQuery(aboutCoronaIntentQuery)
    elif intent == "generalIntent-aboutCovidIntent":
        sparql.setQuery(aboutCovidIntentQuery)
    elif intent == "generalIntent-aboutVirusIntent":
        sparql.setQuery(aboutVirusIntentQuery)
    elif intent == "generalIntent-aboutTreatmentIntent":
        sparql.setQuery(aboutTreatmentIntentQuery)
    elif intent == "generalIntent-diffSarsIntent":
        sparql.setQuery(diffSarsIntentQuery)
    elif intent == "symptomsIntent-normalIntent":
        sparql.setQuery(normalIntentQuery)
    elif intent == "symptomsIntent-criticalIntent":
        sparql.setQuery(criticalIntentQuery)
    elif intent == "infectionPossibilitiesIntent-howIntent":
        sparql.setQuery(howIntentQuery)
    elif intent == "infectionPossibilitiesIntent-petIntent":
        sparql.setQuery(petIntentQuery)
    elif intent == "infectionPossibilitiesIntent-airIntent":
        sparql.setQuery(airIntentQuery)
    elif intent == "precautionsIntent-shouldIntent-healthyIntent":
        sparql.setQuery(healthyIntentQuery)
    elif intent == "precautionsIntent-shouldIntent-affectedIntent":
        sparql.setQuery(affectedIntentQuery)
    elif intent == "precautionsIntent-shouldIntent-seriousIntent":
        sparql.setQuery(seriousIntentQuery)
    elif intent == "precautionsIntent-riskIntent":
        sparql.setQuery(riskIntentQuery)
    elif intent == "precautionsIntent-maskIntent-shouldMaskIntent":
        sparql.setQuery(shouldMaskIntentQuery)
    elif intent == "precautionsIntent-maskIntent-whoMaskIntent":
        sparql.setQuery(whoMaskIntentQuery)
    elif intent == "precautionsIntent-maskIntent-howMaskIntent":
        sparql.setQuery(howMaskIntentQuery)
    elif intent == "precautionsIntent-shouldNotIntent":
        sparql.setQuery(shouldNotIntentQuery)
    elif intent == "biologicalIntent-partIntent":
        sparql.setQuery(partIntentQuery)
    elif intent == "biologicalIntent-lungsIntent":
        sparql.setQuery(lungsIntentQuery)
    elif intent == "biologicalIntent-immuneIntent":
        sparql.setQuery(immuneIntentQuery)
    elif intent == "biologicalIntent-bacteriaIntent":
        sparql.setQuery(bacteriaIntentQuery)
    else:
        return "Sorry, there is a bug in our system"

    results = sparql.query().convert()
    out = []

    for result in results["results"]["bindings"]:
        out.append(result["ans"]["value"])  # Here Y should be the answer use a common one called "ans"

    out = ', '.join(out)
    return out
