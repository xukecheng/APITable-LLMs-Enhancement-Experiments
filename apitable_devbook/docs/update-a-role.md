---
title: Update a Role

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [Update a role](/api/reference#operation/update-a-role) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage roles can use this API.
:::

## Example:

Suppose you have a space and you want to rename the role "Finance A" to "Finance" and adjust its sequence to 2.

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the role "Finance A". ([How to get it](/api/list-roles))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3` and the unitId of the role "Finance A" is `pL5rZ6E9vTjXzJ7fK3xSsV2GqNnYyM4`):

   ``````mdx-code-block
    <Tabs
    groupId="update a role"
    defaultValue="cURL"
    values={
        [
          { label: "cURL", value: 'cURL'}
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X PUT \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/roles/pL5rZ6E9vTjXzJ7fK3xSsV2GqNnYyM4" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
      "name":"Finance",
      "sequence":2002
   }'
   ```

    </TabItem>

    </Tabs>
  ``````

5. The server will return the following JSON data. The data under `"data"` is the information of the updated role:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/update-a-role).

   ```json
   {
      "code": 200,
      "success": true,
      "message": "SUCCESS",
      "data": {
        "role": {
          "unitId": "pL5rZ6E9vTjXzJ7fK3xSsV2GqNnYyM4",
          "name": "Finance",
          "sequence": 2002
        }
      }
   }
   ```