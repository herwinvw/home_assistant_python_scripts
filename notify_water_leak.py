"""
Notifies notify.home_group of any water leaks
Parameters
----------
group : string, optional
	group that contains waterleak sensors, default: group.water_leak
"""
waterleak_group = data.get('group', 'group.water_leak')
entities = hass.states.get(waterleak_group).attributes['entity_id'];
for entity_id in entities:
	entity = hass.states.get(entity_id)
	if entity.state == 'on':
		hass.services.call('notify', 'home_group', {"message":"Waterleak: {}".format(entity.attributes['friendly_name'])}, False)