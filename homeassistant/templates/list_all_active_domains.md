# List all active domains

```yaml
{{ states | map(attribute='domain') |list | unique | list}}
```

From: https://github.com/skalavala/smarthome/tree/master/jinja_helpers
