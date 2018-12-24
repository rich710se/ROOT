# Sync device states

```yaml
- alias: 'Share state test'
  trigger:
    - platform: state
      entity_id: 
        - switch.my_switch
        - light.my_ligths
  action:
    - service_template: "homeassistant.turn_{{ trigger.to_state.state | lower}}"
      data_template:
        entity_id: >-
          {% set entities = ["light", "switch"] %}
          {{ entities |reject("equalto", trigger.entity_id)|list }}
```

Updated by [skalavala](https://github.com/skalavala) to be simpler and scalable.
