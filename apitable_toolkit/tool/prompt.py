APITABLE_GET_SPACES_PROMPT = """
This tool helps you search for spaces using APITable's space API.

useful when you need to fetch all the spaces the user has access to, find out how many spaces there are, or as an intermediary step that involv searching by spaces. 
there is no input to this tool.

For example, to find all the spaces you have, you would do that:
self.apitable.spaces.all()
"""

APITABLE_GET_NODES_PROMPT = """
This tool helps you search for datasheets, mirrors, dashboards, folders and forms in a space using APITable's node API.
The input to this tool is a space id string, and will be passed into Apitable's `space` function,
The first three characters of the space ID must be fixed as `spc` and must meet this condition, 

Here are some examples, it should be noted that the following IDs are all fake and cannot be used for real requests, 

For example, to find all the nodes in space id `spcjXzqVrjaP3`, python code would be:
self.apitable.space('spcjXzqVrjaP3').nodes.all()
So I need you to pass data like json below, it should be noted that the following json are fake and cannot be used for real requests:
{{"space_id": "spcjXzqVrjaP3"}}

Do not make up space_id, if you do not know the space_id, you can use the `get_spaces` tool to get all space_ids
"""

APITABLE_GET_FIELD_PROMPT = """
This tool helps you search for fields in a datasheet using APITable's field API.
To use this tool, input a datasheet ID string that starts with `dst` and is followed by unique characters.
If the user query includes terms like "latest", "oldest", or a specific field name, please use the get_fields tool to obtain all available fields before using the get_records tool to retrieve records.
Here are some examples (note that the following JSON is for illustration purposes only and cannot be used for real requests):
If you want to find all fields in datasheet ID `dstS94qPZFXjC1LKns`, use the following Python code:
self.apitable.datasheet("dstlRNFl8L2mufwT5t").fields.all()
Pass the datasheet ID as a JSON object like this:
{{"datasheet_id": "dstlRNFl8L2mufwT5t"}}
Do not make up datasheet_id, if you do not know the datasheet ID, use the `get_nodes` tool to get all datasheet IDs.
"""


APITABLE_GET_RECORDS_PROMPT = """
This tool is a wrapper around APITable's record API, useful when you need to search for records.
The input to this tool is a datasheet id string, and will be passed into Apitable's `datasheet` function,
The first three characters of the datasheet ID must be fixed as `dst` and must meet this condition, 

Here are some examples, it should be noted that the following json are all fake and cannot be used for real requests, 

For example, to find all the records in datasheet id `dstS94qPZFXjC1LKns`, python code would be:
dst = self.apitable.datasheet('dstS94qPZFXjC1LKns')
records = dst.records.all()
So I need you to pass data like json below, it should be noted that the following json are fake and cannot be used for real requests:
{{"datasheet_id": "dstS94qPZFXjC1LKns"}}

or to find records with key named "title" that match the word "test" in datasheet id `dstS94qPZFXjC1LKns`, python code would be:
dst = self.apitable.datasheet('dstS94qPZFXjC1LKns')
records = dst.records.filter(title='test').get()
So I need you to pass data like json below, it should be noted that the following json are all fake and cannot be used for real requests:
{{"datasheet_id": "dstS94qPZFXjC1LKns", "filter_condition": {{"title": "test"}}}}

or find and sort records by a specified field, say reverse order by a field named `test` in datasheet id `dstS94qPZFXjC1LKns`, python code would be:
dst = self.apitable.datasheet('dstS94qPZFXjC1LKns')
records = dst.records.all(sort=[{{ field: 'test', order: 'desc' }}])
So I need you to pass data like json below, it should be noted that the following json are all fake and cannot be used for real requests:
{{"datasheet_id": "dstS94qPZFXjC1LKns", "sort_condition": [{{ "field": "test", "order": "desc" }}]}}

or find records and set the number of records returned is 10 in datasheet id `dstS94qPZFXjC1LKns`, python code would be:
dst = self.apitable.datasheet('dstS94qPZFXjC1LKns')
dst.records.all(maxRecords=10)
So I need you to pass data like json below, it should be noted that the following json are fake and cannot be used for real requests:
{{"datasheet_id": "dstS94qPZFXjC1LKns", "maxRecords_condition": 10}}

Do not make up datasheet_id, if you do not know the datasheet_id, you can use the `get_nodes` tool to get all datasheet_ids
Do not make up field key, if you don't know the field key, use the 'get_fields' tool to retrieve all fields in a datasheet and find the closest field name to use as the field key
"""

APITABLE_CATCH_ALL_PROMPT = """
This tool is a wrapper around APITable's API.
There are other dedicated tools for fetching all spaces, and searching for nodes and searching for records, 
use this tool if you need to perform any other actions allowed by the APITable API.
The input to this tool is line of python code that calls a function from APITable API

Here are some examples, it should be noted that the following IDs are all fake and cannot be used for real requests, 

For example,to find all the records in datasheet id dstS94qPZFXjC1LKns and update the key named title to test2, python code would be:
records = self.apitable.datasheet('dstS94qPZFXjC1LKns')
records.update('title': 'test2')
So I need you to pass data like json below, it should be noted that the following IDs are all fake and cannot be used for real requests:
{{"datasheet_id": "dstS94qPZFXjC1LKns", "update_condition": {{"title": "test2"}}}}

For more information on the python package for the Fusion API of APITable, refer to https://github.com/apitable/apitable-sdks/tree/develop/apitable.py
"""
