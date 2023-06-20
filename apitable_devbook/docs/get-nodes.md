---
title: Get Node List
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Get Node List](/api/reference#operation/get-nodes) interface.

## Example: Get the list of outermost nodes in the working directory of the specified space

Suppose you have a space and the working directory under the space holds a lot of files (such as datasheets, folders, forms and dashboards) and you want to get a list of the outermost nodes in this working directory.

> **Note:**
> 
> The "Get Node List" interface only supports returning the outermost list of files in the working directory. If you want to return a list of all nodes in the working directory, you can call both the [Get Node details](get-node-details) interface to do so. Alternatively, you can use the [Search Nodes](search-nodes) to retrieve a list of file nodes with specified types and permissions.

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get your Space ID.([How to get it](introduction.md#spaceid))

3. Open the terminal on your computer, execute the following code and send the query request to the server (e.g. `spaceId` is `spcX9P2xUcKst`):

    ````mdx-code-block
    <Tabs
    groupId="get nodes"
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
    "https://api.apitable.com/fusion/v1/spaces/spcX9P2xUcKst/nodes" \
    -H  "Authorization: Bearer {Your API Token}"
    ```

    </TabItem>

    <TabItem value="Javascript SDK">

    > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```js
    import { APITable } from 'apitable';

    const apitable = new APITable({
      token: 'Your API Token',
    });
    // Get the first-level file directory of the specified space
    const nodeListResp = await apitable.nodes.list({spaceId: 'spcX9P2xUcKst'})

    if (nodeListResp.success) {
      console.log(nodeListResp.data.nodes);
      const nodes = nodeListResp.data.nodes
      nodes.forEach(node=> {
        // When the node is a folder, you can execute the following code to get information about the files under the folder
        if (node.type === 'Folder') {
          const folderDetailResp = await apitable.nodes.get({spaceId: 'spcX9P2xUcKst', nodeId: node.id})
          if (folderDetailResp.success){
            // Print the child nodes under the folder
            console.log(folderDetailResp.data.children)
          }
        }
      })
    } else {
      console.error(nodeListResp);
    }
    ```

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    for node in apitable.space('spcX9P2xUcKst').nodes.all():
      print(node.name)
    ```

    </TabItem>

    </Tabs>
    ````
4. The server returns the following JSON data, with a list of the outermost files in the working directory returned under `"nodes"`.
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-nodes) 
> 
> ```json
>     {
>     "code": 200,
>     "success": true,
>     "data": {
>         "nodes": [
>         {
>             "id": "fom680eghkCem0wZxk",
>             "name": "New Form",
>             "type": "Form",
>             "icon": "",
>             "isFav": false
>         },
>         {
>             "id": "dsbWxTei5gdTvdAfKM",
>             "name": "New Dashboard",
>             "type": "Dashboard",
>             "icon": "",
>             "isFav": false
>         },
>         {
>             "id": "fod23ha5NvyM5",
>             "name": "New Folder",
>             "type": "Folder",
>             "icon": "",
>             "isFav": false
>         },
>         {
>             "id": "dstZsEg3RpBvsdCgop",
>             "name": "test-specific-template3",
>             "type": "Datasheet",
>             "icon": "",
>             "isFav": true
>         }
>         ]
>     },
>     "message": "SUCCESS"
>     }
> ```
