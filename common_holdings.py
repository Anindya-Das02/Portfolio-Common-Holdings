from loggers import COMPARE_FUNDS_DIR_PATH, finish, prgm_end, linespace
import os

os.chdir(COMPARE_FUNDS_DIR_PATH)
amcs =  [f for f in os.listdir('.') if os.path.isfile(f)]

if len(amcs) == 0:
    print("No AMCs file found for comparision.. please add files in 'Compare Funds' folder to compare!")
    exit(0)

print(f"Comparing following {len(amcs)} funds:")
for fund_name in amcs:
    print(f" - {fund_name}")
linespace()


holdings = []
for amc in amcs:
    with open(amc,'r') as f:
        holdings.append(set(f.readlines()))

common_companies = set.intersection(*holdings)
print(f"No of common companies: {len(common_companies)}")
counter = 1
for i in common_companies:
	print(f"[{counter}]. {i}")
	counter += 1

finish()
prgm_end()
