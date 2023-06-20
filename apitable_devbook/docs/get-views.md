---
title: Get Views
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Get views](/api/reference#operation/get-views) interface.

## Example: Get all views of a specified APITable

Suppose you have a channel sales inventory summary datasheet and you want to get information about all the views of this datasheet.

![Get views demo](media/views-example.jpg)

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

3. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dst0vPx2577RdMN9MC`):

    ````mdx-code-block
    <Tabs
    groupId="get views"
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
    "https://api.apitable.com/fusion/v1/datasheets/dst0vPx2577RdMN9MC/views" \
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
    const datasheet = apitable.datasheet("dst0vPx2577RdMN9MC");
    const viewsResp = await datasheet.views.list()

    if (viewsResp.success) {
      console.log(viewsResp.data.views);
    } else {
      console.error(viewsResp);
    }
    ```

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dst0vPx2577RdMN9MC")
    views = dst.views.all()
    for view in views:
      print(view.json())
    ```

    </TabItem>

    </Tabs>
    ````
4. The server returns the following JSON data, below the `"views"`  is all data in this view:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-views) 
> 
> ```json
>     {
>     "code": 200,
>     "success": true,
>     "data": {
>         "views": [
>             {
>                 "id": "viwBBD0FJmGgl",
>                 "name": "Grid view",
>                 "type": "Grid"
>             },
>             {
>                 "id": "viwHikMoyvm3U",
>                 "name": "Gallery",
>                 "type": "Gallery"
>             },
>             {
>                 "id": "viwZbTXzYeLOm",
>                 "name": "Brand Grouping",
>                 "type": "Grid"
>             },
>             {
>                 "id": "viwi88msbLv50",
>                 "name": "Kanban",
>                 "type": "Kanban"
>             },
>             {
>                 "id": "viwWwIQcQKdKw",
>                 "name": "Gantt",
>                 "type": "Gantt"
>             }
>         ]
>     },
>     "message": "SUCCESS"
> }
> ```