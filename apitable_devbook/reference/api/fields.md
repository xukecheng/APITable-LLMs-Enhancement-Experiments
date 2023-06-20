The data structure of the fields is as follows.

| Properties | Description                                                                                                                                                                                                                                             |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| id         | <p>`string`, field ID </p> Example values: `fldsRHWJZwFcM`                                                                                                                                                                                              |
| name       | <p>`string`, field name </p> Example values: `Order number`                                                                                                                                                                                             |
| type       | <p>`string`, Field types, possible values are listed in the section [Field Types and Attributes](#field-types-and-attributes) </p> Example values: `SingleText`                                                                                         |
| editable   | <p>`boolean`, Field permissions, i.e. [column permissions](https://help.apitable.com/docs/guide/manual-field-permission), `true` for editable, `false` for read-only </p> Example values: `true`                                                        |
| property   | <p>`object`,Field attributes.Different fields have different attributes, see the section [Field Types and Attributes](#field-types-and-attributes) for details on the attributes of various fields</p> Example values: `{"defaultValue":"To be added"}` |
| isPrimary  | <p>`boolean`, Is the primary field</p> Example values: `true`                                                                                                                                                                                           |
| desc       | <p>`string`, Field descriptions, i.e. column descriptions </p> Example values: `This column is the automatic generation of the single number, do not manually modify`                                                                                   |




### Field Types and Attributes

APITable currently has the following field types.

| The type of field returned by the interface | The type of the corresponding field |
| ------------------------------------------- | ----------------------------------- |
| SingleText                                  | single-line text                    |
| Text                                        | Multi-line text                     |
| SingleSelect                                | Single choice                       |
| MultiSelect                                 | Multiple choice                     |
| Number                                      | Number                              |
| Currency                                    | Currency                            |
| Percent                                     | Percentage                          |
| DateTime                                    | Datetime                            |
| Attachment                                  | Attachment                          |
| Member                                      | Member                              |
| Checkbox                                    | Check                               |
| Rating                                      | Rating                              |
| URL                                         | Website                             |
| Phone                                       | A telephone number.                 |
| Email                                       | Email                               |
| MagicLink                                   | MagicLink                           |
| MagicLookUp                                 | MagicLookUp                         |
| Formula                                     | Intelligent formula                 |
| AutoNumber                                  | Autoincrement number                |
| CreatedTime                                 | Create Timestamp                    |
| LastModifiedTime                            | Modify Timestamp                    |
| CreatedBy                                   | Created by                          |
| LastModifiedBy                              | Updated by                          |

The following section describes the properties of each field type in detail.

When the "Get Field" interface is called, the following results are returned for each field type.

#### SingleText

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "SingleText",
  "property": {
    "defaultValue": ""
  }
}
```

| Field Properties | Data Type | Description                                                                                                 |
| ---------------- | --------- | ----------------------------------------------------------------------------------------------------------- |
| defaultValue     | string    | When creating a new record, the default value of the corresponding cell of this field, the default is empty |

#### Text

No field properties are available at this time.

#### SingleSelect

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "SingleSelect",
  "property": {
    "options": [
      {
        "id": "optpTVSGk0R2M",
        "name": "Elevit",
        "color": {
          "name": "indigo_4",
          "value": "#5586FF"
        }
      },
      {
        "id": "optqX2Bw479FG",
        "name": "OAD",
        "color": {
          "name": "blue_4",
          "value": "#55CDFF"
        }
      }
    ]
  }
}
```

| Field Properties | Data Type     | Description                   |
| ---------------- | ------------- | ----------------------------- |
| options          | object arrays | List of all available options |

Description of the parameters contained under options.

| Parameters | Data Type | Description                                                        |
| ---------- | --------- | ------------------------------------------------------------------ |
| id         | string    | option ID                                                          |
| name       | string    | option name                                                        |
| color      | object    | The color of the option, including the name and value of the color |

#### MultiSelect

The field properties are the same as the radio selection.

#### Number

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Number",
  "property": {
    "defaultValue": "2",
    "precision": 0,
    "commaStyle": ",",
    "symbol": "Square meters"
  }
}
```

| Field Properties | Data Type | Description                                                                                                                                                                                                             |
| ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| defaultValue     | string    | The default value for this field when creating a new record, default is empty.                                                                                                                                          |
| precision        | number    | Indicates the number of decimal places, i.e., the precision of the number.The values are 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places) |
| commaStyle       | string    | Thousand separator, set this property to separate thousands of digits by a comma, such as 1,000.default is empty (optional)                                                                                             | symbol |
| symbol           | string    | numeric units, displayed to the right of the number, default is null (optional)                                                                                                                                         |

#### Currency

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Currency",
  "property": {
    "defaultValue": "1000.00",
    "precision": 2,
    "symbol": "¥",
    "symbolAlign": "Default"
  }
}
```

| Field Properties | Data Type | Description                                                                                                                                                                                                                                 |
| ---------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| defaultValue     | string    | The default value for this field when creating a new record, the default is null.                                                                                                                                                           |
| precision        | number    | Indicates the number of decimal places, i.e., the precision of the number.The values are 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)                     |
| symbol           | string    | currency symbol, can be any custom character                                                                                                                                                                                                |
| symbolAlign      | string    | currency symbol (optional).The default value is `Default` (the currency unit is immediately to the left of the value), other values are `Left` (the currency unit is fixed to the left), `Right` (the currency unit is fixed to the right). |

