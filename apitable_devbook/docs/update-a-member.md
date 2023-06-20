---
title: Update a Member

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [Update a Member](/api/reference#operation/update-a-member) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage members and roles can use this API.
:::


## Example:

Suppose you have a space and you want to change the team of member "John" to "Product team".

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the member "John" ([How to get it](/api/list-the-team-members))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Get the unitId of the team "Product team"（[How to get it](/api/list-teams)）

5. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3` and the unitId of member "John" is `kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6`, the unitId of team "Product team" is `E3jG1xNzR2iM4tL6XmYyKpFqWuV8vDc`):

   
    ````mdx-code-block
    <Tabs
    groupId="update a member"
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
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/members/kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6" \
   -H "Authorization: Bearer {Your API Token}" \
   -H 'Content-Type: application/json' \
   -d '{
     "teams":["E3jG1xNzR2iM4tL6XmYyKpFqWuV8vDc"]
   }'
   ```

    </TabItem>

    </Tabs>
  ````

6. The server will return the following JSON data. The data under `"data"` is the updated information of the member:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/update-a-member).

   ```json
   {
    "code": 200,
    "message": "SUCCESS",
    "success": true,
    "data":{
    "member": 
      {
        "unitId": "kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6",
        "name": "John",
        "avatar": "https://s1.apitable.com/public/2023/05/16/00a91wbb47fd0594fbc975d2d764a45q",
        "status": 1,
        "type": "Member",
        "teams": [
          {
            "unitId": "E3jG1xNzR2iM4tL6XmYyKpFqWuV8vDc",
            "name": "Product team",
            "sequence": 1,
            "parentUnitId": "YN3YT97EPGL9ZA0loc9V2kNQnWb9ivKW"
          }
        ],
        "roles": [
          {
            "unitId": "VS1SejiywaMWbiGMEHAohh62T9EPmmlh",
            "name": "role C",
            "sequence": 1,
          }
        ]
      } 
    }
   }
   ```