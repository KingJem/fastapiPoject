

##  tortoise-orm 中使用  aerich


初始化 之后会多出来一个 `[migrations](migrations)` 文件夹
```shell
aerich init -t settings.settings.TORTOISE_ORM

Success create migrate location ./migrations
Success write config to pyproject.toml

 ```
根据模型生成一个sql 
```shell

aerich init-db
Success create app migrate location migrations/models
Success generate schema for app "models"

```

更新数据库

```shell


```
