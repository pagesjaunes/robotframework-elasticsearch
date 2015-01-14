# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

class ElasticSearchLib(object):
    """
    RobotFramework lib for querying an elasticsearch server.
    It allows to run a query, count docs and manage indices (create, delete)

    requires elasticsearch-py : http://elasticsearch-py.readthedocs.org/en/latest/index.html

    = Table of contents =

    - `Usage`
    - `Keywords`

    = Usage =

    This library has several keywords : es search, es count, es delete index, es create index.
    """

    ROBOT_LIBRARY_VERSION = '1.1'

    def es_search(self,p_host,p_port,p_index,p_query):
        """
        Returns a query result from elastic search
        The result is the response from elasticsearch as a dictionnary.

        {p_host}   Elasticsearch server\n
        {p_port}   Port of the es server\n
        {p_index}  Name of the index to query\n
        {p_query}  Query to run\n

        | ${res} = | es search | localhost | 9200 | myIndex |  {"query":{"query_string":{"query": "searched value"}}} |
        """
        
        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connexion error on %s:%i",p_host,int(p_port))

        try:
            documents = es.search(body=p_query, index=p_index)
        except Exception:
            raise AssertionError("Search error on %s:%i/%s for query : %s",p_host,int(p_port),p_index,p_query)

        return documents

    def es_count(self,p_host,p_port,p_index,p_query=None):
        """
        Returns the number of documents that match a query
        The result is the response from elastic search. The value is in the "count" field of the response.

        {p_host}   Elasticsearch server\n
        {p_port}   Port of the es server\n
        {p_index}  Name of the index to query\n
        {p_query}  Query to run\n

        | ${res} = | es count | localhost | 9200 | myIndex |  {"query":{"query_string":{"query": "searched value"}}} |

        ${res} contains the number of docs
        """

        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connexion error on %s:%i",p_host,int(p_port))

        try:
            result = es.count(index=p_index, body=p_query)
        except Exception:
            raise AssertionError("Count error on %s:%i/%s for query : %s",p_host,int(p_port),p_index,p_query)

        return result['count']

    def es_delete_index(self,p_host,p_port,p_index):
        """
        Deletes an index

        {p_host}   Elasticsearch server\n
        {p_port}   Port of the es server\n
        {p_index}  Name of the index to remove\n

        | ${res} = | es delete index | localhost | 9200 | myIndex |
        """

        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connexion error on %s:%i",p_host,int(p_port))

        try:
            es.indices.delete(index=p_index)
        except Exception:
            raise AssertionError("Can't delete the index %s on %s:%i",p_index,p_host,int(p_port))

    def es_create_index(self,p_host,p_port,p_index,p_mapping=None):
        """
        Creates an index

        {p_host}        Elasticsearch server\n
        {p_port}        Port of the es server\n
        {p_index}       Name of the index to create\n
        {p_mapping}     (optional) Dictionnary containing a custom mapping\n

        | ${res} = | es create index | localhost | 9200 | myIndex |
        | ${res} = | es create index | localhost | 9200 | myIndex | CustomDicMapping |
        """

        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connexion error on %s:%i",p_host,int(p_port))

        try:
            es.indices.create(index=p_index,body=p_mapping)

        except Exception:
            raise AssertionError("Can't create the index %s on %s:%i",p_index,p_host,int(p_port))

    def es_index(self,p_host,p_port,p_index,p_doctype,p_docid,p_document):
        """
        Indexes a document on an elasticsearch index according to a doctype and a docid

        {p_host}   Elasticsearch server\n
        {p_port}   Port of the es server\n
        {p_index}  Name of the index to query\n
        {p_doctype}  type of the document to index\n
        {p_docid}     Id of the document to index\n
        {p_document}  Document to index\n

        | es index | localhost | 9200 | myIndex | theDocType | id_457891 | {"adress":{"street":"myAdress", "city":"Wow city"}} |
        """
        
        # Es client
        try:
            param = [{'host':p_host,'port':int(p_port)}]
            es = Elasticsearch(param)
        except Exception:
            raise AssertionError("Connexion error on %s:%i",p_host,int(p_port))

        try:
            es.index(doc_type=p_doctype, id=p_docid, body=p_document, index=p_index)
        except Exception:
            raise AssertionError("Index error on %s:%i/%s for document : %s",p_host,int(p_port),p_index,p_document)
