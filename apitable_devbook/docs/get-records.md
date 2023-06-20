---
title: Get Records
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Get records](/api/reference#operation/get-records) interface.

## Example 1: Get all records in the specified view under the specified APITable

Suppose you have a datasheet, and you want to get all the records in the "Grid View".

![Log action - Example datasheet](media/get-record-example.png)

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the dastasheet ID([How to get it](introduction.md#datasheetid)) and 'Grid view' ID([How to get it](introduction.md#viewid)).

3. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstWUHwzTH2YQaXEE`, viewId is `viw4mnkqkaqdh`):

    ````mdx-code-block
    <Tabs
    groupId="get records"
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

    > Note: When sending query requests via cURL, the encodeURIComponent() function is required to escape the values of the query parameters.

    ```bash
    curl -X GET \
    "https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/records?viewId=viw4mnkqkaqdh" \
    -H "Authorization: Bearer {Your API Token}"
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
    // Get records in pages, return to the first page by default
    datasheet.records.query({ viewId: "viw4mnkqkaqdh"}).then(response => {
    if (response.success) {
      console.log(response.data.records);
    } else {
      console.error(response);
    }
    });

    // Automatically handles paging and iteratively returns all records.
    const recordsIter = datasheet.records.queryAll({ viewId: "viw4mnkqkaqdh"})
    // for await needs to be run in an async function and requires a browser/node version.See https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements/for-await... .of
    for await (const eachPageRecords of recordsIter){
      console.log(eachPageRecords)
    }
    ```

    The `query` and `queryAll` methods support passing in multiple parameters to customize the set of records returned.The supported parameters are consistent with the query parameters in [API Reference "Get Records"](/api/reference#operation/get-records).

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dstWUHwzTHd2YQaXEE")
    records = dst.records.all(viewId="viw4mnkqkaqdh")
    for record in records:
      print(record.json())
    ```

    The `all` method supports passing in multiple parameters to customize the returned recordset.The supported parameters are consistent with the query parameters in [API Reference "Get Records"](/api/reference#operation/get-records).

    </TabItem>

    </Tabs>
    ````
4. The server returns the JSON data below which records are required under records:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-records) 
> 
> ```json
>     {
>         "code": 200,
>         "success": true,
>         "data": {
>             "total": 3,
>             "pageNum": 1,
>             "pageSize": 3,
>             "records": [
>                 {
>                     "recordId": "reciVgKCRJhCd",
>                     "createdAt": 1659459289000,
>                     "uploadedAt": 1659459933000,
>                     "fields": {
>                         "features": [
>                             "gluttonous",
>                             "sleepy",
>                             "lively"
>                         ],
>                         "create time": 1659459289490,
>                         "health check date": [
>                             1659283200000,
>                             1661961600000
>                         ],
>                         "health check": [
>                             "reczjPnU9tTkJ",
>                             "rec1fXsdmjOOD"
>                         ],
>                         "photo": [
>                             {
>                                 "id": "atcEuF1pgKFSm",
>                                 "name": "image_1.jpeg",
>                                 "size": 1684539,
>                                 "mimeType": "image/jpeg",
>                                 "token": "space/2022/08/03/831b7a8ebda84d16abc5006f38d29483",
>                                 "width": 2592,
>                                 "height": 3872,
>                                 "url": "https://s1.apitable.com/space/2022/08/03/831b7a8ebda84d16abc5006f38d29483"
>                             }
>                         ],
>                         "body_length": 1.2,
>                         "creator": {
>                             "id": "defa8eadd75648cca0a0125c2f9445c9",
>                             "unitId": "*********",
>                             "name": "Yang Weiming",
>                             "avatar": "https://s1.apitable.com/space/2020/09/11/e4d073b1fa674bc884a8c194e9248ecf"
>                         },
>                         "age": "5 years old",
>                         "nickname": "An An",
>                         "guardian": [
>                             {
>                                 "id": "1395644188512026652",
>                                 "unitId": "*********",
>                                 "type": "Member",
>                                 "name": "Yang Weiming",
>                                 "avatar": "https://s1.apitable.com/space/2020/09/11/e4d073b1fa674bc884a8c194e9248ecf"
>                             }
>                         ],
>                         "weight": 90,
>                         "chest": 87,
>                         "gender": "boy",
>                         "registered or not": true
>                     }
>                 },
>                 {
>                     "recordId": "rec5oAO1IwVmB",
>                     "createdAt": 1659459289000,
>                     "uploadedAt": 1659460724000,
>                     "fields": {
>                         "features": [
>                             "obedient",
>                             "lively"
>                         ],
>                         "create time": 1659459289490,
>                         "health check date": [
>                             1659283200000,
>                             1661961600000
>                         ],
>                         "health check": [
>                             "recaXVhw4AoAx",
>                             "reccOYxRDPHdA"
>                         ],
>                         "photo": [
>                             {
>                                 "id": "atcuMRSi1Bztg",
>                                 "name": "image_2.jpeg",
>                                 "size": 1684539,
>                                 "mimeType": "image/jpeg",
>                                 "token": "space/2022/08/03/831b7a8ebda84d16abc5006f38d29483",
>                                 "width": 2592,
>                                 "height": 3872,
>                                 "url": "https://s1.apitable.com/space/2022/08/03/831b7a8ebda84d16abc5006f38d29483"
>                             }
>                         ],
>                         "body_length": 1.52,
>                         "creator": {
>                             "id": "defa8eadd75648cca0a0125c2f9445c9",
>                             "unitId": "*********",
>                             "name": "Yang Weiming",
>                             "avatar": "https://s1.apitable.com/space/2020/09/11/e4d073b1fa674bc884a8c194e9248ecf"
>                         },
>                         "age": "7 years old",
>                         "nickname": "Xiaoxiao",
>                         "guardian": [
>                             {
>                                 "id": "1395644188512026652",
>                                 "unitId": "*********",
>                                 "type": "Member",
>                                 "name": "Yang Weiming",
>                                 "avatar": "https://s1.apitable.com/space/2020/09/11/e4d073b1fa674bc884a8c194e9248ecf"
>                             }
>                         ],
>                         "weight": 110,
>                         "chest": 71,
>                         "gender": "girl",
>                         "registered or not": true
>                     }
>                 },
>                           {
>                     "recordId": "recqNslHPuU13",
>                     "createdAt": 1659459289000,
>                     "uploadedAt": 1659459941000,
>                     "fields": {
>                         "features": [
>                             "sleepy",
>                             "quiet"
>                         ],
>                         "create time": 1659459289490,
>                         "health check date": [
>                             1659283200000,
>                             1661961600000
>                         ],
>                         "health check": [
>                             "rec0kjjE3WkwK",
>                             "reca7dxHhe237"
>                         ],
>                         "photo": [
>                             {
>                                 "id": "atcGT6nF7yPXb",
>                                 "name": "image_3.jpeg",
>                                 "size": 1684539,
>                                 "mimeType": "image/jpeg",
>                                 "token": "space/2022/08/03/831b7a8ebda84d16abc5006f38d29483",
>                                 "width": 2592,
>                                 "height": 3872,
>                                 "url": "https://s1.apitable.com/space/2022/08/03/831b7a8ebda84d16abc5006f38d29483"
>                             }
>                         ],
>                         "body_length": 1.4,
>                         "creator": {
>                             "id": "defa8eadd75648cca0a0125c2f9445c9",
>                             "unitId": "*********",
>                             "name": "Yang Weiming",
>                             "avatar": "https://s1.apitable.com/space/2020/09/11/e4d073b1fa674bc884a8c194e9248ecf"
>                         },
>                         "age": "6 years old",
>                         "nickname": "Jiajia",
>                         "guardian": [
>                             {
>                                 "id": "1395644188512026652",
>                                 "unitId": "*********",
>                                 "type": "Member",
>                                 "name": "Yang Weiming",
>                                 "avatar": "https://s1.apitable.com/space/2020/09/11/e4d073b1fa674bc884a8c194e9248ecf"
>                             }
>                         ],
>                         "weight": 88,
>                         "chest": 66,
>                         "gender": "girl",
>                         "registered or not": true
>                     }
>                 }
>             ]
>         },
>         "message": "SUCCESS"
>     }
> ```

## Example 2: specifies the fields to be included in the record returned

Assuming you have a datasheet you want to get all of these records and these records contain only two fields of nickname 'age'.

![Log action - Example datasheet](media/get-record-example.png)

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Gets the ID ([How to get it](introduction.md#datasheetid)) and Nickname for both fields ([How to get it](introduction.md#fieldId)).

3. Open the terminal on your computer, execute the following code and send the query request to the server (assuming dstWUHwzTH2YQaXEEE, `dstWUHwzTH2YQaXEE,`field id for 'nickname' fields `fldY2RQCZ1ycC` and `fldBmgui8bhNt`):

    ````mdx-code-block
    <Tabs
    groupId="get records query fields"
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

    > Note: When sending query requests via cURL, the encodeURIComponent() function is required to escape the values of the query parameters.

    ```bash
    # Query before encoding, for demonstration purposes only, direct execution may report an error "[fields] value is incorrect"
    curl -X GET \
    "https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/records?fields=nickname,age" \
    -H "Authorization: Bearer {Your API Token}"

    # The encoded query can be executed directly
    curl -X GET \
    "https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/records?fields%5B%5D%3D%E6%98%B5%E7%A7%B0%26fields%5B%5D%3D%E5%B9%B4%E9%BE%84" \
    -H "Authorization: Bearer {Your API Token}"
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
    // Get records in pages, return to the first page by default
    datasheet.records.query({ fields: ["nickname", "age"] }).then(response => {
    if (response.success) {
      console.log(response.data.records);
    } else {
      console.error(response);
    }
    });
    ```

    The `query` and `queryAll` methods support passing in multiple parameters to customize the set of records returned.The supported parameters are consistent with the query parameters in [API Reference "Get Records"](/api/reference#operation/get-records).

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    </TabItem>

    </Tabs>```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dstWUHwzTHd2YQaXEE")
    records = dst.records.all(fields=["nickname", "age"])
    for record in records:
      print(record.json())
    ```

    The `all` method supports passing in multiple parameters to customize the returned recordset.

    The supported parameters are consistent with the query parameters in [API Reference "Get Records"](/api/reference#operation/get-records).
    ````
4. The server returns the following JSON packets, records are eligible under records:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-records) 
> 
> ```json
>     {
>         "code": 200,
>         "success": true,
>         "data": {
>             "total": 3,
>             "pageNum": 1,
>             "pageSize": 3,
>             "records": [
>                 {
>                     "recordId": "reciVgKCRJhCd",
>                     "createdAt": 1659459289000,
>                     "updatedAt": 1659459933000,
>                     "fields": {
>                         "nickname": "An An",
>                         "age": "5 years old"
>                     }
>                 },
>                 {
>                     "recordId": "rec5oAO1IwVmB",
>                     "createdAt": 1659459289000,
>                     "updatedAt": 1659460724000,
>                     "fields": {
>                         "nickname": "Xiao Xiao",
>                         "age": "7 years old"
>                     }
>                 },
>                 {
>                     "recordId": "recqNslHPuU13",
>                     "createdAt": 1659459289000,
>                     "updatedAt": 1659459941000,
>                     "fields": {
>                         "nickname": "Jia Jia",
>                         "age": "6 years old"
>                     }
>                 }
>             ]
>         },
>         "message": "SUCCESS"
>     }
> ```

## Example 3: Gets a record of the specified filters and quantities, and customize the sort

Suppose you have a [datasheet](https://apitable.com/share/shrYK1XCEWFKWDhTdC0Mo/dsteXU5G2h7B0QelRm/viwnNMtzK7mMp), you want to filter out 3 products whose "main selling points" contains the keywords "Vacuum" or "Thermal isulation", and sort them by promotional price from high to low.

![Log action - Example datasheet2](media/records-example-2.png)

Two query parameters are required here:

- `filterByFormula`: value is `OR(find("Vacuum", {main selling point}) > 0, find("Thermal insulation", {main selling point}) > 0)`
- `maxRecords`: value is `3`
- `sort`: value is `{"field": "promotion price", "order": "desc"}`

For a detailed description of the query parameters, see [API Handbook "Get Records"](/api/reference#operation/get-records)

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))
2. Get datasheet Id ([How to get it](introduction.md#datasheetid)).
3. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstNrmvismEKLSMn2Q`):

    ````mdx-code-block
    <Tabs
    groupId="get records filterByFormula and sort"
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

    > Note: When sending query requests via cURL, the encodeURIComponent() function is required to escape the values of the query parameters.

    ```bash
    curl -X GET \
    'https://api.apitable.com/fusion/v1/datasheets/dstNrmvismEKLSMn2Q/records?filterByFormula=OR(find("Vacuum", {main selling Points}) > 0, find("Thermal insulation", {main selling points}) > 0)&maxRecords=3&sort={"field": "promotion price", "order": "desc"}' \
    -H "Authorization: Bearer {Your API Token}"
    ```

    </TabItem>

    <TabItem value="Javascript SDK">

    > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```js
    import { APITable } from 'apitable';

    const apitable = new APITable({
      token: 'Your API Token',
    });
    const datasheet = apitable.datasheet("dstNrmvismEKLSMn2Q");
    // Get records in pages, return to the first page by default
    datasheet.records.query({ filterByFormula: 'OR(find("Vacuum", {Main Selling Points}) > 0, find("Thermal insulation", {Main Selling Points}) > 0)', maxRecords: 3, sort: [{"field": "Promotion Price", "order": "desc"}]}).then(response => {
    if (response.success) {
      console.log(response.data.records);
    } else {
      console.error(response);
    }
    });
    ```

    The `query` and `queryAll` methods support passing in multiple parameters to customize the set of records returned.The supported parameters are consistent with the query parameters in [API Reference "Get Records"](/api/reference#operation/get-records).

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dstNrmvismEKLSMn2Q")
    records = dst.records.all(filterByFormula='OR(find("Vacuum", {Main Selling Points}) > 0, find("Thermal insulation", {Main Selling Points}) > 0)', maxRecords=3, sort=[{"field": "Promotion Price", "order": "desc"}])
    for record in records:
      print(record.json())
    ```

    The `all` method supports passing in multiple parameters to customize the returned recordset.The supported parameters are consistent with the query parameters in [API Reference "Get Records"](/api/reference#operation/get-records).

    </TabItem>

    </Tabs>
    ````
4. The server returns the following JSON packets, records are eligible under records:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/get-records) 
> 
> ```json
>     {
>     "code": 200,
>     "success": true,
>     "data": {
>         "total": 3,
>         "records": [
>             {
>                 "recordId": "recX1UxK12bIo",
>                 "createdAt": 1671589943000,
>                 "updatedAt": 1671597856000,
>                 "fields": {
>                     "original price": 399,
>                     "promotion price": 369,
>                     "inbound time": 1671589943382,
>                     "title": "Life multifunctional cup",
>                     "picture": [
>                         {
>                             "id": "atcbGfpA2Jc6O",
>                             "name": "image.png",
>                             "size": 3539,
>                             "mimeType": "image/png",
>                             "token": "space/2022/12/21/085bb750ba3a4eccbaf68c74f8e92734",
>                             "width": 48,
>                             "height": 49,
>                             "url": "https://s1.apitable.com/space/2022/12/21/085bb750ba3a4eccbaf68c74f8e92734"
>                         }
>                     ],
>                     "main selling points": [
>                         "High-borosilicate glass",
>                         "Cook",
>                         "Thermal insulation"
>                     ]
>                 }
>             },
>             {
>                 "recordId": "rectaGRaNuGYU",
>                 "createdAt": 1671589943000,
>                 "updatedAt": 1671597856000,
>                 "fields": {
>                     "original price": 299,
>                     "promotion price": 239,
>                     "inbound time": 1671589943382,
>                     "title": "Juice Cup",
>                     "picture": [
>                         {
>                             "id": "atcbGfpA2Jc6O",
>                             "name": "image.png",
>                             "size": 3539,
>                             "mimeType": "image/png",
>                             "token": "space/2022/12/21/085bb750ba3a4eccbaf68c74f8e92734",
>                             "width": 48,
>                             "height": 49,
>                             "url": "https://s1.apitable.com/space/2022/12/21/085bb750ba3a4eccbaf68c74f8e92734"
>                         }
>                     ],
>                     "main selling points": [
>                         "Vacuum",
>                         "Push Button Type"
>                     ]
>                 }
>             },
>             {
>                 "recordId": "recZ9ZLTXVFPc",
>                 "createdAt": 1671589943000,
>                 "updatedAt": 1671597856000,
>                 "fields": {
>                     "original price": 149,
>                     "promotion price": 129,
>                     "inbound time": 1671589943382,
>                     "title": "Electric heating water cup",
>                     "picture": [
>                         {
>                             "id": "atcbGfpA2Jc6O",
>                             "name": "image.png",
>                             "size": 3539,
>                             "mimeType": "image/png",
>                             "token": "space/2022/12/21/085bb750ba3a4eccbaf68c74f8e92734",
>                             "width": 48,
>                             "height": 49,
>                             "url": "https://s1.apitable.com/space/2022/12/21/085bb750ba3a4eccbaf68c74f8e92734"
>                         }
>                     ],
>                     "main selling points": [
>                         "Electric hot water bottle",
>                         "Thermal insulation"
>                     ]
>                 }
>             }
>         "pageSize": 3
>         ],
>         "pageNum": 1,
>     },
>     "message": "SUCCESS"
> }
> ```
