---
title: Delete Embedded Links
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

:::tip

The **[Embedded Links](https://help.apitable.com/docs/guide/embedding-with-embedded-link)** are only available for the spaces on the **[paid Pro or higher plan](https://apitable.com/pricing/)** in APITable Cloud as well as **[Enterprise](https://apitable.com/pricing/)** self-hosted edition.

:::

## Example

Here is an example of calling [API](/api/reference#operation/create-embedlinks) to delete an embedded link of a datasheet.

To delete an embedded link of a datasheet in the space, follow the steps below:

1. Obtain your API token. ([how to](quick-start#get-api-token))

2. Obtain the spaceId. ([how to](/api/introduction#spaceid))

3. Obtain the datasheetId. ([how to](introduction.md#datasheetid))

4. Obtain the ID of embedded link. ([how to](/api/reference#operation/get-embedlinks))

5. Open your system terminal, copy and paste following code on it and make a request to APITable server (the example space ID here is `spcjXzqVrjaP3`, datasheetId is `dstWUHwzTHd2YQaXEE`, and linkId is `embb90a52cfc02a4f83`)

    ````mdx-code-block
    <Tabs
    groupId="delete embedded links"
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
   "https://api.apitable.cn/fusion/v1/spaces/spcjXzqVrjaP3/nodes/dstWUHwzTHd2YQaXEE/embedlinks/embb90a52cfc02a4f83" \
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
     const res = await apitable.space('spcjXzqVrjaP3').datasheet('dstWUHwzTHd2YQaXEE').deleteEmbedLink('embb90a52cfc02a4f83');
     if (res.success) {
       // TODO
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
        isDeleted = apitable.space('spcjXzqVrjaP3').datasheet('dstWUHwzTHd2YQaXEE').delete_embed_link('embb90a52cfc02a4f83')
        print(isDeleted)
    except Exception:
        # handle error
        pass

    ```

    </TabItem> 

   </Tabs>
    ````

6. The response result:

    ```json
    {
        "code": 200,
        "success": true,
        "message": "SUCCESS"
    }
    ```

    :::tip

    For the meaning of each parameter in the response result above, please check the [API Reference](/api/reference#operation/delete-embedlinks)。

    :::
