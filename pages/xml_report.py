import xml.etree.ElementTree as ET
from lxml import etree

'''Pass XML File'''
mytree = ET.parse('/Users/wipro/Documents/SimRun_Execution/Test_Runner/SIMRUN-SIMRUN-V11-Release-V11_RETAIL_BATCH_01-0.xml')

'''Get Root Variable'''

myroot = mytree.getroot()

test_results = myroot.attrib

'''Get the Summary of Total Tests and Failed Tests'''

result = len(myroot.getchildren())

print(result)

def get_execution_summary():

    if 'tests' in test_results:
        total_cases = int(test_results.get('tests'))
        print('total_cases: ',total_cases)

    if 'failures' in test_results:
        failures = int(test_results.get('failures'))
        passed = total_cases-failures
        print('total_passed_cases: ',passed)
        print('total_failures: ',failures)

def detailed_execution_result():
    pass





print(myroot[2][0].text)

print('------0------')

print(type(test_results))

print(test_results)

print('------1------')

print(myroot[0].attrib)
print(myroot[0].tag)
print(myroot[13].attrib)

print('-------2-----')

for x in myroot[1:15]:
    print(x.tag,x.attrib)

print('------3------')
