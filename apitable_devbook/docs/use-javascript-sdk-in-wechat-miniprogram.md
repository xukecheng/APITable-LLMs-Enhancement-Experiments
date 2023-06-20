---
title: Using Javascript SDK in WeChat Mini Programs
---

When you use Javascript SDK in WeChat Mini Programs, you will usually encounter an error of ` adapter is not a function `:

```shell
Error occurred in the request: {success: false, code: 400, message: "adapter is not a function"}
```

This is because JS SDK uses ` axios ` as the network request library. In WeChat Mini Programs's environment, requests need to use ` wx.request `, so SDK cannot be used directly in WeChat Mini Programs.

However, axios provides the adapter interface, and [ axios-miniprogram-adapter ](https://github.com/bigmeow/axios-miniprogram-adapter) is axios's request adapter in Mini Program, which makes SDK work properly.

## Install axios-miniprogram-adapter

```shell
yarn add axios-miniprogram-adapter
```

## Import Adapter {#adapter}

When initializing the APITable instance, specify the `adapter` as the imported `axios-miniprogram-adapter` :

```js
import mpAdapter from 'axios-miniprogram-adapter';
import { APITable } from "apitable";

const apitable = new APITable({
  token: 'your_api_token',
  adapter: mpAdapter,
});

apitable.datasheet('dstxJZ2xZXJnXScfni').records.query().then(resp => {
  console.log(resp.data?.records)
})
```

## Reference Code

The following is the basic code of Mini Program generated using the taro framework. After the program is loaded, you can see the console prints out the recorded data.

```jsx
import { Component } from 'react'
import { View, Text, Button } from '@tarojs/components'
import APITable from 'apitable';
import Taro from '@tarojs/taro';
import mpAdapter from 'axios-miniprogram-adapter';
import './index.less';


export default class Index extends Component {

  componentWillMount() { }

  componentDidMount() {
    const apitable = new APITable({
      token: 'your_api_token',
      adapter: mpAdapter,
    });
    apitable.datasheet('dstxJZ2xZXJnXScxxx').records.query().then(resp => {
      console.log(resp.data?.records)
    })
  }

  componentWillUnmount() { }

  componentDidShow() { }

  componentDidHide() { }
  render() {
    return (
      <View className='index'>
        <Text>Hello APITable!</Text>
      </View>
    )
  }
}
```

## How do I upload the attachment?

The FormData object is not available because of WeChat Mini Programs's restrictions.In order to ensure that SDK is not coupled with non-standard platforms, uploading attachments in Mini Program is not supported.

You can refer to [the solutions from the community](https://developers.weixin.qq.com/community/develop/article/doc/0000cc0e5bc5d093c6f8be17254c13) and encapsulate the request implementation by yourself.
