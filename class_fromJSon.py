from abc import ABCMeta, abstractmethod
import json

class Software(object):
    """A Abstract Base Class to generic softwares.
    """

    __metaclass__ = ABCMeta

    base_price = 0
    company = ""

    def __init__(self, name, version, owner):
        self.name = name
        self.version = version
        self.owner = owner

    def sale_price(self):
        """Return the sale price for this software (if commercial) as a float amount."""
        return 2500.0

    @abstractmethod
    def software_type(self):
        """Return a string representing the type of software this is: free, commercial, freeware, open."""
        pass
##################################### Child class derived from: Class Software 
class FreeSoftware(Software):
    """A child class derived from Software (parent class)."""

    base_price = 0
    company = "Non-company; a group of people."

    def software_type(self):
        return 'Free Software'
 

################################################ 
with open('json_distros.json', 'r') as f:
    distros_dict = json.load(f)

iCount=0
for distro in distros_dict:
    print(distro['Name'])
    if (distro['Name']=='Fedora'):
        iCount+=1

print("\n\n##### iCount = %d\n" % iCount)

print("\nFull Dictionary: ", distros_dict)

software1 = FreeSoftware(distro['Name'],distro['Version'],distro['Owner'])
print("\n\n##### Class atributes -  Price:", software1.base_price, "Company: ", software1.company)
print("\n\n##### Instance atributes - ", "Name:", software1.name, "V.", software1.version, "Owner:", software1.owner)
