# Set of queries

# What is a Coronavirus?
aboutCoronaIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'Coronavirus'.
	?X covid:definition ?ans.
}"""

# What is Covid-19?
aboutCovidIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?X covid:definition ?ans.
}"""

# What is a virus?
aboutVirusIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'virus'.
	?X covid:definition ?ans.
}"""

# Is there a vaccine, drug or treatment?
aboutTreatmentIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?Y covid:helpsToCure ?X.
	?Y covid:definition ?ans.
}"""

# Are SARS and Covid-19 the same?
diffSarsIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'SARS'.
	?X covid:definition ?ans.
}"""

# What are the normal symptoms of corona virus?
normalIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'people have virus not serious'.
	?X covid:shows ?Y.
	?Y covid:common ?ans.
}"""

# What are the critical symptoms of covid-19?
criticalIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'people have virus and serious'.
	?X covid:shows ?Y.
	?Y covid:criticle ?ans.
}"""

# How does covid-19 spread?
howIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?X covid:spreadingSource ?ans.
}"""

# Can I catch covid-19 from my pet?
petIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'pets or animals'.
	?X covid:definition ?ans.
}"""

# Can covid-19 get airborn?
airIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?X covid:canItGetAirborn ?ans.
}"""

# What can I do to protect myself from this disease?
healthyIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'people'.
	?X covid:hasToTake ?Y.
	?Y covid:everyone ?ans.
}"""

# What are the things a person who has affected with covid-19 should do?
affectedIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'people have virus not serious'.
	?X covid:hasToTake ?Y.
	?Y covid:visitedPatientOrHaveSymptoms ?ans.
}"""

# What should a seriously affected person do?
seriousIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'people have virus and serious'.
	?X covid:hasToTake ?Y.
	?Y covid:withDevelopedFever ?ans.
}"""

# Who is at risk of developing severe illness?
riskIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?Y covid:hasHighRiskOfGetting ?X.
	?Y covid:name ?ans.
}"""

# Should I wear a mask to protect myself?
shouldMaskIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'mask'.
	?X covid:definition ?ans.
}"""

# Who should wear masks?
whoMaskIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'mask'.
	?Y covid:hasToWear ?X.
	?Y covid:name ?ans.
}"""

# How to wear a mask properly?
howMaskIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'mask'.
	?X covid:howToWear ?ans.
}"""

# Is there anything I should not do to protect myself?
shouldNotIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:name 'people'.
	?X covid:shouldNotDo ?Y.
	?Y covid:shouldNotDo ?ans.
}"""

# What body part will be affected by Covid-19?
partIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?X covid:attacks ?Y.
	?Y covid:name ?ans.
}"""

# How does it infect lungs?
lungsIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?X covid:connectsToReproduce ?Y.
	?Y covid:epithelialCells ?ans.
}"""

# How does Covid-19 turns your immune system against you?
immuneIntentQuery = """
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?X covid:confuses ?Y.
	?Y covid:immuneCells ?ans.
}"""

bacteriaIntentQuery = """
# Why bacteria infection with covid-19 can be deadly?
prefix covid: <http://covid19.rdf#>
SELECT ?ans
WHERE 
{
	?X covid:shortName 'Covid-19'.
	?Y covid:getsAdvantage ?X.
	?Y covid:bacteriaInfection ?ans.
}"""
