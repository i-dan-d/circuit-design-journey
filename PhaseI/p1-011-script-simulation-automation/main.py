import argparse
def check_result(logfile):
	with open(logfile) as f:
		lines = f.readlines()
	total = []
	passed = []
	failed_lines = [[]]
	smlt = -1
	for line in lines:
		if "PASS" in line:
			total[smlt][0] += 1
			passed[smlt][0] += 1
		elif "FAIL" in line:
			total[smlt][0] += 1
			failed_lines[smlt].append(line)
		elif "run" in line:
			if smlt <0:
				smlt +=1
				total.append([0])
				passed.append([0])
				failed_lines.append([])
			elif total[smlt][0]:
				smlt +=1
				total.append([0])
				passed.append([0])
				failed_lines.append([])
	
	if failed_lines:
		for x in range(len(failed_lines)):
			if failed_lines[x]:
				amount_chr = int(len(failed_lines[x][0]))-3
				print(amount_chr*'=',"errors lines",x,"th")
				for y in failed_lines[x]:
					print(y, end='')
				print(len(failed_lines[x][0])*'-')
	for x in range(len(total)):
		print(f"{x+1} PASS: {passed[x][0]} | FALIED: {len(failed_lines[x])} | TOTAL: {total[x][0]}")


parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", type=str, required=True, help="Path of File data (file.log simulated) ")
args = parser.parse_args()
if __name__=="__main__":
	check_result(args.log)