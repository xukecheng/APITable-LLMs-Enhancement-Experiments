---
title: Create a Team
---

```mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
```

This article provides an example of calling the [Create a Team](/api/reference#operation/create-a-team) API.

:::tip

- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage teams and roles can use this API.
  :::

## Example:

Assuming you have a space and want to create a team named "Product Team" under the "Product Development Department" team.

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the "Product Development Department" team. ([How to get it](/api/list-teams))

   > [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send an API request to the server (assuming the spaceId is `spcjXzqVrjaP3`, the unitId of the "Product Development Department" team is `eJ6mP5SbW8hF2Zl4YxRrXyKwDzQcTnN`, and the role "Product Designer" is associated with it, whose unitId is `bY5nKzT4LrJpHsN3jG7fW2mVcXvq8xQ`):

   ````mdx-code-block
   <Tabs
    groupId="create a team"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL', }
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X POST \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/teams" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
      "name":"Product Team",
      "sequence":1,
      "parentUnitId":"eJ6mP5SbW8hF2Zl4YxRrXyKwDzQcTnN",
      "roles":["bY5nKzT4LrJpHsN3jG7fW2mVcXvq8xQ"]
   }'
   ```

    </TabItem>

    </Tabs>
   ````

````

5. The server will return the following JSON data, the data under `"data"` is the information of the newly created team:

 > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/create-a-team).

 ```json
 {
   "code": 200,
   "message": "SUCCESS",
   "success": true,
   "data": {
      "team": {
        "unitId": "T6dCwJ9zUxYfKpV2kNvMmGtXqL1sHrS",
        "name": "Product Team",
        "sequence": 1,
        "parentUnitId": "eJ6mP5SbW8hF2Zl4YxRrXyKwDzQcTnN",
        "roles": [
          {
            "unitId": "bY5nKzT4LrJpHsN3jG7fW2mVcXvq8xQ",
            "name": "Product Designer",
            "sequence": 1
          }
        ]
      }
    }
 }
 ```
````
