---
title: Uploading Attachments
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This text provides an example of how to call [Upload attachments](/api/reference#tag/attachment) interface.

## Example: Upload an attachment and bind to APITable

Suppose you have a picture, you want to upload the picture to APITable

Your action steps below:

1. Get your API Token.([How to get it](quick-start.md#get-api-token))

2. Get the ID of the datasheet.([How to get it](introduction.md#datasheetid))

3. Get your absolute path of your local picture.

4. Open the terminal on your computer, execute the following code and send the query request to the server (assuming datasheetId is `dstWUHwzTHd2YQaXEE`, path of local pictures is `/Users/coco/Documents/3.jpg`):

    ````mdx-code-block
    <Tabs
    groupId="upload attachments"
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
    https://api.apitable.com/fusion/v1/datasheets/dstWUHwzTHd2YQaXEE/attachments \
    -H 'Authorization: Bearer {Your API Token}' \
    -H 'content-type: multipart/form-data' \
    -F 'file=@/Users/coco/Documents/3.jpg'
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
    // in the node environment

    const file = fs.createReadStream('/Users/coco/Documents/3.jpg')

    try {
      const resp = await datasheet.upload(file)
      if (resp.success) {
        const uploaded_attachments = resp.data
        await apitable.datasheet('dstWUHwzTHd2YQaXEE').records.create([{
          'title': 'Title A',
          'photos': [uploaded_attachments]
          }])
      }
    } catch (error) {
      console.error(error)
    }
    ```

    </TabItem>

    <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    dst = apitable.datasheet("dstWUHwzTHd2YQaXEE")

    # Upload a file to the specified datasheet
    file = dst.upload_file("/Users/coco/Documents/3.jpg")

    # Update the "Attachments" field of a specified record
    record = dst.records.get(Nickname="Anan")
    record.attachment = [file]
    ```

    </TabItem>

    </Tabs>
    ````
5. The server returns the following JSON data, below the `"data"` is all upload successful attachment information:
> For the meaning of each parameter in the response, please check the [API Reference](/api/reference#operation/upload-attachments) 
> 
> ```json
>     {
>         "code": 200,
>         "success": true,
>         "data": {
>             "token": "space/2021/06/30/d336232203054effb819231a3426d40d",
>             "mimeType": "image/jpeg",
>             "size": 229426,
>             "height": 1024,
>             "width": 1792,
>             "name": "3.jpg",
>             "url": "https://s1.apitable.com/space/2021/06/30/d336232203054effb819231a3426d40d"
>         },
>         "message": "SUCCESS"
>     }
> ```
