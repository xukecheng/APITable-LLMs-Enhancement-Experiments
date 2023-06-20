---
title: Create a Role

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [Create a role](/api/reference#operation/create-a-role) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage roles can use this API.
:::

## Example: 

Suppose you have a space and you want to create a new role named "Finance".

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Open the terminal on your computer and execute the following code to send an API request to the server (assuming the spaceId is `spcjXzqVrjaP3`):

   `````mdx-code-block
    <Tabs
    groupId="create a role"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL'}
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X POST \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/roles" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
      "name":"Finance"
   }'
   ```

    </TabItem>

    </Tabs>
  `````

4. The server will return the following JSON data. The data under `"data"` is the information of the newly created role:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/create-a-role).

   ```json
   {
      "code": 200,
      "success": true,
      "message": "SUCCESS",
      "data": {
        "role": {
          "unitId": "W8tXqHs5KuRlV7vN4aJyZc2gM3fYpT6",
          "name": "Finance",
          "sequence": 2001
        }
	}
   }
   ```