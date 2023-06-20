---
title: Delete Fields
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Delete fields](/api/reference#operation/delete-fields) interface.

## Example: delete fields

Assuming you have a datasheet, you would like to delete one of these fields.

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get your Space ID.([How to get it](introduction#spaceid))

3. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

4. Get the ID of the field that needs to be deleted.([How to get it](introduction.md#fieldid))

5. Open the terminal on your computer and execute the following code to send a query request to the server (Assuming spaceId is `spcjXzqVrjaP3`，datasheetId is `dstNiC6R9MryevVaCQ`, fieldId is `fld4SRHNAugJq`) :
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
   curl -X DELETE \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/datasheets/dstNiC6R9MryevVaCQ/fields/fld4SRHNAugJq" \
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
   
   try {
     const resp = await apitable.space('spcjXzqVrjaP3').datasheet('dstNiC6R9MryevVaCQ').fields.delete('fld4SRHNAugJq');
     if (resp.success) {
       // TODO: 
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

    try:
        apitable.space('spcjXzqVrjaP3').datasheet('dstNiC6R9MryevVaCQ').fields.delete('fld4SRHNAugJq')
    except Exception:
        # Handling abnormal situations
        pass

    ```

    </TabItem> 

   </Tabs>
   ````
6. Upon success, the server will return the following JSON data.
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/delete-fields) 
> 
> ```json
>    {
>      "success": true,
>      "code": 200,
>      "message": "SUCCESS",
>      "data": {}
>    }
> ```