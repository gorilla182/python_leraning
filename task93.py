def build_query_string(params):
    s = []
    for key, value in params.items():
        s.append(key + '='  + str(value))
    a = "&".join(s)
    return a

print(build_query_string({'name': 'timur', 'age': 28}))
