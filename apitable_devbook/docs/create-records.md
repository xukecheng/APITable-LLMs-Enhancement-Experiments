---
title: Create Records
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

We will show you how to [Create records](/api/reference#operation/create-records).

## Example: creates two new records in the specified datasheet

Assume you have a datasheet, you want to create two new records in it.

:::tip
The "id" attribute in the member field may be deprecated in the future. 
If you need to fill in the member field when creating or updating a record, please use the "unitId" attribute to add members.
:::

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

3. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstWUHwzTHd2YQaXEE`):
    ````mdx-code-block
    <Tabs
    groupId="create records"
    defaultValue="cURL"
    values={
        [
        { label: "cURL", value: 'cURL', },
        { label: "Javascript SDK", value: 'Javascript SDK', },
        { label: "Python SDK", value: 'Python SDK', },
        ]
    }
    >

    <TabItem value="cURL">

    ```bash
    curl -X POST \
    https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/records \
    -H 'Authorization: Bearer {Your API Token}' \
    -H 'Content-Type: application/json' \
    -d '{
        "records": [
            {
                "fields": {
                    "weight": "80 kg",
                    "shoulder height": "65cm",
                    "registration date": "2020/09/15 17:14",
                    "chest": "87cm",
                    "body length": "1.2m",
                    "photo": [
                        {
                            "name": "image.png",
                            "size": 207456,
                            "mimeType": "image/png",
                            "token": "space/2020/09/21/f577af8bd73f44c79dfc28408eaeff83",
                            "width": 374,
                            "height": 347
                        }
                    ],
                    "registrars": [
                        {
                           "id": "1385370606558318594",
                           "unitId": "*********",
                           "name": "Coco",
                           "type": "Member",
                           "avatar": "https://s1.apitable.com/default/avatar004.jpg"
                        }
                    ],
                    "gender": "Boy",
                    "nickname": "An An",
                    "age": "5 years old"
                }
            },
            {
                "fields": {
                    "weight": "88 kg",
                    "shoulder height": "66cm",
                    "registration date": "2020/09/15 17:14",
                    "chest": "89cm",
                    "body length": "1.4m",
                    "photo": [
                        {
                            "name": "image.png",
                            "size": 395220,
                            "mimeType": "image/png",
                            "token": "space/2020/09/21/c42f476c01c24e8ca7908188d460f8f1",
                            "width": 400,
                            "height": 347
                        }
                    ],
                    "registrar": [
                        {
                           "id": "1379641203598823425",
                           "unitId": "*********",
                           "type": "Member",
                           "name": "Niko",
                           "avatar": "https://s1.apitable.com/default/avatar003.jpg"
                        }
                    ],
                    "gender": "Girl",
                    "nickname": "Jia Jia",
                    "age": "6 years old"
                }
            }
        ]
    }'
    ```

    </TabItem>

    <TabItem value="Javascript SDK">

    > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```js
   import { APITable } from 'apitable';

   const apitable = new APITable({
     token: 'Your API Token',
   });

    const datasheet = apitable.datasheet("dstWUHwzTHd2YQaXEE");

    datasheet.records.create([
    {
        fields:{
          "weight": "80 kg",
          "shoulder height": "65cm",
          "registration date": "2020/09/15 17:14",
          "chest": "87cm",
          "body length": "1.2m",
          "photo": [
              {
                  "name": "image.png",
                  "size": 207456,
                  "mimeType": "image/png",
                  "token": "space/2020/09/21/f577af8bd73f44c79dfc28408eaeff83",
                  "width": 374,
                  "height": 347
              }
          ],
          "registrar": [
              {
                  "type": "Member",
                  "name": "Bruce · K"
              }
          ],
          "gender": "Boy",
          "nickname": "An An",
          "age": "5 years old"
        }
    },
    {
        fields:{
          "weight": "88 kg",
          "shoulder height": "66cm",
          "registration date": "2020/09/15 17:14",
          "chest": "89cm",
          "body length": "1.4m",
          "photo": [
              {
                  "name": "image.png",
                  "size": 395220,
                  "mimeType": "image/png",
                  "token": "space/2020/09/21/c42f476c01c24e8ca7908188d460f8f1",
                  "width": 400,
                  "height": 347
              }
          ],
          "registrar": [
              {
                  "unitId": "*********"
              }
          ],
          "gender": "Girl",
          "nickname": "Jia Jia",
          "age": "6 years old"
        }
    }
    ]).then(response => {
    if (response.success) {
      console.log(response.data.records);
    } else {
      console.error(response);
    }
    });
    ```

    </TabItem>

   <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dstWUHwzTHd2YQaXEE")

    records = dst.records.create([
    {
        "weight": "80 kg",
        "shoulder height": "65cm",
        "registration date": "2020/09/15 17:14",
        "chest": "87cm",
        "body length": "1.2m",
        "photo": [
            {
                "name": "image.png",
                "size": 207456,
                "mimeType": "image/png",
                "token": "space/2020/09/21/f577af8bd73f44c79dfc28408eaeff83",
                "width": 374,
                "height": 347
            }
        ],
        "registrar": [
            {
                "type": "Member",
                "name": "Bruce · K"
            }
        ],
        "gender": "Boy",
        "nickname": "An An",
        "age": "5 years old"
    },
    {
        "weight": "88 kg",
        "shoulder height": "66cm",
        "registration date": "2020/09/15 17:14",
        "chest": "89cm",
        "body length": "1.4m",
        "photo": [
            {
                "name": "image.png",
                "size": 395220,
                "mimeType": "image/png",
                "token": "space/2020/09/21/c42f476c01c24e8ca7908188d460f8f1",
                "width": 400,
                "height": 347
            }
        ],
        "registrar": [
            {
                "unitId": "*********"
            }
        ],
        "gender": "Girl",
        "nickname": "Jia Jia",
        "age": "6 years old"
    }
    ])
    ```

    </TabItem> 

    </Tabs>
    ````