#### Percent

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Percent",
  "property": {
    "defaultValue": "0.85",
    "precision": 1
  }
}
```

| Field Properties | Data Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| defaultValue     | string    | The default value of the cell corresponding to this field when creating a new record, the default is empty.                                                                                                                                                                                                                                                                                                                            |
| precision        | number    | Indicates the number of decimal places to convert the field value to a percentage, i.e., the percentage precision.The values are 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places).For example, if the field value is 0.22, it will be displayed as 22% if the percentage precision is 0. If the percentage precision is 1, it will be displayed as 22.0% |

#### Datetime

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "DateTime",
  "property": {
    "dateFormat": "YYYY/MM/DD hh:mm",
    "includeTime": true,
    "timeFormat": "hh:mm",
    "autoFill": true,
    "timeZone": "Asia/Hongkong",
    "includeTimeZone": true
  }
}
```

| Field Properties | Data Type     | Description                                                      |
| ---------------- | ------------- | ---------------------------------------------------------------- |
| dateFormat       | string(enum)* | YYYY/MM/DD, YYYY-MM-DD, DD/MM/YYYY, YYYY-MM, MM-DD, YYYY, MM, DD |
| includeTime      | Boolean       | Whether to display the time                                      |
| timeFormat       | string(enum)  | HH:mm, hh:mm                                                     |
| autoFill         | Boolean       | Whether to auto-fill the time when creating a new record         |
| timeZone         | String        | Time zone                                                        |
| includeTimeZone  | Boolean       | Whether to display time zone                                     |

