# APITable Langchain Toolkit

This is [Langchain](https://python.langchain.com/) toolkits allows agents to interact with APITable Fusion API, performing actions such as get spaces, get datasheets, get records, create fields and create datasheet. The tool wraps the [apitable.py](https://github.com/apitable/apitable-sdks/tree/develop/apitable.py) library. 

And it is in beta, please don't use it in production.

To use this tool, you must first set as environment variables: APITABLE_API_TOKEN

```python
os.environ["OPENAI_API_KEY"] = "xxx"
os.environ["APITABLE_API_TOKEN"] = "xxx"
```

See [example](example.ipynb).
