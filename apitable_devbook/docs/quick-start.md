---
title: Quick Start
---

````mdx-code-block
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
````

This paper describes how to quickly start viewing the APITable API in 5 minutes.

## Step 1: Get API Token

API Token is the user authentication token.When sending API requests to APITAble servers, you must take `Authorization: Bearer {Your API Token}`at the head of the request to facilitate server authentication.

When authenticated successfully, the API request will have the same permissions as the user has to operate on the APITAble interface, that is, what data the user can do on the interface, and what data can be used in the request.

Get API Token as follows::

1. Sign in to [APITable](https://apitable.com/) and tap the profile of the lower left corner, enter the User Center and go to the Developer Configuration.

2. Click "+" to generate an API Token.Note: You need to bind your email when you generate it for the first time.

3. Copy API Token.

> **Note:**
> 
> - Please secure your API Token, if API Token leaks, others may tamper with data in your datasheet.
> - If the API Token is leaked, you can regenerate the Token in the Developer Configuration screen to ensure data security.

## Step 2: Calling the API interface to implement data additions and deletions

Select the programming language you are familiar with (e.g. Javascript) and make sure you need to call the [APITable API interface](introduction.md#open-api) you can choose either of the following ways to send requests to the API server.

### Method 1: Send HTTPS request directly

Example HTTPS request in some common languages using the Access API interface:

> Note: Before executing the following code, you need to replace the `{datasheetid}` and `{your API Token}` to the real datasheetId and API token.

````mdx-code-block
<Tabs
  groupId="send https requests"
  defaultValue="cURL"
  values={
    [
      { label: "cURL", value: 'cURL', },
      { label: "JavaScript", value: 'JavaScript', },
      { label: "Python", value: 'Python', },
    ]
  }
>

<TabItem value="cURL">

```bash
curl "https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {Your API Token}"
```

</TabItem>

<TabItem value="JavaScript">

```js
// Method 1: Fetch
const URL = 'https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records'
const res = await fetch(URL, {
  method: 'GET',
  headers: new Headers({
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {Your API Token}'
  })
})

//Method 2: Axios
const URL = 'https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records'
const res = await axios.get(URL, {
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {Your API Token}'
  }
});
```

</TabItem>

<TabItem value="Python">

```python
import requests

request_url = 'https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records'
headers = {"Authorization": "Bearer {Your API Token}","Content-Type":"application/json"}
response = requests.get(request_url, headers=headers)
result = response.json()
```

</TabItem>

</Tabs>
````
You can also send HTTPS requests by selecting any other language or library.
### Method 2: Use officially provided SDK
The SDK (Sofware Development Kit, Software Development Toolkit) provides a cover for network requests and authentications, handles details on many API requests and helps you quickly start to experience APITable API.
APITable SDK is officially provided on [GitHub](https://github.com/apitable/apitable-sdks).
Before using SDK, you need to execute the following commands on the terminal of the computer to install and initialize the SDK

````mdx-code-block
<Tabs
groupId="use SDK"
defaultValue="Javascript SDK"
values={
    [
    { label: "Javascript SDK", value: "Javascript SDK", },
    { label: "Python SDK", value: "Python SDK", },
    ]
}
>

<TabItem value="Javascript SDK">

1. Install the Javascript SDK by either of the following methods.

    <Tabs
      groupId="package management tools"
      defaultValue="npm"
      values={
      [
        { label: "npm", value: 'npm', },
        { label: "yarn", value: 'yarn', },
      ]
    }>

    <TabItem value="npm">

    ```bash
    # You need to install npm in advance
    npm install apitable@latest
    ```

    </TabItem>

    <TabItem value="yarn">

    ```bash
    # You need to install yarn in advance
    yarn add apitable@latest
    ```

    </TabItem>
    </Tabs>


2. Initialize the Javascript SDK.

    ```js
    import { APITable } from "apitable";
    const apitable  = new APITable({ token: "_Your_API_Token_"});
    ```

    When instantiating the SDK client you have the option to configure the following global parameters.

    | Options        | Type   | Default value                        | Description                                                                                                                                                                                                                     |
    | -------------- | ------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | token          | string |                                      | Required, representing the incoming API Token                                                                                                                                                                                   |
    | fieldKey       | string | name                                 | The key used to query and return fields.By default use `name`(field name).\n When specified as `id`, fieldId will be used as the query and return method (using `id` can avoid code failure caused by modifying the field name) |
    | requestTimeout | number | 60000                                | Request expiration time, milliseconds, default value is 6000000 (i. e. 10 seconds)                                                                                                                                              |
    | host           | string | `https://api.apitable.com/fusion/v1` | Destination server                                                                                                                                                                                                              |
    | adapter        | any    |                                      | If it needs to be used in the WeChat Miniprogram, a request adapter needs to be added, see [Using Vika JS SDK in the WeChat Miniprogram](/api/use-javascript-sdk-in-wechat-miniprogram)                                         |

</TabItem>

<TabItem value="Python SDK">

1. Install Python SDK.

    ```py
    # Python version needs to be v3.6 or above
    # Need to install pip in advance
    pip install --upgrade apitable
    ```

2. Initialize the Python SDK.

    ```py
    from apitable import Apitable
    apitable = Apitable("_Your_API_Token_")
    ```

</TabItem>

</Tabs> 
````

Once the request is determined, you can write the code, calling the corresponding APItable API interface.
