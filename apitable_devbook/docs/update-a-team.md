---
title: Update a Team

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [Update a Team](/api/reference#operation/update-a-team) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage teams and roles can use this API.
:::

## Example:

Suppose you have a space and you want to change the name of the "Product Group" to "Product Department" and modify its sequence to 2.

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the "Product Group" ([How to get it](/api/list-teams))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3` and the unitId of the "Product Group" is `E3jG1xNzR2iM4tL6XmYyKpFqWuV8vDc`):

   ``````mdx-code-block
    <Tabs
    groupId="update a team"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL', }
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X PUT \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/teams/E3jG1xNzR2iM4tL6XmYyKpFqWuV8vDc" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
      "name": "Product Department",
      "sequence":2
   }'
   ```

   </TabItem>

   </Tabs>
  ``````

5. The server will return the following JSON data, with the updated team information under the `"data"`:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/update-a-team).

   ```json
   {
     "code": 200,
     "message": "SUCCESS",
     "success": true,
     "data": {
        "team": {
          "unitId": "E3jG1xNzR2iM4tL6XmYyKpFqWuV8vDc",
          "name": "Product Department",
          "sequence":2, 
          "parentUnitId":"YN3YT97EPGL9ZA0loc9V2kNQnWb9ivKW",
          "roles": []
		    }
     }
   }
   ```