import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import argparse
 # 1. Khởi tạo parser
parser = argparse.ArgumentParser(description="Script vẽ biểu đồ LTspice")
# 2. Thêm tham số --input (hoặc tên ngắn -i)
parser.add_argument(
    "-i",
    "--input",
    type=str,
    required=True,
    help="Đường dẫn tới file CSV/TXT",
)

# 3. Đọc tham số truyền từ Terminal
args = parser.parse_args()

input_file_name = f"{args.input}"

output_file_name = "NMOS_out.csv"
df = pd.read_csv(input_file_name, sep='\t')
# print("---------------------HEAD")
# print(df.head(1))
# print("---------------------INFO")
# df.info()
# print("---------------------DESCRIBE")
# print(df.describe())
# df.to_csv(output_file_name, index=False)

# print(np.where(df["V(vin)"].isna())) #Lấy RangeIndex của value
steps = []
steps_array = np.where(df["V(vin)"].isna())
steps_array = steps_array[0]
cout_steps = len(steps_array)

for s in range(cout_steps):
	steps.append(f"Step{s+1}/{cout_steps}")
steps.append(steps_array)

data = df
clean_data = df.loc[df["V(vdd)"].isna() == False]
Vin_max = df["V(vin)"].max()
# 1. Định nghĩa dòng ngưỡng I_th (ví dụ: 1 uA)
I_th = 1e-6

# 2. Lấy dữ liệu Vin và Id dạng mảng 1D tăng dần
v_in = df["V(vin)"].values
i_d = df["Id(M1)"].values
# 3. Nội suy lấy Vth tại điểm I_d = I_th
v_th = np.interp(I_th, i_d, v_in)
print(f"Vth (Threshold Crossing) = {v_th:.4f} V")



# print("vinmax", Vin_max)
# print(clean_data)

fig, axes = plt.subplots(figsize=(6,4))
axes.set_ylim(-1*(10**-4), (Vin_max+2)*(10**-4))

axes2 = axes.twinx()
axes2.set_ylim(-1, Vin_max+2)
for i in range(cout_steps):

	if i < cout_steps-1:
		V_dd = np.array(data["V(vdd)"].iloc[steps[-1][i]+1:steps[-1][i+1]-1])
		Id = np.array(data["Id(M1)"].iloc[steps[-1][i]+1:steps[-1][i+1]-1])
		V_in = np.array(data["V(vin)"].iloc[steps[-1][i]+1:steps[-1][i+1]-1])

		
		# print(data["V(vdd)"].iloc[steps[-1][i]+1:steps[-1][i+1]-1])
	else:
		V_dd = np.array(data["V(vdd)"].iloc[steps[-1][i]-1:])
		Id = np.array(data["Id(M1)"].iloc[steps[-1][i]-1:])
		V_in = np.array(data["V(vin)"].iloc[steps[-1][i]-1:])
		


	axes.plot(V_dd, Id )
	axes2.plot(V_dd, V_in, label=f"{steps[i]}")

axes2.legend()
fig.tight_layout()
fig.savefig("Image_visualized.png", dpi=300, bbox_inches='tight')
fig.title("Threshold Voltage")

plt.title("Visualizes MOSFET")
plt.legend()
plt.show()
