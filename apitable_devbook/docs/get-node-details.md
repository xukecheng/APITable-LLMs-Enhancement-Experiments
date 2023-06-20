---
title: Get Node Details
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Get Node Details](/api/reference#operation/get-node-details) interface.

## Example: Get the list and details of nodes in a specified folder

Suppose there is a folder under your space, and you want to get detailed information about this folder, including the information of its sub-files.

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get your Space ID.([How to get it](introduction.md#spaceid))

3. Get the ID of this folder.([How to get it](introduction.md#nodeid))

4. Open a terminal on your computer and execute the following code to send a query request to the server (assuming the Space ID is `spcX9P2xUcKst` and the folder ID is `fod23ha5NvyM5`).

    ````mdx-code-block
    <Tabs
    groupId="get node details"
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
    "https://api.apitable.com/fusion/v1/spaces/spcX9P2xUcKst/nodes/fod23ha5NvyM5" \
    -H  "Authorization: Bearer Your API Token}"
    ```

    </TabItem>

    <TabItem value="Javascript SDK">

    > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```js
    import { APITable } from 'apitable';

    const apitable = new APITable({
      token: 'Your API Token',
    });
    // Get details of a specified folder on a specified space
    const folderDetailResp = await apitable.nodes.get({spaceId: 'spcX9P2xUcKst', nodeId: 'fod23ha5NvyM5'})
    if (folderDetailResp.success){
      // Get the information of the child nodes under the folder
      console.log(folderDetailResp.data.children)
    }

    // Or get the details of the specified datasheet for the specified space (same for dashboard, forms)
    const datasheetDetailResp = await apitable.nodes.get({spaceId: 'spcX9P2xUcKst', nodeId: 'dstZsEg3RpBvsdCgop'})
    if (datasheetDetailResp.success){
      console.log(datasheetDetailResp.data)
    }
    ```

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst_info = apitable.nodes.get('dstZsEg3RpBvsdCgop')
    # Print the datasheet name
    print(dst_info.name)
    folder_info = apitable.nodes.get('fod23ha5NvyM5')
    # Folder node exists for children to get information about child files
    print(dst_info.children)
    ```

    </TabItem>

    </Tabs>
    ````
5. The server returns the following JSON data, with the details of the returned file under `"data"`.
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-node-details) 
> 
> ```json
>     {
>     "code": 200,
>     "success": true,
>     "data": {
>         "id": "fod23ha5NvyM5",
>         "name": "New Folder",
>         "type": "Folder",
>         "icon": "",
>         "isFav": false,
>         "children": [
>             {
>                 "id": "fodrPKCnaGAMy",
>                 "name": "New subfolder",
>                 "type": "Folder",
>                 "icon": "",
>                 "isFav": false
>             },
>             {
>                 "id": "dstNJhKwL0LAnRVVJd",
>                 "name": "New Datasheet”,
>                 "type": "Datasheet",
>                 "icon": "",
>                 "isFav": true
>             }
>         ]
>     },
>     "message": "SUCCESS"
>     }
> ```
