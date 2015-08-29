
def general_string_filter(value_to_filter):
    def specific_string_filter(data_dict):
        #print('Data  = {0}'.format(data_dict))
        #print('Value to filter = {0}'.format(value_to_filter))
        #print('Value of id = {0}'.format(data_dict['id']))
        # I had to put in all these print statements as I had 
        # had used "lower" instead of "lower()" on the left.
        # Ah!  The perils of dynamic types and attributes.
        if data_dict['id'].lower() == value_to_filter.lower():
            return True
        else:
            return False
    return specific_string_filter

print(general_string_filter)
sameer_filter = general_string_filter('Sameer')
print(sameer_filter)
arnab_filter = general_string_filter('Arnab')
print(arnab_filter)
umesh_filter = general_string_filter('Umesh')
print(umesh_filter)

data = [{'id': 'Arnab'}, {'id': 'Sameer'}, {'id': 'Umesh'}, {'id': 'Vinod'}]

for item in data:
    print(15*'=')
    print(item)
    print(sameer_filter(item))
    print(arnab_filter(item))
    print(umesh_filter(item))
    