---
title: List Roles

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [List Roles](/api/reference#operation/list-roles) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage roles can use this API.
:::

## Example: List all roles in a space

Suppose you have a space and want to get the list of all roles in the space.

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3`):

   ``````mdx-code-block
    <Tabs
    groupId="list roles"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL'}
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X GET \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/roles?pageSize=2&pageNum=1" \
   -H "Authorization: Bearer {Your API Token}"
   ```

    </TabItem>

    </Tabs>
  ``````

1. The server will return the following JSON data, with the role list data under `"data"`:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/list-roles).

   ```json
   {
     "code": 200,
     "message": "SUCCESS",
     "success": true,
     "data": {
      "total": 2,
      "pageSize": 2,
      "pageNum": 1,
      "roles": [
        {
            "unitId": "c9EQqwN1pOEgjXqKJznPF6xF8t5TYTf0",
            "name": "role A",
            "sequence": 1
        },
        {
            "unitId": "Q6sVrK4xL5JmG7pNnYyBvXcFzW1wTtH",
            "name": "role B",
            "sequence": 2
        },
      ]
     }
   }
   ```