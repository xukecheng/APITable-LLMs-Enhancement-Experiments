---
title: Get the List of Spaces
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Get the List of Spaces](/api/reference#operation/get-spaces)interface.

## Example: Get all the spaces you created or invited to enter

Suppose you have created a lot of spaces and are invited to enter many external spaces. You want to know the summary information of these spaces.

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Open the terminal on your computer, execute the following code, and send query requests to the server:

    ````mdx-code-block
    <Tabs
    groupId="get spaces"
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
    "https://api.apitable.com/fusion/v1/spaces" \
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
    // Get a list of spaces for the current user
    const spaceListResp = await apitable.spaces.list()

    if (spaceListResp.success) {
      console.log(spaceListResp.data.spaces);
    } else {
      console.error(spaceListResp);
    }
    ```

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    spaces = apitable.spaces.all()
    for space in spaces:
      print(space.json())
    ```

    </TabItem>

    </Tabs>
    ````
3. The server returns the following JSON data, below the `"spaces"` is all created three spaces:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-spaces) 
> 
> ```json
>     {
>     "code": 200,
>     "success": true,
>     "data": {
>         "spaces": [
>         {
>             "id": "spcX9P2xUcKst",
>             "name": "Coco's Space",
>             "isAdmin": true
>         },
>         {
>             "id": "spcDWQSdso7fi",
>             "name": "Test Space",
>             "isAdmin": true
>         },
>         {
>             "id": "spc56JRl8TBlX",
>             "name": "Invited External Space",
>         }
>         ]
>     },
>     "message": "SUCCESS"
>     }
> ```
