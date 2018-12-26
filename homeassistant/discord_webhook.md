# Discord webhook

```yaml
notify
  - name: discord_webhook
    platform: rest
    method: POST
    message_param_name: content
    title_param_name: username
    data:
      username: Home Assistant
    resource: "https://discordapp.com/api/webhooks/36723429/UBbENaEKpuUHOWs3wBjAiq2Ribcf74688fcn6n8748M9y0p7KD7C-YJ"
```

service: `notify.discord_webhook`

```json
{"message":"This is a test"}
```