The value of the date field returns timestamp without restricted format.The `format` information in the field property can be used for formatting, see [dayjs format](https://day.js.org/docs/en/display/format#list-of-all-available-formats) for the meaning.

_If you don't want to handle date formatting and want the returned result to be consistent with the view display, you can assign [`cellFormat`](#operation/get-records) to `string` in the interface request parameters, and all the returned content will be a string._

For available values for `timeZone` property, please refer to [List of Time Zones](https://timezonedb.com/time-zones). Example: `Asia/Shanghai`。

#### Attachment

No field properties are available at this time.

#### Member

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Member",
  "property": {
    "isMulti": true,
    "shouldSendMsg": true
  }
}
```

| Field Properties | Data Type | Description                                                                              |
| ---------------- | --------- | ---------------------------------------------------------------------------------------- |
| isMulti          | Boolean   | If or not multiple members can be selected                                               |
| shouldSendMsg    | Boolean   | Whether to send an in-site message to a member when it is mentioned in the member column |

Description of the parameters contained under options.

| Parameters | Data Type | Description                                                                                                                                                                                                      |
| ---------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | String    | The user's organizational unit id (different from the actual user id) on the current space, hereafter referred to as the member id. e. g.Bob's member id on space A is different from his member id on space B | name |
| name       | String    | member name                                                                                                                                                                                                      |
| type       | String    | member type, including `Member` (for users with physical accounts) and `Team` (for organizational units in the space, such as departments, groups, etc.)                                                       |
| avatar     | String    | URL of the member's avatar                                                                                                                                                                                       |

#### Checkbox

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Checkbox",
  "property": {
    "icon": "white_check_mark"
  }
}
```

| Field Properties | Data Type    | Description                                                   |
| ---------------- | ------------ | ------------------------------------------------------------- |
| icon             | string(enum) | Please refer to [Expression Pack Enumeration](/widget/emojis) |

#### Rating

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Rating",
  "property": {
    "icon": "star",
    "max": 5
  }
}
```

| Field Properties | Data Type    | Description                                                   |
| ---------------- | ------------ | ------------------------------------------------------------- |
| icon             | string(enum) | Please refer to [Expression Pack Enumeration](/widget/emojis) |
| max              | Number       | The maximum value of the rating, from 1-10                    |

#### URL

No field properties are available at this time.

#### Phone

No field properties are available at this time.

#### Email

No field properties are available at this time.

#### MagicLink

Two datasheets A and B are connected by a link field, and there will be an association field in A that is associated with B, and a link field in B that is associated with A.This pair of related fields is called a `brother field`.

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "MagicLink",
  "property": {
    "foreignDatasheetId": "dstgr2YN264s7CXKVs",
    "limitToViewId": "viwY4B8pmiMoi",
    "limitSingleRecord": true
  }
}
```

| Field Properties   | Data Type | Description                                                                                         |
| ------------------ | --------- | --------------------------------------------------------------------------------------------------- |
| foreignDatasheetId | String    | Related datasheet ID                                                                                |
| limitSingleRecord  | Boolean   | Whether to select only a single record                                                              |
| limitToViewId      | String    | Specifies a view of the associated datasheet, limiting the selection to the records under that view |

#### MagicLookUp

The MagicLookUp field is a field attached to a MagicLink field. It is a dynamic computed field, and the cell itself does not store any value.

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "MagicLookUp",
  "property": {
    "relatedLinkFieldId": "fldhBGpM3ylTq",
    "targetFieldId": "fldS2mgS18LE1",
    "rollupFunction": "VALUES",
    "valueType": "Array",
    "entityField": {
      "datasheetId": "dstgr2YN264s7CXKVs",
      "field": {
        "id": "fldS2mgS18LE1",
        "name": "title",
        "type": "SingleText",
        "property": {
          "defaultValue": ""
        },
        "editable": true
      }
    }
  }
}
```

| Field Properties   | Data Type | Description                                                                                                                |
| ------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------- |
| relatedLinkFieldId | String    | The associated field ID of the referenced current datasheet                                                                |
| targetFieldId      | String    | the field ID of the queried field in the associated datasheet                                                              |
| hasError           | Boolean   | When a lookup dependent associated field is deleted or converted, the referenced value may not be retrieved properly       |
| entityField        | Object    | The entity fields are finally referenced, excluding MagicLoopUp fields.If an error exists, the entity field may not exist. |
| rollupFunction     | String    | aggregate function                                                                                                         |
| valueType          | String    | Return value type, including `String`, `Boolean`, `Number`, `DateTime`, `Array`                                            |
| format             | Object    | Returns the result of a number or date formatting operation when the return value is of type `Number` or `DateTime`        |

- Description of the rollupFunction values refer to [Lookup Product Manual](https://help.apitable.com/docs/guide/manual-field-lookup) for the meaning of the parameters.

  | Function Name | Return Value Type | Description            |
  | ------------- | ----------------- | ---------------------- |
  | VALUES        | array             | Original values        |
  | AVERAGE       | number            | average                |
  | COUNT         | number            | non-null count         |
  | COUNTA        | number            | non-null value count   |
  | COUNTALL      | number            | full count             |
  | SUM           | number            | Total                  |
  | MIN           | number/datetime   | minimum                |
  | MAX           | number/datetime   | maximum                |
  | AND           | boolean           | and operation          |
  | OR            | boolean           | or operation           |
  | XOR           | boolean           | eXclusive OR operation |
  | CONCATENATE   | string            | concatenate to text    |
  | ARRAYJOIN     | string            | comma-join             |
  | ARRAYUNIQUE   | array             | Deduplication          |
  | ARRAYCOMPACT  | array             | filter all null values |

- Description of the parameters contained under entityField.

  | Parameters  | Data Type | Description                                                                                                                                                     |
  | ----------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | datasheetId | String    | the datasheet ID of the entity field                                                                                                                            |
  | field       | Object    | A `Field` object other than LookUp, a MagicLookUp can refer to a field of a MagicLookUp type from another datasheet, but ultimately an entity field will exist. |

  > Note: If you use this field feature in your application, you will need to handle exceptions when a reference error is detected for the field.

- The parameters included under format are described below.

  | Parameters | Data Type | Description                                                 |
  | ---------- | --------- | ----------------------------------------------------------- |
  | type       | String    | formatting type `DateTime`, `Number`, `Percent`, `Currency` |
  | format     | Object    | The specific format of the different formatting types       |

  **Formatted as date.**

  | Parameters      | Data Type | Description                        |
  | --------------- | --------- | ---------------------------------- |
  | dateFormat      | String    | Date format, e.g. `YYYY/MM/DD`     |
  | timeFormat      | String    | Time format, e.g. `hh:mm`, `HH:mm` |
  | includeTime     | Boolean   | Whether to display the time        |
  | timeZone        | String    | Time zone                          |
  | includeTimeZone | Boolean   | Whether to display time zone       |

  **Formatted as a number or percentage:**

  | Parameters | Data Type | Description                               |
  | ---------- | --------- | ----------------------------------------- |
  | precision  | Number    | numeric precision or percentage precision |

  **Formatted as currency:**

  | Parameters | Data Type | Description     |
  | ---------- | --------- | --------------- |
  | precision  | Number    | Precision       |
  | symbol     | String    | currency symbol |

#### Formula

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "Formula",
  "property": {
    "expression": "",
    "valueType": "String",
    "hasError": false
  }
}
```

