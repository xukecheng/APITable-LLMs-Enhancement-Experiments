---
title: List Units under the Role

---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This article provides an example of calling the [List Units under the Role](/api/reference#operation/list-units-under-the-role) API.

:::tip
- This API is only available for spaces on the enterprise plan.([Learn more](https://apitable.com/pricing)).
- Only the primary admin and sub-admins who can manage roles can use this API.
:::

## Example: Get the list of members and teams with the specific role

A role contains members and teams that have the same functionality. 

For example, the role named "product manager" contains the product management team and members who are product managers, [learn more about Role](https://help.apitable.com/docs/guide/role)

Suppose you have a space and want to get the list of all members and teams in the "Product designer" role.

Follow these steps:

1. Get your API Token. ([How to get it](quick-start#get-api-token))

2. Get your Space ID. ([How to get it](/api/introduction#spaceid))

3. Get the unitId of the "Product designer" role ([How to get it](/api/list-roles))
> [What is unitId?](/api/faqs#what-is-the-meaning-of-unitid-in-the-contacts-api)

4. Open the terminal on your computer and execute the following code to send a query request to the server (assuming the spaceId is `spcjXzqVrjaP3` and the unitId of "Product designer" role is `bV1wL8uG5iZnXz9xR7rMjYsKfPpTcHq`):

   ``````mdx-code-block
    <Tabs
    groupId="list units under the role"
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
   "https://api.apitable.com/fusion/v1/spaces/spcjXzqVrjaP3/roles/bV1wL8uG5iZnXz9xR7rMjYsKfPpTcHq/units" \
   -H "Authorization: Bearer {Your API Token}" 
   ```

    </TabItem>

    </Tabs>
  ``````

5. The server will return the following JSON data. The data under `"data"` is the members and teams data under the role:

   > For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/list-units-under-the-role).

   ```json
   {
     "code": 200,
     "message": "SUCCESS",
     "success": true,
     "data": {
       "members": [
          {
            "unitId": "K2QmXjH1tLzSsZbYyVWv6gUoP9wN7pC",
            "name": "John",
            "mobile": {
                "number": "14567890123",
                "areaCode": "+86"
            }
            "email": "test3@apitable.com",
            "avatar": "https://s1.apitable.com/public/2023/05/16/00a91wbb47fd0594fbc975d2d764a45q",
            "status": 1,
            "type": "Member",
            "teams": [{
                "unitId": "aDfT7yGpJ5rVcN2xZ8nQzKuWkMl4SbH",
                "name": "Product team",
                "sequence": 3,
                "parentUnitId": "0"
            }],
            "roles": [{
                "unitId": "bV1wL8uG5iZnXz9xR7rMjYsKfPpTcHq",
                "name": "Product designer",
                "sequence": 1         
            }]
          }
        ],
        "teams": [
        {
          "unitId": "VS1SejiywaMWbiGMEHAohh62T9EPmmlh",
          "name": "team A",
          "sequence": 1,
          "parentUnitId": "0",
          "roles": [
            {
                "unitId": "bV1wL8uG5iZnXz9xR7rMjYsKfPpTcHq",
                "name": "Product designer",
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
                "unitId": "bV1wL8uG5iZnXz9xR7rMjYsKfPpTcHq",
                "name": "Product designer",
                "sequence": 1
            }
          ]
        }
      ]
     }
   }
   ```