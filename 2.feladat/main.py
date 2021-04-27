import sys
import pandas
from pprint import pprint
import re

file_path = sys.argv[1]
email_regex ="^[a-záéúőóüöíA-ZÁÉÚŐÓÜÖÍ\.\&\#\!\+\-\$]+@+[a-zA-Z]+\.[a-z]"
name_regex = "^[a-záéúőóüöíA-ZÁÉÚŐÓÜÖÍ]+\s[a-záéúőóüöíA-ZÁÉÚŐÓÜÖÍ]+\Z"
address_regex = "^\d{4}\s[a-záéúőóüöíA-ZÁÉÚŐÓÜÖÍ]+\,\s[\sa-záéúőóüöíA-ZÁÉÚŐÓÜÖÍ\.\d\/]+\."
phone_regex = "^(\d){2}\s+(\d){6,7}\Z"

def is_valid(dict:dict):
    bad_index = []
    if not re.search(name_regex,dict["NAME"]):
        bad_index.append("0")
    if not re.search(address_regex,dict["ADDRESS"]):
        bad_index.append("1")
    if  not re.search(phone_regex,dict["PHONE"]):
        bad_index.append("2")
    if not re.search(email_regex,dict["EMAIL"]):
        bad_index.append("3")

    if bad_index != []:
        dict["INDEX"] = ", ".join(bad_index)
        return False

contacts_bad = []
contacts_good = []
data = pandas.read_csv(file_path, sep=";")
data_dict = data.to_dict(orient="records")
pprint(data_dict)
for i in data_dict:
    if is_valid(i) == False:
        contacts_bad.append(i)
    else:
        contacts_good.append(i)

print(contacts_bad)
bad_contact_dataframe = pandas.DataFrame(contacts_bad)
bad_contact_dataframe.to_csv("contacts_bad.csv", index=False, sep=";")

good_contact_dataframe = pandas.DataFrame(contacts_good)
good_contact_dataframe.to_csv("contracts_good.csv", index=False, sep=";")