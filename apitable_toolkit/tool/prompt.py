PREFIX = """
Answer the following questions as best you can, 
You have access to the following tools.  
But every tool has a cost, so be smart and efficient. 
Aim to complete tasks in the least number of steps:
"""

FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""

SUFFIX = """If latest Observation can solute original input question, 
then output final answer, 
don't move on to the next question:

Begin!
Question: {input}
Thought:{agent_scratchpad}"""


APITABLE_GET_SPACES_PROMPT = """
This tool helps you search for spaces using APITable's space API.
It's useful when you need to fetch all the spaces the user has access to, 
find out how many spaces there are, or as an intermediary step that involv searching by spaces. 
there is no input to this tool.
"""

APITABLE_GET_NODES_PROMPT = """
This tool helps you search for datasheets, mirrors, dashboards, folders and forms using APITable's node API,
datasheet, mirror, dashboard, folder and form are all called node in APITable.
The input to this tool is a space id that starts with `spc` and is followed by unique characters.
So I need you to pass data like json below, the following json are fake and cannot be used for real requests:
{{"space_id": "spcjXzqVrjaP3"}}
Do not make up space_id, if you do not know the space_id, you can use the `get_spaces` tool to get all space_ids
"""

APITABLE_GET_FIELD_PROMPT = """
This tool helps you search for fields in a datasheet using APITable's field API.
To use this tool, input a datasheet id that starts with `dst` and is followed by unique characters.
If the user query includes terms like "latest", "oldest", or a specific field name, 
please use the `get_fields` tool first to get the field name as field key
Pass the datasheet ID as a JSON object like this, the following json are fake and cannot be used for real requests:
{{"datasheet_id": "dstlRNFl8L2mufwT5t"}}
Do not make up datasheet_id, if you do not know the datasheet ID, use the `get_nodes` tool to get all datasheet IDs.
"""

APITABLE_CREATE_FIELD_PROMPT = """
This tool helps you create fields in a datasheet using APITable's field API.
To use this tool, input a space id and a datasheet id, if you don't have these two ids, 
you can use the `get_spaces` and `get_nodes` tools to get them.
Different field types have different properties, the following are all field types and their properties:
1.SingleText:
defaultValue | string | Default is empty
2.Text: No field properties are available.
3.SingleSelect:
options | object arrays	| List of all available options, Default is empty
Each object in the `options` key has the following schema:
name | string | option name
4.MultiSelect: The field properties are the same as the SingleSelect.
5.Number:
defaultValue | string | Default is empty.
precision | number(enum) | the precision of the number. 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)
6.Currency:
defaultValue | string | Default is empty.
precision | number(enum) | the precision of the number. 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)
symbol | string | Currency symbol
7.Percent: The field properties are the same as the number.
8.DateTime:
dateFormat | string(enum) | `YYYY-MM-DD` `YYYY-MM` `MM-DD` `YYYY` `MM` `DD` 
includeTime | boolean | Include time or not, default is False
timeFormat | string(enum) | `HH:mm` `hh:mm`
9.Attachment: Don't need properties
10.Member:
isMulti | boolean | Is it possible to select multiple members, default is True
shouldSendMsg | boolean | Whether to send a message to members in time, default is False
11.Checkbox:
icon | string(enum) | Default is white_check_mark
12.Rating:
icon | string(enum) | Default is star
max | number | The maximum value of the rating, from 1-10, default is 5
13.URL: Don't need properties
14.Phone: Don't need properties
15.Email: Don't need properties
16.MagicLink:
foreignDatasheetId | string | Related datasheet id
limitSingleRecord | boolean | Link to multiple records, default is False
17.AutoNumber: Don't need properties
18.CreatedTime: Same as DateTime.
19.LastModifiedTime: Same as DateTime.
20.CreatedBy: Don't need properties
21.LastModifiedBy: Don't need properties
22.Formula:
expression | string | formula expression, default is empty
valueType | string(enum) | Including `String` `Boolean` `Number` `DateTime` `Array`
hasError | boolean | Default is False
Do not make up field type, the num of field type is 22
Do not make up properties, if you do not know the properties, then don't send field_data
--------------------------
Pass the datasheet ID as a JSON object like this, the following JSON is for illustration purposes only and cannot be used for real requests:
{{"space_id": "spcjXzqVrjaP3", "datasheet_id": "dstlRNFl8L2mufwT5t", "field_data": {{"defaultValue": "Default value"}}}}
"""


APITABLE_GET_RECORDS_PROMPT = """
This tool is a wrapper around APITable's record API, useful when you need to search for records.
The input to this tool is a datasheet id string, and will be passed into Apitable's `datasheet` function,
The first three characters of the datasheet ID must be fixed as `dst` and must meet this condition, 
Here are some examples, it should be noted that the following json are all fake and cannot be used for real requests, 
For example, to find all the records in datasheet id `dstS94qPZFXjC1LKns`, json would be:
{{"datasheet_id": "dstS94qPZFXjC1LKns"}}
or to find records with key named "title" that match the word "test" in datasheet id `dstS94qPZFXjC1LKns`, json would be:
dst = self.apitable.datasheet('dstS94qPZFXjC1LKns')
{{"datasheet_id": "dstS94qPZFXjC1LKns", "filter_condition": {{"title": "test"}}}}
or to find and sort records by a specified field, say reverse order by a field named `test` in datasheet id `dstS94qPZFXjC1LKns`, json would be:
{{"datasheet_id": "dstS94qPZFXjC1LKns", "sort_condition": [{{ "field": "test", "order": "desc" }}]}}
or find records and set the number of records returned is 10 in datasheet id `dstS94qPZFXjC1LKns`, json would be:
{{"datasheet_id": "dstS94qPZFXjC1LKns", "maxRecords_condition": 10}}
Do not make up datasheet_id, if you do not know the datasheet_id, you can use the `get_nodes` tool to get all datasheet_ids
Do not make up field key, if you don't know the field key, use the 'get_fields' tool to retrieve all fields in a datasheet 
and find the closest field name to use as the field key
"""
