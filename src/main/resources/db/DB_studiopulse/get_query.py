def load_queries(filepath):
    queries = {}
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):  # Skip empty lines and comments
                key, value = line.strip().split('=', 1)    # Split at '='
                queries[key] = value
    return queries

 #queries = load_queries('create-query.properties')   # Load all queries

# create_query = queries['client_create_query']     # Get specific query

#print(create_query)







