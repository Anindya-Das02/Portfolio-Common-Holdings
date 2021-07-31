def prgm_end():
	print("--end program")

def finish():
	print("--finish")

def reached(point:int=None):
	if point is not None:
		print(f">> reached pt #{point}")
		return 
	print(">> reached")

def linespace():
	print()

HOLDINGS_TABLE_NOT_FOUND = "could not find holdings table!"
EMPTY_STRING = ""
HOLDINGS_TABLE_ID = "equityCompleteHoldingTable"
FILE_PATH = "AMC COMPANY HOLDINGS"
FUND_TITLE_CLASS = "page_heading navdetails_heading"
TARGET_BLANK = "_blank"
LXML_PARSER = "lxml"
COMPARE_FUNDS_DIR_PATH = "Compare Funds"
AMC_HOLDING_DIR_PATH = "AMC COMPANY HOLDINGS"
NO_FILES_IN_DIR_MSG = f"No files found in directory! Please add files in '{FILE_PATH}' to compare!"