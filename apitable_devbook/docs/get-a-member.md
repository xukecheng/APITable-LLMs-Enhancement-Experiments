---
title: Get a Member

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [Get a Member](/api/reference#operation/get-a-member) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage members can use this API.
:::

## Example: Get a member's information

Suppose you have a space and you want to get the information of member "John".

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the member "John". ([How to get it](/api/list-the-team-members))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3` and the unitId of member "John" is `kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6`):

   > Note: The member's email and mobile number are considered as sensitive data. To get them, you need to pass the Query parameter: sensitiveData=true.

    ````mdx-code-block
    <Tabs
    groupId="get a member"
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
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/members/kD8tPcZ3fYxSjV9qWvL5X2TmQbN1nR6?sensitiveData=true" \
   -H "Authorization: Bearer {Your API Token}" 
   ```
    </TabItem>

    </Tabs>
  ````

5. The server will return the following JSON data. The data under `"data"` is the information of the member:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-a-member).

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
        "mobile": {
            "number": "13000111000",
            "areaCode": "+86"
        },
        "email":"John@apitable.com",
        "avatar": "https://s1.apitable.com/public/2023/05/16/00a91wbb47fd0594fbc975d2d764a45q",
        "status": 1,
        "type": "Member",
        "teams": [
          {
            "unitId": "VS1SejiywaMWbiGMEHAohh62T9EPmmlh",
            "name": "team A",
            "sequence": 1,
            "parentUnitId": "0",
            "roles": [
              {
                  "unitId": "zJ6TuQvH2RtNfSx9eY7XKgD1oWcE5pV",
                  "name": "role A",
                  "sequence": 1
              }
            ]
          }
        ],
        "roles": [
          {
            "unitId": "c9EQqwN1pOEgjXqKJznPF6xF8t5TYTf0",
            "name": "role B",
            "sequence": 2
          }
        ]
      } 
    }
  }
   ```