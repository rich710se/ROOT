# Translate the day from strftime
_to norwegian in this example_

```yaml
{% set days = {
  "Mon": "Man",
  "Tue": "Tir",
  "Wed": "Ons",
  "Thu": "Tor",
  "Fri": "Fre",
  "Sat": "Lør",
  "Sun": "Søn",
} %}
{{ days[now().strftime('%a')]}}

```
