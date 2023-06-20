---
title: Create Datasheet
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

We will show you how to [Create a datasheet](/api/reference#operation/create-datasheets).

## Example: create datasheet

Suppose you have a space and you want to create a datasheet in the space.

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get your Space ID.([How to get it](/api/introduction#spaceid))

3. Get the ID (not required) of the folder to which it belongs.([How to get it](/api/introduction#nodeid))

4. Open the terminal on your computer, execute the following code and send the query request to the server (e.g. `spaceId` is `spcjXzqVrjaP3`):

    ````mdx-code-block
    <Tabs
    groupId="create records"
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
   curl -X POST \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/datasheets" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
     "name": "Title",
     "description": "Description",
     "folderId": "Not required, belong to the folder ID",
     "preNodeId": "Not required, previous node ID",
     "fields": [
       {
         "type": "Text",
         "name": "Title"
       }
     ]
   }'
   ```

    </TabItem>

   <TabItem value="Javascript SDK">

   > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

   ```js
   import { APITable } from 'apitable';
   
   const apitable = new APITable({
     token: 'Your API Token',
   });
   
   // Referring to IAddOpenFieldProperty, different FieldType corresponds to different Property structures
   const property = {
     defaultValue: 'Default value',
   };
   
   const fieldRo = {
     name: 'New text field',
     type: 'SingleText',
     property,
   };
   
   const datasheetRo = {
     name: 'New unit test datasheet',
     fields: [fieldRo],
   };
   
   try {
     const res = await apitable.space('spcjXzqVrjaP3').datasheets.create(datasheetRo);
     if (res.success) {
       for (const field of res.data.fields) {
         // TODO: save field.id
       }
     }
   } catch (error) {
     // TODO: handle error
   }
   ```

   </TabItem>

   <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")

    prop = {
        'defaultValue': 'Default value'
    }
    field = {
        'name': 'New text field',
        'type': 'SingleText',
        'property': prop
    }
    req_data = {
        'name': 'New unit test datasheet',
        'fields': [field]
    }
    try:
        datasheet = apitable.space('spcjXzqVrjaP3').datasheets.create(req_data)
    except Exception:
        # Handling abnormal situations
        pass

    ```

    </TabItem> 

    </Tabs>
  ````
5. The server returns the following JSON packets, below the `"views"` is all created datasheet:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/create-datasheets) 
> 
> ```json
>    {
>      "success": true,
>      "code": 200,
>      "message": "SUCCESS",
>      "data": {
>        "id": "dstbs2U7mt8AEqgKuh",
>        "createdAt": 1648648690000,
>        "fields": [
>          {
>            "id": "fldupsvkR2ATB",
>            "name": "title"
>          }
>        ]
>      }
>    }
> ```