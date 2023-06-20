At the present time, APITable is open to the interfaces of getting records, creating records, updating records and deleting records.

The data structure of the records is as follows.

| Properties | Description                                                                                                     |
| :--------- | :-------------------------------------------------------------------------------------------------------------- |
| recordId   | string <br/>record ID <br/> e.g. `"rec1jV9eWxcaB"`                                                              |
| createdAt  | number <br/>The creation time of the record, in timestamp format <br/> e.g.  `1624960629000`                    |
| updatedAt  | number <br/>The modification time of this record, in timestamp format <br/> e.g.  `1624964696000`               |
| fields     | object <br/>the data of the corresponding field in a record, returned in the format `{"fieldName": fieldValue}` |


When using the [Create Records](create-records) or [Update Records](update-records) API to write to fields, you need to understand the data type and structure of each field value. 

Note: calculated fields do not allow values to be written actively, including: AutoNumber, Formula, MagicLookUp, LastModifiedTime, CreatedTime, LastModifiedBy, CreatedBy, etc.

For reference,the following table lists the values of different types of fields:

| Field Types  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SingleText   | string <br/>returns a string without "\n" line breaks<br/>e.g. `{"fieldName": "an example title"}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Text         | string <br/>returns a string with "\n" line breaks<br/>e.g. `{"fieldName": "a long text"}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SingleSelect | string <br/>returns the selected option as a string<br/>e.g. `{"fieldName": "done"}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MultiSelect  | array of strings <br/>returns the selected options as an array of strings<br/>e.g. `"{"fieldName": ["Option1", "Option2"]}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Number       | number <br/>returns a positive or negative number. The return result will not include the precision or symbol given in the field settings.<br/>e.g. `"{"fieldName": 1998}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Currency     | number <br/>returns a positive or negative number. The return result will not include the precision or symbol given in the field settings.<br/>e.g. `"{"fieldName": 999}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Percent      | number <br/>returns a positive or negative number. The return result will not include the precision or symbol given in the field settings.<br/>e.g. `"{"fieldName": 0.1}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DateTime     | number <br/>returns a timestamp in milliseconds<br/>e.g. `"{"fieldName": 1678723200000}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attachment   | array of attachment objects <br/>returns an array of attachment objects. Each object includes the following properties: <br/>1. mimeType (string): the media type of the attachment; <br/>2. name (string): the name of the attachment; <br/>3. size (number): the size of the attachment (byte); <br/>4. width (number): the width of the image (px), if the attachment is an image; <br/>5. height (number): the height of the image (px), if the attachment is an image; <br/>6. token (string): the access path of the attachment; <br/>7. preview (string): the preview image URL that you can open in a browser, if the attachment is a PDF<br/>e.g. `{"fieldName":[{"id":"atcFagvJrELTS","name":"logo.png","size":6396,"mimeType":"image/png","token":"space/2023/03/17/ee1bb79d3fd847e383e21c9b0bd53dfc","width":424,"height":80,"url":"https://legacy-s1.apitable.com/space/2023/03/17/ee1bb79d3fd847e383e21c9b0bd53dfc"}]}` |
| Member       | array of unit objects <br/>returns an array of unit objects. A unit describes the roles in a Space such as a member or a team.<br/>- id: string, the ID of the organizational unit<br/>- type: number, the type of organizational unit, 1 is the group, 3 is the member<br/>- name: string, the name of the group or member<br/>- avatar: string, avatar URL, read-only, not writable<br/>e.g. `{"fieldName":[{"id":"1291258301781176321","type":3,"name":"Jane","avatar":"https://s1.apitable.com/space/2023/02/09/79e112dd10424ac7842256736e4f5568"}]}`                                                                                                                                                                                                                                                                                                                                                                             |
| Checkbox     | boolean <br/>returns true as boolean format if the checkbox is checked. Otherwise the return result will not include this Checkbox field.<br/>e.g. `{"fieldName": true}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Rating       | number <br/>returns a positive number between 1 and 10. The return result will not include this field if the value is empty.<br/>e.g. `{"fieldName": 5}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| URL          | url object <br/>returns a URL object, including title (webpage title), text (webpage address), favicon (webpage icon)<br/>e.g. `{"fieldName":{"title":"APITable","text":"https://apitable.com","favicon":"https://legacy-s1.apitable.com/space/2022/12/08/f8693e8f39774a1c8f0b937f39da0e17"}}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Phone        | string <br/> returns a phone number as a string<br/>e.g. `{"fieldName": "(310) 3xx-5xxx"}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Email        | string <br/>returns a email address as a string<br/>e.g. `{"fieldName": "support@apitable.com"}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MagicLink    | array of record IDs (strings) <br/>returns an array of strings. Each string is the ID of a record that is added into the Magic Link field.<br/>e.g. `{"fieldName": ['recz9eeg61SEa']}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MagicLookUp  | array of any <br/>returns a number, string, or array. The Lookup result is calculated by the system. You can't write into the Lookup field by API. <br/>e.g. `{"fieldName": ['Reference data 1', 'Reference data 2']}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Formula      | string \| number \| boolean <br/>returns a number, string, or boolean result. The formula result is calculated by the system. You can't write into the Formula field by API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AutoNumber   | number <br/>returns a positive number. The system automatically generates the numbers so you can't write into the field by API.<br/>e.g. `{"fieldName": 1}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |