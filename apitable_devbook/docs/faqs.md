---
title: FAQ
---

## API related issues

### What should I do if I want to listen to data changes in a datasheet?

Currently webhook is not supported, you can poll the data to check if the data has changed.Stay tuned for subsequent automation features.

### Are there more use cases for the filterByFormula query condition in the Get Records interface?

| Demand                                             | Scenes                                                                   | Formula                           | Complete Search                                                                                                                                                                                                           |
| -------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Precise search for records that match the criteria | Search for records with a value equal to "Title 1" in the "Title" column | `{title}="Title 1"`               | `https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records?filterByFormula={Title}="Title 1"'`（`{Title}="Title 1"` need to use encodeURIComponent() function for transcoding first)                             |
| Fuzzy search for records that match the criteria   | Search for records whose value in the "Title" column contains "Title 1"  | `find("Title 1", {Title}) > 0` | `https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records?filterByFormula=find("Title 1", {Title}) > 0'`（`find("Title 1", {Title}) > 0` need to use encodeURIComponent() function for transcoding first) |

### What is the meaning of "unitId" in the Contacts API?

If we regard a space as a company in the real world, then teams can be seen as departments within the company. Therefore, you can create multiple teams within the space.

The Contacts of a space are composed of several teams and members. ([Learn more about Team management](https://help.apitable.com/docs/guide/manual-team-management))
- Each team can have multiple members.
- Members can also belong to multiple teams.

Roles, on the other hand, are not part of the Contacts. Each role can be associated with multiple members and teams. ([Learn more about Role management](https://help.apitable.com/docs/guide/role))

There is a unique ID called "unitId" for each member, team, and role.

You can use this "unitId" to get, update, or delete the specified member, team, or role. 

For more details, please refer to the [API documentation](/api/contacts).

## SDK related issues

### Is an official SDK currently available?

APITable SDK is officially provided on \[GitHub\](https://github.com/apitable/apitable-sdks).

### How to use the SDK?

1. [Installing and initializing the SDK](/api/quick-start#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9A%E4%BD%BF%E7%94%A8%E5%AE%98%E6%96%B9%E6%8F%90%E4%BE%9B%E7%9A%84-sdk)
2. Use the SDK to call the appropriate API interface (see the guide documentation for each interface, such as [getting records](/api/get-records))

### How to use SDK in WeChat Mini Program?

It can be used, but uploading attachments is not supported for the time being. Refer [to Using Javascript SDK in WeChat Mini Programs](/api/use-javascript-sdk-in-wechat-miniprogram) .

### How can I use the Pandas library to view and analyze the recordsets returned by the Python SDK?

The result of `records = datasheet.records.all()` returned is a recordset, and each record in the recordset is an object rather than a JSON format, so you cannot use `pandas.DataFrame(records)` to display the result directly.

You can iterate through each record and print out the data separately:.

```py
records = datasheet.records.all()
for record in records:
    print(record.json())
```

Or you can continue to use Pandas by converting each record in the recordset to JSON format.

```py
records = datasheet.records.all()
json_records = [record.json() for record in records]
pandas.DataFrame(json_records)
```
