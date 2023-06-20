---
title: Get Embedded Links
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

:::tip

The **[Embedded Links](https://help.apitable.com/docs/guide/embedding-with-embedded-link)** are only available for the spaces on the **[paid Pro or higher plan](https://apitable.com/pricing/)** in APITable Cloud as well as **[Enterprise](https://apitable.com/pricing/)** self-hosted edition.  

Node types that support creating embedded links are:

- [Datasheet](introduction.md#datasheetid)
- [Dashboard](introduction.md#datasheetid)
- [Form](introduction.md#formid)

:::

## Example

Here is an example of calling [API](/api/reference#operation/get-embedlinks) to check and get all the embedded links of a datasheet.

If you'd like to get all embedded links about a specified datasheet in the space, you can follow below steps:

1. Obtain your API token. ([how to](quick-start#get-api-token))

2. Obtain the spaceId. ([how to](/api/introduction#spaceid))

3. Obtain the datasheetId. ([how to](introduction.md#datasheetid))

4. Open your system terminal, copy and paste the following code on it and make a request to APITable server (here the example space ID is `spcjXzqVrjaP3`, and the datasheetId is `dstWUHwzTHd2YQaXEE`)

    ````mdx-code-block
    <Tabs
    groupId="get embedded links"
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
   curl -X GET \
   "https://api.apitable.cn/fusion/v1/spaces/spcjXzqVrjaP3/nodes/dstWUHwzTHd2YQaXEE/embedlinks" \
   -H "Authorization: Bearer {Your API Token}" \
   -H "Content-Type: application/json"
   ```

   </TabItem>
   
   <TabItem value="Javascript SDK">

   > Note: Need to [Download and initialize Javascript SDK](/api/quick-start#official-sdk) first, and then execute the following command.

   ```js
   import { APITable } from 'apitable';

   const apitable = new APITable({
      token: 'Your API Token',
    });
   
   try {
     const res = await apitable.space('spcjXzqVrjaP3').datasheet('dstWUHwzTHd2YQaXEE').getEmbedLinks();
     if (res.success) {
       const embedsLinks = res.data || []
     }
   } catch (error) {
     // TODO: handle error
   }
   ```

   </TabItem>
   
   <TabItem value="Python SDK">

    > Note: You need to [download and initialize the Python SDK](/api/quick-start#official-sdk) first, and then execute the following command.

    ```py
    from apitable import Apitable

    apitable = Apitable("Your API Token")
    
    try:
        embedLinks = apitable.space('spcjXzqVrjaP3').datasheet('dstWUHwzTHd2YQaXEE').get_embed_links()
        print(embedLinks)
        print(len(embedLinks))
    except Exception:
        # handle error
        pass

    ```

    </TabItem> 

   </Tabs>
    ````

5. The server will return the following JSON object, and the information of the embedded link will be displayed in `data` property:

    ```json
    {
        "code": 200,
        "success": true,
        "data": [{
            "linkId": "embb90a52cfc02a4f83",
            "url": "https://apitable.com/embed/embb90a52cfc02a4f83",
            "payload": {
                "primarySideBar": {
                    "collapsed": false
                },
                "viewControl": {
                    "tabBar": false,
                    "toolBar": {
                        "basicTools": false,
                        "widgetBtn": false,
                        "apiBtn": false,
                        "formBtn": false,
                        "historyBtn": false,
                        "robotBtn": false,
                        "addWidgetBtn": false,
                        "fullScreenBtn": false,
                        "formSettingBtn": false
                    },
                    "collapsed": false,
                    "collaboratorStatusBar": true,
                    "nodeInfoBar": false
                },
                "bannerLogo": true,
                "permissionType": "readOnly"
            },
            "theme": "light"
        }],
        "message": "SUCCESS"
    }
    ```

    :::tip

    For the meaning of each parameter in the response result above, please check the [API Reference](/api/reference#operation/get-embedlinks).

    :::
