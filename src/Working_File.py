my_list = [1,2,3]

my_file = open("/Users/wipro/Desktop/Material/wwf.txt","w",)

for item in my_list:
    my_file.write (str(item)+"\n")

my_file.close()

my_file = open("/Users/wipro/Documents/SimRun_Execution/Test_Runner/SIMRUN-SIMRUN-V11-Release-GS2_CAS_BATCH1-0.xml","r",)

print(my_file.read())

my_file.close()

my_file1 = open("/Users/wipro/Documents/SimRun_Execution/Test_Runner/SIMRUN-SIMRUN-V11-Release-GS2_CAS_BATCH1-0.xml","r",)

print(my_file1.readline())

my_file1.close()

