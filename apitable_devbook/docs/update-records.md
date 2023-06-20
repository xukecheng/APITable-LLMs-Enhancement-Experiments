---
title: Update Records
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

We will show you how to [Update records](/api/reference#operation/update-records).

## Example: updates the two records of the specified datasheet

Assuming you have a datasheet, you would like to update two of these records.

:::tip
The "id" attribute in the member field may be deprecated in the future. 
If you need to fill in the member field when creating or updating a record, please use the "unitId" attribute to add members.
:::

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

3. Get the ID of the 2 records you want to update.([How to get it](introduction.md#recordid))

4. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstWUHwzTHd2YQaXEE,`prior record Id is `recbaKEuZ9gDC` and `rec0dm5nsmS6`):

    ````mdx-code-block
    <Tabs
    groupId="update records"
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
    curl -X PATCH \
    https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/records \
    -H 'Authorization: Bearer {Your API Token}' \
    -H 'Content-Type: application/json' \
    -d '{
        "records": [
            {
                "recordId": "recbaKEuZ9gDC",
                "fields": {
                    "Nickname": "An An",
                    "Weight": "90kg"
                }
            },
            {
                "recordId": "rec09dm5nsmS6",
                "fields": {
                    "Nickname": "Jia Jia",
                    "Weight": "89kg"
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

    datasheet.records.update([
    {
        "recordId": "recbaKEuZ9gDC",
        fields:{
          "Nickname": "An An",
          "Weight": "90kg"
        }
    },
    {
        "recordId": "rec09dm5nsmS6",
        fields:{
          "Nickname": "Jia Jia",
          "Weight": "90kg"
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
    record = datasheet.records.get(Nickname="Anan")

    # Update a single field
    record.weight = "90kg"

    # Update multiple fields
    record.update({
      "nickname": "Xiaoan",
      "weight": "90kg",
    })

    # Return the updated record
    print(record.json())
    ```

    </TabItem>

    </Tabs>
    ````
5. The server returns the following JSON data, below the `"records"`  is updated data:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/update-records) 
> 
> ```json
>     {
>         "code": 200,
>         "success": true,
>         "data": {
>             "records": [
>                 {
>                     "recordId": "recbaKEuZ9gDC",
>                     "createdAt": 1600431195000,
>                     "fields": {
>                         "weight": "90kg",
>                         "shoulderHeight": "65cm",
>                         "registration_date": "2020/09/15 17:14",
>                         "Chest": "87cm",
>                         "body length": "1.2m",
>                         "Photo": [
>                             {
>                                 "id": "atcPtxnvqti5M",
>                                 "name": "6.gif",
>                                 "size": 33914,
>                                 "mimeType": "image/gif",
>                                 "token": "space/2020/09/22/01ee7202922d48688f61e34f12da5abc",
>                                 "width": 240,
>                                 "height": 240,
>                                 "url": "https://s1.apitable.com/space/2020/09/22/01ee7202922d48688f61e34f12da5abc"
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
>                         "nickname": "Anon",
>                         "age": "5 years old"
>                     }
>                 },
>                 {
>                     "recordId": "rec09dm5nsmS6",
>                     "createdAt": 1600431195000,
>                     "fields": {
>                         "weight": "89kg",
>                         "shoulderHeight": "66cm",
>                         "registration_date": "2020/09/15 17:14",
>                         "Chest": "89cm",
>                         "body length": "1.4m",
>                         "Photo": [
>                             {
>                                 "id": "atcPtxnvqti5M",
>                                 "name": "6.gif",
>                                 "size": 33914,
>                                 "mimeType": "image/gif",
>                                 "token": "space/2020/09/22/01ee7202922d48688f61e34f12da5abc",
>                                 "width": 240,
>                                 "height": 240,
>                                 "url": "https://s1.apitable.com/space/2020/09/22/01ee7202922d48688f61e34f12da5abc"
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
>                         "nickname": "Jiajia",
>                         "age": "6 years old"
>                     }
>                 }
>             ]
>         },
>         "message": "SUCCESS"
>     }
> ```

