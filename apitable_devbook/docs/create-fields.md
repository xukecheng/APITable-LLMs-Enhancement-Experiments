---
title: Create Fields
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Create fields](/api/reference#operation/create-fields) interface.

## Example: create fields

Suppose you have a channel sales inventory summary table and you want to create a field in it.

![Log action - Example datasheet](media/fields-example.png)

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get your Space ID.([How to get it](/api/introduction#spaceid))

3. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

4. Open the terminal on your computer and execute the following code to send a query request to the server (Assuming spaceId is `spcjXzqVrjaP3`，datasheetId is `dstNiC6R9MryevVaCQ`) :

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
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/datasheets/dstNiC6R9MryevVaCQ/fields" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
     "type": "SingleText",
     "name": "Title",
     "property": {
     "defaultValue": "Default value"
     }
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
   
   try {
     const res = await apitable.space('spcjXzqVrjaP3').datasheet('dstNiC6R9MryevVaCQ').fields.create(fieldRo);
     if (res.success) {
       // TODO: save field.id
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
        'defaultValue': 'Default value',
    }

    req_data = {
        'name': 'New text field',
        'type': 'SingleText',
        'property': prop,
    }

    try:
        field = apitable.space('spcjXzqVrjaP3').datasheet('dstNiC6R9MryevVaCQ').fields.create(req_data)
    except Exception:
        # Handling abnormal situations
        pass

    ```

    </TabItem> 

   </Tabs>
   ````
5. The server returns the following JSON packets, below the `"data"` is all created fields:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/create-fields) 
> 
> ```json
>    {
>      "success": true,
>      "code": 200,
>      "message": "SUCCESS",
>      "data": {
>        "id": "fldupsvkR2ATB",
>        "name": "Title"
>      }
>    }
> ```