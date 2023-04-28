# FluentQA Helper

Use as less code as you can to capture API request to database for automation code generation.
A simple UI to do the proxy setting and start capturing API Request.

## Commandline Features:

- Use mitmproxy to capture API request:
```shell
poetry run qacli capture start --name="scenario_name"
```
![img.png](img.png)

- Capture API Request Based on Configuration: configs/settings.toml

captured URL setting: all request to www.baidu.com and www.bing.com will save to database
```shell
mitm = { recorded_url = "https://www.baidu.com,https://www.bing.com" }
```

- all api request and response in database, table fields:

```python
class ApiMonitorRecord(SQLModel, table=True):
    __tablename__ = "api_monitor_record"

    id: Optional[int] = Field(default=None, primary_key=True)
    app: Optional[str] = None
    service: Optional[str] = None
    api: Optional[str] = None
    path: Optional[str] = None
    request_url: Optional[str] = None
    method: Optional[str] = None
    request_headers: Optional[str] = None
    request_body: Optional[str] = None
    response_headers: Optional[str] = None
    status_code: int
    response_body: Optional[str] = None
    scenario_name: Optional[str] = None

```

- turn on/off proxy setting in MAC

```shell
 poetry run qacli mac-proxy --help
                                                                                                                                                         
 Usage: qacli mac-proxy [OPTIONS] COMMAND [ARGS]...                                                                                                      
                                                                                                                                                         
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ off                  disable api capture proxy                                                                                                        │
│ on                   enable api capture proxy 
```

## UI Feature

```shell
poetry run qaui
```
![img.png](img.png)
- input capture name: any name your want
- start to capture API request
- Query Database to get all the request you want
```sql
select * from api_monitor_record where scenario_name=<your_record_name>
```
- export or do some changes for your automation testing


## To Do

- [] Code Generation
- [] ......

## References

- [gradio]
- [todo-cli-app]( https://github.com/tddschn/todo-cli-tddschn.git)