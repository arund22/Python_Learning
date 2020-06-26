import xml.etree.ElementTree as ET

data = ET.parse('/Users/wipro/Documents/SimRun_Execution/Test_Runner/SIMRUN-SIMRUN-V11-Release-V11_RETAIL_BATCH_01-0.xml')

myroot = ET.fromstringlist(data)

print(myroot.tag)