| Field Properties | Data Type     | Description                                                                                                                      |
| ---------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| expression       | string*       | formula expression                                                                                                               |
| valueType        | string(enum)* | Return value type, including `String`, `Boolean`, `Number`, `DateTime`, `Array`                                                  |
| hasError         | boolean       | The calculated value may not be retrieved properly when the relevant field dependent on the formula is deleted or converted.     |
| format           | object        | When the return value is of type `Number` or `DateTime`, it returns a number or date formatted in the same format as the lookup. |

Same as magiclookup, exceptions need to be handled when errors are encountered.

#### AutoNumber

DescriptionNo field properties are available at this time.

#### CreatedTime

Same as DateTime.

#### LastModifiedTime

Same as DateTime.

#### CreatedBy

The member id is at the space level and the creator id is at the account level.

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "CreatedBy",
  "property": {
    "options": [
      {
        "id": "e9cbc839fd1b49be85b1f7b0977047e2",
        "name": "Coco",
        "avatar": "https://s1.apitable.com/default/avatar004.jpg"
      }
    ]
  }
}
```

| Field Properties | Data Type | Description                                                   |
| ---------------- | --------- | ------------------------------------------------------------- |
| options          | option[]  | Members whose fields have been selected by the current member |

Description of the parameters contained under options.

| Parameters | Data Type | Description        |
| ---------- | --------- | ------------------ |
| id         | string*   | user id            |
| name       | string*   | user nickname      |
| avatar     | string*   | URL of user avatar |

#### LastModifiedBy

Return a sample fragment of the result (containing only field types and attributes).

```json
{
  "type": "LastModifiedBy",
  "property": {
    "options": [
      {
        "id": "e9cbc839fd1b49be85b1f7b0977047e2",
        "name": "Coco",
        "avatar": "https://s1.apitable.com/default/avatar004.jpg"
      }
    ]
  }
}
```

| Field Properties | Data Type | Description                |
| ---------------- | --------- | -------------------------- |
| options          | option[]  | Current field stored users |

Description of the parameters contained under options.

| Parameters | Data Type | Description        |
| ---------- | --------- | ------------------ |
| id         | string*   | user id            |
| name       | string*   | user nickname      |
| avatar     | string*   | URL of user avatar |
