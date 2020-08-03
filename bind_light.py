"""
Controls a light with a dimmer.

Parameters
----------
entity_id : string
	light entity to control
event: integer
    button event
on_event: integer, optional
	on_button event (default: 1002)
off_event: integer, optional
    off_button event (default: 4002)
dim_event: integer, optional
    dim_button event (default: 3001)
undim_event: integer, optional
    undim_button event (default: 2001)
"""
entity_id = data.get('entity_id')
event = int(data.get('event'))
on_event = data.get('on_event',1002)
off_event = data.get('off_event',4002)
dim_event = data.get('dim_event',3001)
undim_event = data.get('undim_event',2001)
state = hass.states.get(entity_id)

service_data = {'entity_id': entity_id}
if event == on_event:
    hass.services.call('light', 'turn_on', service_data, False)
elif event == off_event:
    hass.services.call('light', 'turn_off', service_data, False)
elif event == dim_event and state.state == 'on':
    service_data['brightness_step_pct'] = -5
    hass.services.call('light', 'turn_on', service_data, False)    
elif event == undim_event and state.state == 'on':
    service_data['brightness_step_pct'] = 5
    hass.services.call('light', 'turn_on', service_data, False)