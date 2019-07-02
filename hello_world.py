"""
Writes Hello name to notify.home_group

Parameters
----------
name : string, optional
	name to say hello to, default is 'world'	
"""
name = data.get('name', 'world')
hass.services.call('notify', 'home_group', {"message":"Hello {}".format(name)}, False)