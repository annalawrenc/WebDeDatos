"""
@author: U{Nines Sanguino}
@version: 0.2
@since: 20Jun2015
"""

__version__ = '0.2'
__modified__ = '20Jun2015'
__author__ = 'Nines Sanguino'
from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDF
import xml.dom.minidom



def getLocalLabel (instancia):
 
 	sparqlSesame = SPARQLWrapper("http://localhost:8080/openrdf-sesame/repositories/SocialNetwork",  returnFormat=JSON)
	queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX sn:  <http://ciff.curso2015/ontologies/owl/socialNetwork#> SELECT ?label WHERE { sn:" + instancia + " rdfs:label ?label }"
	sparqlSesame.setQuery(queryString)
	sparqlSesame.setReturnFormat(JSON)
	query   = sparqlSesame.query()
	results = query.convert()
	devolver = []
	for result in results["results"]["bindings"]:
		label = result["label"]["value"]
		if 'xml:lang' in result["label"]:
			lang = result["label"]["xml:lang"]
		else:
			lang = None
		print "The label: " + label
		if 'xml:lang' in result["label"]:
			print "The lang: " + lang
		devolver.append((label, lang))
	return devolver


	
def getDBpediaResource (label, lang, endpoint):

	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . ?s rdf:type foaf:Person} " 
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?s WHERE { ?s rdfs:label \"" + label + "\" . ?s rdf:type foaf:Person } " 
	
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "The resource: " + resource

def getLinkedmdbResource (label, lang, endpoint):

	sparqlLinkedmdb = SPARQLWrapper(endpoint)

	if (lang):
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> SELECT ?s WHERE { ?s dc:title \"" + label + "\"@" +lang + "}" 
	
	else:
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> SELECT ?s WHERE { ?s dc:title \"" + label + "\" }" 
	
	sparqlLinkedmdb.setQuery(queryString)
	sparqlLinkedmdb.setReturnFormat(JSON)
	query   = sparqlLinkedmdb.query()
	results = query.convert()
	print
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "->The resource: " + resource

def getLinkedmdbMovieDirector (label, lang, endpoint):

	sparqlLinkedmdb = SPARQLWrapper(endpoint)

	if (lang):
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?s WHERE {movie:director_name foaf:made <http://data.linkedmdb.org/resource/film/2>}" 
	
	else:
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?s WHERE {movie:director_name foaf:made <http://data.linkedmdb.org/resource/film/2>}" 
	
	sparqlLinkedmdb.setQuery(queryString)
	sparqlLinkedmdb.setReturnFormat(JSON)
	query   = sparqlLinkedmdb.query()
	results = query.convert()
	print
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "->Director: " + resource
		
def getLinkedmdbMovieDate (label, lang, endpoint):

	sparqlLinkedmdb = SPARQLWrapper(endpoint)

	if (lang):
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?o WHERE { ?s dc:title \"" + label + "\"@" +lang + ". ?s movie:initial_release_date ?o}" 
	
	else:
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?o WHERE { ?s dc:title \"" + label + "\" . ?s movie:initial_release_date ?o}" 
	
	sparqlLinkedmdb.setQuery(queryString)
	sparqlLinkedmdb.setReturnFormat(JSON)
	query   = sparqlLinkedmdb.query()
	results = query.convert()
	print
	for result in results["results"]["bindings"]:
		resource = result["o"]["value"]
		print "->Date: " + resource

def getLinkedmdbMovieRunTime (label, lang, endpoint):

	sparqlLinkedmdb = SPARQLWrapper(endpoint)

	if (lang):
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?o WHERE { ?s dc:title \"" + label + "\"@" +lang + ". ?s movie:runtime ?o}" 
	
	else:
		queryString = "PREFIX dc: <http://purl.org/dc/terms/> PREFIX movie: <http://data.linkedmdb.org/resource/movie/> SELECT ?o WHERE { ?s dc:title \"" + label + "\" . ?s movie:runtime ?o}" 
	
	sparqlLinkedmdb.setQuery(queryString)
	sparqlLinkedmdb.setReturnFormat(JSON)
	query   = sparqlLinkedmdb.query()
	results = query.convert()
	print
	for result in results["results"]["bindings"]:
		resource = result["o"]["value"]
		print "->RunTime: " + resource
		
		
def getWebenemasunoResource (label, lang, endpoint):

	sparqlWebenemasuno = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "SELECT ?s WHERE { ?s sioc:title \"" + label + "\"@" +lang + "}"
	else:
		queryString = "SELECT ?s WHERE { ?s sioc:title \"" + label + "\" }"
	sparqlWebenemasuno.setQuery(queryString)
	sparqlWebenemasuno.setReturnFormat(JSON)
	query   = sparqlWebenemasuno.query()
	results = query.convert()
	print
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "->The resource: " + resource
		
def getDBpediaBirthName (label, lang, endpoint):

	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . ?s dbp:birthName ?o} " 
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\" . ?s dbp:birthName ?o } " 
	
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["o"]["value"]
		print "birthName: " + resource	
	
def getDBpediaBirthPlace (label, lang, endpoint):

	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . ?s dbp:birthPlace ?o} " 
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\" . ?s dbp:birthPlace ?o } " 
	
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["o"]["value"]
		print "birthPlace: " + resource
		
def getDBpediaOccupation (label, lang, endpoint):

	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . ?s dbp:occupation ?o} " 
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\" . ?s dbp:occupation ?o } " 
	
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["o"]["value"]
		print "Occupation: " + resource

def getDBpediaMusicalArtist (label, lang, endpoint):

	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbo: <http://dbpedia.org/ontology/>  PREFIX dbr:<http://dbpedia.org/resource/> SELECT ?s WHERE {?s dbo:musicalArtist <http://dbpedia.org/resource/Alicia_Keys>} " 
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX dbr:<http://dbpedia.org/resource/> SELECT ?s WHERE {?s dbo:musicalArtist <http://dbpedia.org/resource/Alicia_Keys> } " 
	
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["s"]["value"]
		print "MusicalArtist: " + resource
		
		
def getDBpediaBirthDate (label, lang, endpoint):

	sparqlDBPedia = SPARQLWrapper(endpoint)
	if (lang):
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\"@" +lang + " . ?s dbp:birthDate ?o} " 
	else:
		queryString = "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX foaf: <http://xmlns.com/foaf/0.1/> PREFIX dbp: <http://dbpedia.org/property/> SELECT ?o WHERE { ?s rdfs:label \"" + label + "\" . ?s dbp:birthDate ?o } " 
	
	sparqlDBPedia.setQuery(queryString)
	sparqlDBPedia.setReturnFormat(JSON)
	query   = sparqlDBPedia.query()
	results = query.convert()
	for result in results["results"]["bindings"]:
		resource = result["o"]["value"]
		print "birthDate: " + resource		

#def getWebenemasunoContent (label, lang, endpoint):

#	sparqlWebenemasuno = SPARQLWrapper(endpoint)
#	if (lang):
#		queryString = "PREFIX opmo: <http://openprovenance.org/model/opmo#> SELECT ?s WHERE { ?s sioc:title \"" + label + "\"@" +lang + ". ?s opmo:content ?o}"
#	else:
#		queryString = "PREFIX opmo: <http://openprovenance.org/model/opmo#> SELECT ?s WHERE { ?s sioc:title \"" + label + "\" . ?s opmo:content ?o}"
#	sparqlWebenemasuno.setQuery(queryString)
#	sparqlWebenemasuno.setReturnFormat(JSON)
#	query   = sparqlWebenemasuno.query()
#	results = query.convert()
#	print
#	for result in results["results"]["bindings"]:
#		resource = result["s"]["value"]
# 		print "->Content: " + resource
		
if __name__ == '__main__':

	# getLocalLabel devuelve una lista con todas las instancias que haya con sus label y lang
	# y luego se hace la llamada al repositorio externo para enriquecer cada combinacion de label-lang recibida
	lista = getLocalLabel("instancia1");
	print lista
	endpoint = 'http://dbpedia.org/sparql';
	for result in lista:
		(label, lang) = result
		resource = getDBpediaResource (label, lang, endpoint);

		birthName = getDBpediaBirthName (label, lang, endpoint);		
		print birthName

		birthDate = getDBpediaBirthDate (label, lang, endpoint);		
		print birthDate

		birthPlace = getDBpediaBirthPlace (label, lang, endpoint);		
		print birthPlace
		
		occupation = getDBpediaOccupation (label, lang, endpoint);		
		print occupation

		musicalArtist = getDBpediaMusicalArtist (label, lang, endpoint);		
		print musicalArtist
		
	print "\n---------------------\n"


	# Descomentar las siguientes lineas y modificar en cada  
	lista = getLocalLabel("instancia3");
	print lista
	endpoint = 'http://data.linkedmdb.org/sparql';
	for result in lista:
		(label, lang) = result
		resource = getLinkedmdbResource (label, lang, endpoint);

		director = getLinkedmdbMovieDirector (label, lang, endpoint);		
		print director

		date = getLinkedmdbMovieDate (label, lang, endpoint);		
		print date

		date = getLinkedmdbMovieRunTime (label, lang, endpoint);		
		print date

		
	print "\n---------------------\n"

	lista = getLocalLabel("instancia4");
	print lista
	endpoint = 'http://webenemasuno.linkeddata.es/sparql';
	for result in lista:
		(label, lang) = result
		resource = getWebenemasunoResource (label, lang, endpoint);

#		vino = getWebenemasunoContent (label, lang, endpoint);		
#		print vino		

		
#if __name__ == '__main__':

	# getLocalLabel devuelve una lista con todas las instancias que haya con sus label y lang
	# y luego se hace la llamada al repositorio externo para enriquecer cada combinacion de label-lang recibida
	#lista = getDBpediaOccupation ('Alicia Keys', '', 'http://dbpedia.org/sparql');
	#print lista;
	
		