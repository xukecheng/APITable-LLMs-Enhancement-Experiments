---
title: List the Team Members 
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [List the Team Members](/api/reference#operation/list-the-team-members) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage teams and members can use this API.
:::

## Example: Get a list of members in a team

Assume that you have a team named "Development Team" and you want to get a list of all members in this team.

Follow these steps:

1. Get your API token. ([How to get it](quick-start#get-api-token))

2. Get your space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the team "Development Team". ([How to get it](/api/list-teams))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send a query request to the server (assuming `spaceId` is `spcjXzqVrjaP3`, `unitId` of the team is `VS1SejiywaMWbiGMEHAohh62T9EPmmlh`, `sensitiveData` is set to `true` to return the email and mobile phone information of the members):
   
    ````mdx-code-block
    <Tabs
    groupId="list the team members"
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
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/teams/VS1SejiywaMWbiGMEHAohh62T9EPmmlh/members?pageSize=2&pageNum=1&sensitiveData=true" \
   -H "Authorization: Bearer {Your API Token}"
   ```

    </TabItem>

      </Tabs>
  `````

5. The server will return the following JSON data, with the member information under `"data"`:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/list-the-team-members).

   ```json
   {
    "code": 200,
    "message": "SUCCESS",
    "success": true,
    "data": {
      "total": 2,
      "pageSize": 2,
      "pageNum": 1,
      "members": [
        {
          "unitId": "P8eYsXuL6pZ3mT9cN7gVjKwA2hBq4Ft",
          "name": "John",
          "mobile": {
              "number": "12345678901",
              "areaCode": "+86"
          },
          "email":"john@apitable.com",
          "avatar": "https://s1.apitable.com/public/2023/05/16/00a91wbb47fd0594fbc975d2d764a45q",
          "status": 1,
          "type": "PrimaryAdmin",
          "teams": [{
              "unitId": "VS1SejiywaMWbiGMEHAohh62T9EPmmlh",
              "name": "Development Team",
              "sequence": 1,
              "parentUnitId": "YN3YT97EPGL9ZA0loc9V2kNQnWb9ivKW"
          }],
          "roles": [{
              "unitId": "c9EQqwN1pOEgjXqKJznPF6xF8t5TYTf0",
              "name": "Front-end Developer",
              "sequence": 1
            }]
        },
        {
          "unitId": "aDfT7yGpJ5rVcN2xZ8nQzKuWkMl4SbH",
          "name": "Tom"
          "mobile": {
              "number": "13456789012",
              "areaCode": "+86"
          }
          "email": "test2@apitable.com",
          "avatar": "https://s1.apitable.com/public/2023/05/16/00a91wbb47fd0594fbc975d2d764a45q",
          "status": 1,
          "type": "Member",
          "teams": [{
              "unitId": "VS1SejiywaMWbiGMEHAohh62T9EPmmlh",
              "name": "Development Team",
              "sequence": 1,
              "parentUnitId": "YN3YT97EPGL9ZA0loc9V2k