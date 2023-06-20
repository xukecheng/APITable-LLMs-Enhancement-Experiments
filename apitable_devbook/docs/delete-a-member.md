---
title: Delete a Member

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````


This article provides an example of calling the [Delete a Member](/api/reference#operation/delete-a-member) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage members can use this API.
:::


## Example:

Suppose you have a space and you want to delete the member "John".

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the member "John" ([How to get it](/api/list-the-team-members))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3` and the unitId of member "John" is `kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6`):
   
    ````mdx-code-block
    <Tabs
    groupId="delete a member"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL', }
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X DELETE \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/members/kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6" \
   -H "Authorization: Bearer {Your API Token}" 
   ```

    </TabItem>

    </Tabs>
  ````

5. The server will return the following JSON data:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/delete-a-member)。

   ```json
   {
    "code": 200,
    "message": "SUCCESS",
    "success": true
   }
   ```
