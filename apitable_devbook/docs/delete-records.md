---
title: Delete Records
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

We will show you how to [Delete records](/api/reference#operation/delete-records).

## Example: delete the two records for the specified datasheet

Assuming you have a datasheet, you would like to delete two of these records.

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

3. Gets the ID of the 2 records you want to delete.([How to get it](introduction.md#recordid))

4. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstWUHwzTHd2YQaXEE`, two record Id is `recADeOmeoJHg` and `recpveDCZYO`):
    ````mdx-code-block
    <Tabs
    groupId="delete records"
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
    curl -X DELETE \
    'https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/records?recordIds=recADeOmeoJHg,recfCpveDCZYO' \
    -H 'Authorization: Bearer {Your API Token}'
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

    datasheet.records.delete(["recADeOmeoJHg","recfCpveDCZYO"]).then(response => {
    if (response.success) {
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

    # Delete a single record
    record = dst.records.get(nickname="Anan")
    record.delete()

    # Delete the batch of records matching the query criteria
    dst.records.filter(weight="90 kg").delete()

    # Delete a record by recordId
    dst.delete_records([
    "recADeOmeoJHg",
    "recfCpveDCZYO"
    ])
    ```

    </TabItem>

    </Tabs>
    ````
5. The server returns the following JSON data, below the `"views"`  is all data in this view:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/delete-records) 
> 
> ```json
>     {
>    "success": true,
>    "code": 200,
>    "message": "SUCCESS",
>    "data": true
> }
> ```
