# A one-liner to get all entities of a group with a given state!

```yaml
{{ dict((states|selectattr('entity_id', 'in', state_attr('group.all_devices', 'entity_id'))|list)|groupby('state'))['home']|map(attribute='name')|list|join(', ') }}
```
