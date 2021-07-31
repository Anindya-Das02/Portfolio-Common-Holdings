import os
from loggers import AMC_HOLDING_DIR_PATH, linespace, prgm_end, finish, NO_FILES_IN_DIR_MSG

dir_path = f"./{AMC_HOLDING_DIR_PATH}"

fund_files = os.listdir(dir_path)

# incase of empty folder
if len(fund_files) == 0:
	print(NO_FILES_IN_DIR_MSG)
	exit(0)

print(f"Comparing {len(fund_files)} AMCs")

company_list = []
amc_details = {}
for c_name in fund_files:
	f_path = f"{AMC_HOLDING_DIR_PATH}/{c_name}"
	with open(f_path,'r') as fund_name:
		c_list = [i for i in fund_name.readlines()]
		amc_details[c_name] = c_list
		company_list.append(set(c_list))

unique_company_list = set.union(*company_list)
print(f"No. of Unique Companies : {len(unique_company_list)}")

linespace()

result = { i : [] for i in unique_company_list } # str : []

for company_name in unique_company_list:
	for amc_name in amc_details.keys():
		if company_name in amc_details[amc_name]:
			result[company_name].append(amc_name)

counter = 1
for cname in sorted(result.keys(),key=str.casefold):
	print(f"[{counter}]. {cname}")
	for amcs in result[cname]:
		print(f"\t- {amcs}")
	counter += 1
	linespace()
		
prgm_end()
finish()