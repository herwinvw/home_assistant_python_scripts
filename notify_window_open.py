"""
Notifies notify.home_group of any open windows
Parameters
----------
group : string, optional
	group that contains the windows to notify for, default: group.windows
message: string, optional
	message template for the notification, use {windows} to list the open windows inside the message. Default: 'Windows in {windows} are open.'
"""
message = data.get('message', 'Windows in {windows} are open.')
window_group = data.get('group', 'group.windows')

entities = hass.states.get(window_group).attributes['entity_id']
open_windows = []

for entity_id in entities:
	entity = hass.states.get(entity_id)
	if entity.state == 'on':
		open_windows.append(entity.attributes['friendly_name'])

if open_windows:
	message = message.format(windows="".join(open_windows))		
	hass.services.call('notify', 'home_group', {"message":message}, False)