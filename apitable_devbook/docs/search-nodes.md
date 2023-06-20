---
title: Search Nodes
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Search Nodes](/api/reference#operation/search-nodes) interface.

## Example: Search nodes by conditions

Assuming you have a Space with many files (such as Datasheets, Folders, Forms, Mirrors, and Dashboards) , you want to retrieve all datasheets for which you have "Manager" or "Editor" permissions.

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
        { label: "cURL", value: 'cURL', }
        ]
    }
    >

    <TabItem value="cURL">

    ```bash
    curl -X GET \
    "https://api.apitable.com/fusion/v2/spaces/spcX9P2xUcKst/nodes?type=Datasheet&permissions=0,1" \
    -H  "Authorization: Bearer {Your API Token}"
    ```

    </TabItem>

    </Tabs>
    ````

4. The server returns the following JSON data, with a list of nodes with specific types and permissions in the working directory returned under `"nodes"`.

> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/search-nodes)
> 
> ```json
> {
>    "code": 200,
>    "success": true,
>    "data": {
>        "nodes": [
>          {
>              "id": "dstXxx",
>              "name": "Test",
>              "type": "Datasheet",
>              "icon": "",
>              "isFav": false,
>              "parentId": "fodXxx",
>              "permission": 0
>          }
>        ]
>    },
>    "message": "SUCCESS"
> }
> ```
