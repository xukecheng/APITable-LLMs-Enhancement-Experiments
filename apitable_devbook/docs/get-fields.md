---
title: Get Fields
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Get fields](/api/reference#operation/get-fields) interface.

## Example: Get all fields of a specified APITable

Suppose you have a channel sales inventory summary datasheet and you want to get information about all the fields of this datasheet.

![Get Fields Demo](media/fields-example.jpg)

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

3. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstCufZ779fE41TzZy`):
    ````mdx-code-block
    <Tabs
    groupId="get fields"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL', },
        { label: "Javascript SDK", value: 'Javascript SDK', },
        { label: "Python SDK", value: 'Python SDK', },
        ]
    }
    >

    <TabItem value="cURL">

    ```bash
    curl -X GET \
    "https://api.apitable.com/fusion/v1/datasheets/dstCufZ779fE41TzZy/fields" \
    -H "Authorization: Bearer {Your API Token}"
    ```

    </TabItem>

    <TabItem value="Javascript SDK">

    > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```js
    import { APITable } from 'apitable';

    const apitable = new APITable({
      token: 'Your API Token',
    });

    const datasheet = apitable.datasheet("dstCufZ779fE41TzZy");
    const fieldsResp = await datasheet.fields.list()

    if (fieldsResp.success) {
      console.log(fieldsResp.data.fields);
    } else {
      console.error(fieldsResp);
    }
    ```

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dstCufZ779fE41TzZy")

    # Get all fields
    fields = dst.fields.all()
    for field in fields:
      print(field.json())
    ```

    </TabItem>

    </Tabs>
    ````
4. The server returns the following JSON data, below the `"fields"` is all data in this view:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-fields) 
> 
> ```json
>     {
>   "code": 200,
>   "success": true,
>   "data": {
>       "fields": [
>           {
>               "id": "fldGMxxBjVzGi",
>               "name": "Product UPC",
>               "type": "SingleText",
>               "property": {
>                   "defaultValue": ""
>               },
>               "editable": true,
>               "isPrimary": true
>           },
>           {
>               "id": "fldlSvMaP5TQG",
>               "name": "SKU name",
>               "type": "SingleText",
>               "property": {},
>               "editable": true
>           },
>           {
>               "id": "fldlXCBJyXTPo",
>               "name": "Brands",
>               "type": "SingleSelect",
>               "property": {
>                   "options": [
>                       {
>                           "id": "optCe7DGNgtkS",
>                           "name": "OAD",
>                           "color": {
>                               "name": "deepPurple_0",
>                               "value": "#E5E1FC"
>                           }
>                       },
>                       {
>                           "id": "optdgOCPhHToc",
>                           "name": "Elevit",
>                           "color": {
>                               "name": "indigo_0",
>                               "value": "#DDE7FF"
>                           }
>                       }
>                   ]
>               },
>               "editable": true
>           }
>       ]
>   },
>   "message": "SUCCESS"
> }
> ```
