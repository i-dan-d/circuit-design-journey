raw_members = "raw_member.txt"
file_report = "Report_outcome.txt"
list_raw_data = []

def competitive_score_computation(name, attendance_points=50, Join_the_event=False, share_idea= False ):
	attendance_points = int(attendance_points)
	if Join_the_event:
		attendance_points += 15
	if share_idea:
		attendance_points +=10
	if attendance_points >100:
		attendance_points = 100
	return name, attendance_points
with open(raw_members, 'r', encoding="utf-8") as f_raw:
	title = (f_raw.readline().strip().replace("(True/False)", '').replace(" ", '').split(','))
	for line in f_raw:
		part = (line.strip().replace(' ', '').split(','))
		user_dict = {
		title[0]:part[0],
		title[1]:part[1],
		title[2]:part[2],
		title[3]:part[3],
		}
		list_raw_data.append(user_dict)
with open(file_report, 'w', encoding="utf-8") as f_outcome:
	f_outcome.write(
"""+===================================================+
|			BÁO CÁO THÔNG TIN SINH VIÊN THAM 		|
|			GIA CÁC SỰ KIỆN, TIẾT HỌC				|
+===================================================+\n""")
	list_title_outcome = ["STT","Name", "Scores", "Detail"]
	title_outcome = "."
	STT = 0
	for titles in list_title_outcome:
		title_outcome += f", {titles}"
	f_outcome.write(title_outcome.replace("., ",""))
	for members in list_raw_data:
		check = competitive_score_computation(members[title[0]], members[title[1]], members[title[2]], members[title[3]])
		point = check[1]
		STT += 1
		if point >= 90:
			f_outcome.write(f"\n{STT}, {check[0]}, {point}, {"excellent"}")
		elif point >= 75:
			f_outcome.write(f"\n{STT}, {check[0]}, {point}, {"Good"}")
		else:
			f_outcome.write(f"\n{STT}, {check[0]}, {point}, {"Complate the task"}")

