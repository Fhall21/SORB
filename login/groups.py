
from accounts.models import GroupRecord
# a list of the possible groups they can choose from 
def list_maker(abbr, name):
	list_group = (str(abbr), str(name))
	return list_group
class Groups:
	def Scout_Groups():
		
		scout_group_list = (
		(None, 'Click here to select the group'),
		('BC', 'Brisbane Central Scout'),
		('Admin', 'N/A'),
		
		)
		return scout_group_list

	def Groups_finder():
		list_format_group = [(None, 'Click here to select the group')]
		data_set = GroupRecord.objects.all()
		for i in data_set:
			group_name = i.group
			group_abbr = i.abbreviation
			list_format_group.append(list_maker(group_abbr, group_name))
		tuple_format_group = tuple(list_format_group)
		return tuple_format_group
# To-Do: Link this with a file which automatically updates based on incoming emails
'''
def list_maker(abbr, name):
	list_group = (str(abbr), str(name))
	return list_group

def Scout_Group():
	list_format_group = []
	data_set = GroupRecord.objects.all()
	for i in data_set:
		group_name = i.group
		group_abbr = i.abbreviation
		list_format_group.append(list_maker(group_abbr, group_name))
	tuple_format_group = tuple(list_format_group)
'''