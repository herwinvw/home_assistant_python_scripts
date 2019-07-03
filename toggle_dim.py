"""
Flip a light from undimmed to dimmed or vice-versa

If the light was turned off, it will first flip to undimmed brightness.

Parameters
----------
entity_id : string
	light entity to toggle the dim value on
dimmed_brightness: integer, optional
	dimmed brightness of the light entity (default: 5)
undimmed_brightness
	undimmed brightness of the light entity (default: 255)
"""
entity_id = data.get('entity_id')
dimmed_brightness = data.get('dimmed_brightness', 5)
undimmed_brightness = data.get('undimmed_brightness', 255)
state = hass.states.get(entity_id)

if state.state == 'off' or state.attributes['brightness'] <= dimmed_brightness:
	brightness = undimmed_brightness
else:
	brightness = dimmed_brightness

service_data = {'entity_id': entity_id, 'brightness': brightness }
hass.services.call('light', 'turn_on', service_data, False)