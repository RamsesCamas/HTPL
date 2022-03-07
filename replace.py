import re
text = '<var type="integer" name="my_int">  25 </var>'

expected_text = '<var type="integer" name="my_int">25 </var>'

print(type(re.sub('> +(?=[\w]*)','>',text)))