# ssscan 雏形
基于mitmproxy的被动扫描系统
使用redis去重
celery做异步处理，broker为redis
Mysql做持续化存储
插件形式
目前实现：1.反射型xss
          2.sqlmapapi
          3.lfi
          4.敏感信息匹配
后续：增加poc插件检测
