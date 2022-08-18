from sec_api import QueryApi

queryApi = QueryApi(api_key="f17bf8cab4647b3fb6ef143ce5211796526dac47dfa412a29a2cf00f0fac7d62")

query = {
  "query": { "query_string": { 
      "query": "ticker:TSLA AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-Q\"" 
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

print(filings)


