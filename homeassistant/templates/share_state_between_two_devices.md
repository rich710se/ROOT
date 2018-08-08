#Sync device states

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
        entity_id: "{{ 'light.my_ligths switch.my_switch' | replace(trigger.entity_id, '') }}"
```
