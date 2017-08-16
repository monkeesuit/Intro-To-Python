d = {
        "glossary": {
                        "title": "example glossary",
		                "GlossDiv": {
                                        "title": "S",
			                            "GlossList": {
                                                        "GlossEntry": {
                                                                        "ID": "SGML",
                                                    					"SortAs": "SGML",
                                                    					"GlossTerm": "Standard Generalized Markup Language",
                                                    					"Acronym": "SGML",
                                                    					"Abbrev": "ISO 8879:1986",
                                                    					"GlossDef": {
                                                                                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                                            						    "GlossSeeAlso": ["GML", "XML"]
                                                                                    },
					                                                    "GlossSee": "markup"
                                                                        }
                                                    }
                                    }
                    }
     }

# DON'T NAME THIS FILE JSON.PY

import json

print(d['glossary']['title'])

# Normal file write - write has to be a string
with open('nojson', 'w') as f:
    f.write(str(d))

# Normal file read
with open('nojson', 'r') as f:
    string_dictionary = f.read()

# Reading a file returns a string not a dictionary
# We can index this string like any other string
print(string_dictionary[0])
# We cannont index this string like a dictionary
try:
    print(string_dictionary['glossary'])
except TypeError:
    print("You Can't Do This")

# JSON Dumping A Python Object To A File
with open('json', 'w') as f:
    json.dump(d, f)

# JSON Loading A JSON Object
with open('json', 'r') as f:
    json_dictionary = json.load(f)

# Now The Object Is A Dictionary And Can Be Indexed Like One
print(json_dictionary['glossary']['title'])
