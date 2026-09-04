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
		elif "run -all" in line:
			smlt +=1
			total.append([0])
			passed.append([0])
			failed_lines.append([])
	
	if failed_lines:
		print("The errors lines:")
		for x in range(len(failed_lines)):
			if failed_lines[x]:
				amount_chr = int(len(failed_lines[x][0]))-3
				print(amount_chr*'=',x,"th")
				for y in failed_lines[x]:
					print(y, end='')
				print(len(failed_lines[x][0])*'-')
	for x in range(len(total)):
		print(f"{x+1} PASS: {passed[x]} | FALIED: {len(failed_lines[x])} | TOTAL: {total[x]}")

check_result("./RCA4.log")