> **Reminder:**
> 
> The current API is in beta, we may add new interface return value properties, but will not remove properties that already exist.If the API does not return the data you need, feel free to feedback to us.

This reference manual is intended to help you gain a comprehensive understanding of the APITable API.

> **Recommendation:**
> 
> If you haven't learned about the APITable API before, it is recommended that you start with [APITable API Introduction](/api/introduction).

The navigation area on the left side of this page provides detailed information about each API interface (including records, fields, views, attachments, spaces, and working directories).

The code area on the right of this page allows you to find sample requests and sample responses for each API interface, making it easy to copy the code you need directly.

## Introduction

The base URL for the APITable API request is `https://api.apitable.com`.

> Note: https requests must be used, not http requests.

The APITable API follows the RESTful convention as much as possible, i.e. data is added, deleted, and checked via `GET`, `POST`, `PATCH`, and `DELETE` requests to the space and APITable resources.

The request and response bodies are encoded in JSON format.

The parameter names in JSON use camel naming (e.g. viewId) and are case sensitive.

## Authentication

### Way 1: By API token

API Token is the user authentication token.When you send an API request to the APITable server, you must include `Authorization: Bearer {Your API Token}` in the request header to facilitate the server's authentication of the user's identity.

After successful authentication, this API request will have the same privileges as the user's operations in the APITable interface, i.e. whatever data the user can operate on the interface, this request can also operate on it.

Take the following cURL request as an example.

```bash
curl "https://api.apitable.com/fusion/v1/datasheets/{datasheetId}/records" \
  -H "Authorization: Bearer {Your API Token}" \
```

Its request header includes.

| Name          | Data Type       | Required | Format of Value           | Example Value                    |
| ------------- | --------------- | -------- | ------------------------- | -------------------------------- |
| Authorization | String (string) | Yes      | `Bearer {Your API Token}` | `Bearer uskYtInkHozfsMikhh0yfoS` |

For specific authentication operations, please refer to [Quick Start](/api/quick-start)

### Way 2: OAuth2 (WIP)

## Restrictions

When sending API requests, you need to be aware of several restrictions: frequency restrictions, interface restrictions, usage restrictions.

### Frequency limits

The frequency of API requests to the same table from the same user is limited to `5 requests/second`.

If the request frequency exceeds the limit, an error "Operation too frequent" will be displayed (error status code 429).

### API limits

- Get records interface: Get up to 1000 rows of records at a time.
<br/>
    For example, if you want to fetch 10000 rows of records in bulk, you need to call the Get Records interface at least 10 times.
<br/>
<br/>
- Create records interface: Create up to 10 rows of records at a time.
<br/>
    For example, if you want to create 1000 rows of records in a batch, you need to call the Create Record interface at least 100 times.
<br/>
<br/>
- Update records interface: update up to 10 rows of records at a time.
<br/>
    For example, if you want to update 1000 rows of records in a batch, you need to call the Update Record interface at least 100 times.
<br/>
<br/>
- Delete records interface: Delete up to 10 rows of records at a time.
<br/>
    For example, if you want to delete 1000 rows of records in a batch, you need to call the Delete Record interface at least 100 times.
<br/>
<br/>
- Upload attachments interface: only 1 attachment can be uploaded at a time.
    If you need to upload multiple files, you need to call this interface repeatedly.

### Usage limits

There are two types of usage limits: one is the limit of API usage; the other is the limit of space resource usage, for details, please refer to [pring page](https://apitable.com/pricing).

The maximum capacity of uploading attachments to a single space is 1 GB.

## Status Codes

Each time you send an API request, the application returns a business status code and a corresponding message.

If the request fails, you can troubleshoot it based on the status code and error message returned.

| **HTTP Status Code** | **Response Message**                                      | **Business Status Code** | Description                                                                                                                                                          |
| -------------------- | --------------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200                  | SUCCESS                                                   | 200                      | `GET`, `PATCH`, `DELETE` requests work and return results as expected                                                                                                |
| 201                  | SUCCESS                                                   | 200                      | `POST` request works and returns results as expected                                                                                                                 |
| 200                  | Cannot find the specified datasheet                       | 301                      | Possible scenarios: <br />1) The datasheet may have been deleted<br />2) The user cannot find the datasheet in their own space list                                  |
| 200                  | Failed to upload attachment                               | 426                      | Possible scenarios: <br />① Attachments exceed the 1 GB size limit<br />② The space has reached its maximum attachment capacity                                      |
| 200                  | The number of uploaded attachments exceeds the limit      | 428                      | Upload attachments can only upload one per call, beyond this error will be reported                                                                                  |
| 200                  | Operation without node permission                         | 602                      | Users do not have access rights to the specified datasheet (e.g., manageable, editable, or read-only)                                                                |
| 200                  | (Refer to the specific error message)                     | 400                      | Parameter exception, data verification exception                                                                                                                     |
| 401                  | Authentication failure                                    | 401                      | Possible scenarios: <br />① API Token is not passed in the request header <br />② API Token is incorrect                                                             |
| 403                  | Prohibit access                                           | 403                      | Possible scenarios:<br /> ① The number of API calls has exceeded the limit<br /> ② Unable to get the API usage quota for the space, please try again later           |
| 404                  | Interface does not exist                                  | 404                      | Please check if the request address is correct                                                                                                                       |
| 429                  | Operate too often                                         | 429                      | The maximum request frequency for the same table by the same user is 5 times/second                                                                                  |
| 500                  | SERVER_ERROR (code)                                       | 500                      | Unhandled exceptions for internal services                                                                                                                           |
| 200                  | You have exceeded the "Public Beta" limit of 50,000 lines | 304                      | The number of rows in the table has reached the maximum number of rows in a single table, please replace the number of tables as soon as possible to avoid data loss |
