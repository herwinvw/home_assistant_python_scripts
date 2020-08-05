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
step_pct: integer, optional
    dim/undim step size in percent (default:5)
"""
entity_id = data.get('entity_id')
event = int(data.get('event'))
on_events = data.get('on_event',[1002])
off_events = data.get('off_event',[4002])
dim_events = data.get('dim_events',[3001, 3002])
undim_events = data.get('undim_events',[2001, 2002])
step_pct = data.get('step_pct', 5)

service_data = {'entity_id': entity_id}
if event in on_events:
    hass.services.call('light', 'turn_on', service_data, False)
elif event in off_events:
    hass.services.call('light', 'turn_off', service_data, False)
elif event in dim_events:
    service_data['brightness_step_pct'] = -step_pct
    hass.services.call('light', 'turn_on', service_data, False)    
elif event in undim_events:
    service_data['brightness_step_pct'] = step_pct
    hass.services.call('light', 'turn_on', service_data, False)