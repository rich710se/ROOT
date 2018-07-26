# Check if current week is odd/even

```yaml
{% set weeknumber= (as_timestamp(now())|timestamp_custom("%W"))|int %}
{% if weeknumber is divisibleby 2 %}even{% else%}odd{% endif %}
```
