---
title: List Teams
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [List Teams](/api/reference#operation/list-teams) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage teams can use this API.
:::

## Example: Get a list of first-level teams in a space

If we regard space as a company, then the teams in space are the departments in the company.

Suppose you have a space and want to get the list of all teams in the first level.

Follow these steps:

1. Get your API token. ([How to get it](quick-start#get-api-token))

2. Get your space ID. ([How to get it](/api/introduction#spaceid))

3. Open the terminal on your computer and execute the following code to send a query request to the server (assuming `spaceId` is `spcjXzqVrjaP3` and the `unitId` of the team is `0` to get the first-level teams):
    ````mdx-code-block
    <Tabs
    groupId="list sub teams"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL', }
        ]
    }
    >

   <TabItem value="cURL">

   ```bash
   curl -X GET \
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/teams/0/children?pageSize=2&pageNum=1" \
   -H "Authorization: Bearer {Your API Token}" 
   ```

    </TabItem>

    </Tabs>
  `````

1. The server will return the following JSON data, with the team information under `"data"`:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/list-teams).

   ```json
   {
    "code": 200,
    "message": "SUCCESS",
    "success": true,
    "data": {
      "total": 2,
      "pageSize": 2,
      "pageNum": 1,
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
        },
        {
          "unitId": "bG9xSdV1fR6pMlN2tJyXkZzW5TjHcK4",
          "name": "team B",
          "sequence": 2,
          "parentUnitId": "0",
          "roles": [
            {
                "unitId": "zJ6TuQvH2RtNfSx9eY7XKgD1oWcE5pV",
                "name": "role A",
                "sequence": 1
            }
          ]
        }
      ]
    }
  }
   ```