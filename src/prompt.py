# PROMPT = """
# Generate a valid SQL query for the following natural language instruction:

# Query: ${query}

# ${gr.complete_json_suffix_v3}
# """

PROMPT = """
Generate a valid SQL query for the following natural language instruction:

Here is the query: ${query}

${gr.complete_json_suffix_v3}
"""