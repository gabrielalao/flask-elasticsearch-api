from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import certifi

ES_HOSTS = ['https://4a0fe9b139a0f63e8dd3955617adf9e5.us-west-2.aws.found.io:9243']
ES_AUTH = ('elastic', 'KhHW75LOYREnaGhNLIsZQinZ')

ES_INDEX = 'master'

es = Elasticsearch(hosts=ES_HOSTS, http_auth=ES_AUTH, use_ssl=True)

# Full text search functions
def get_all_docs(term):
    term = '*%s*' % term
    q = {'query': {'query_string': {'fields':['_all'],'query': term}}}
    
    results = {}
    for doc in scan(es, q, index=ES_INDEX, doc_type='tax'):
        PID = doc['_id']
        source = doc['_source']
        results[PID] = source

    return results

def get_pagination_docs(_type, _query, _fields, _size, _from):
    term = '*%s*' % _query
    fields = _fields.split(',');
    if 'all' in fields:
        q = {'query': {'query_string': {'fields':['_all'],'query': term}}}
    else:
        q = {'query': {'query_string': {'fields': fields, 'query': term}}}

    r = es.search(index=ES_INDEX, doc_type=_type, body=q, size=_size, from_=_from)

    results = {}
    if r['hits']['total']:
        for doc in r['hits']['hits']:
            PID = doc['_id']
            source = doc['_source']
            results[PID] = source

    return (r['hits']['total'], results)

def multi_search(situs_address='*', tax_bill_mailing_address='*', primary_owner_full_name='*'):
    boolQ = {
        'must': [
            {
                'query_string': {
                    'default_field': 'SitusAddress',
                    'query': situs_address
                }
            },
            {
                'query_string': {
                    'default_field': 'PrimaryOwnerFullName',
                    'query': primary_owner_full_name
                }
            },
            {
                'query_string': {
                    'default_field': 'TaxBillMailingAddress',
                    'query': tax_bill_mailing_address
                }
            }
        ]
    }
    q = {'query': {'bool': boolQ}}
    results = {}
    
    for doc in scan(es, q, index=ES_INDEX, doc_type='tax'):
        PID = doc['_id']
        source = doc['_source']
        results[PID] = source

    return results


def test_multi_search():
  results = multi_search(situs_address='*franklin*', tax_bill_mailing_address='*ma*')
  assert len(results) == 13