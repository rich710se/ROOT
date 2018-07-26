# Trigger stuff with curl

## Trigger automation:

```bash
curl -v -X POST -H "x-ha-access: YOURAPIPASSWORD" -H "Content-Type: application/json" -d '{"entity_id": "automation.AUTOMATIONNAME"}' https://example.duckdns.org:8123/api/services/automation/trigger
```

## Toggle switch:

```bash
curl -v -X POST -H "x-ha-access: xxxxxxxxxx-H "Content-Type: application/json" -d '{"entity_i
```