4. The server returns the following JSON packets, below the `"records"`  is new data:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/create-records) 
> 
> ```json
>     {
>         "code": 200,
>         "success": true,
>         "data": {
>             "records": [
>                 {
>                     "recordId": "reclxDBUBjQo6",
>                     "createdAt": 1600708683000,
>                     "fields": {
>                         "weight": "80kg",
>                         "shoulderHeight": "65cm",
>                         "registration_date": "2020/09/15 17:14",
>                         "Chest": "87cm",
>                         "body length": "1.2m",
>                         "Photo": [
>                             {
>                                 "id": "atcUJME9gbmFQ",
>                                 "name": "1.png",
>                                 "size": 207456,
>                                 "mimeType": "image/png",
>                                 "token": "space/2020/09/21/f577af8bd73f44c79dfc28408eaeff83",
>                                 "width": 374,
>                                 "height": 347,
>                                 "url": "https://s1.apitable.com/space/2020/09/21/f577af8bd73f44c79dfc28408eaeff83"
>                             }
>                         ],
>                         "registrar": [
>                             {
>                                 "id": "1286184164530659329",
>                                 "unitId": "*********",
>                                 "type": "Member",
>                                 "name": "Bruce - K",
>                                 "avatar": "https://s1.apitable.com/public/2020/08/03/574bcee4cfc54f6fbb7d686bb237f6f3"
>                             }
>                         ],
>                         "gender": "boy",
>                         "age": "5 years old"
>                     }
>                 },
>                 {
>                     "recordId": "reckuCT1F1Asn",
>                     "createdAt": 1600708683000,
>                     "fields": {
>                         "weight": "88kg",
>                         "shoulderHeight": "66cm",
>                         "registration_date": "2020/09/15 17:14",
>                         "Chest": "89cm",
>                         "body length": "1.4m",
>                         "Photo": [
>                             {
>                                 "id": "atcSvAn7wEBtJ",
>                                 "name": "image.png",
>                                 "size": 395220,
>                                 "mimeType": "image/png",
>                                 "token": "space/2020/09/21/c42f476c01c24e8ca7908188d460f8f1",
>                                 "width": 400,
>                                 "height": 347,
>                                 "url": "https://s1.apitable.com/space/2020/09/21/c42f476c01c24e8ca7908188d460f8f1"
>                             }
>                         ],
>                         "registrar": [
>                             {
>                                 "id": "1291258301781176321",
>                                 "unitId": "*********",
>                                 "type": "Member",
>                                 "name": "Aoi🌻",
>                                 "avatar": "https://s1.apitable.com/public/2020/09/07/dbfe6ceccbdb4d5bbc1fd129566dea89"
>                             }
>                         ],
>                         "gender": "girl",
>                         "age": "6 years old"
>                     }
>                 }
>             ]
>         },
>         "message": "SUCCESS"
>     }
> ```
