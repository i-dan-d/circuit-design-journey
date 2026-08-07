import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--family", type=str, required=True, help="File data family curves (Vds sweep)")
parser.add_argument("-t", "--vth", type=str, required=True, help="File data Vth extraction (Vgs sweep, Vds nhỏ)")
args = parser.parse_args()

# ============ PHẦN A: FAMILY CURVES (đẹp) ============
df_fam = pd.read_csv(args.family, sep='\t')

sep_rows = df_fam.index[df_fam["V(vin)"].isna()].tolist()
sep_rows.append(len(df_fam))

blocks = []
start = 0
for end in sep_rows:
    block = df_fam.iloc[start:end].dropna(subset=["V(vin)", "V(vdd)", "Id(M1)"])
    if len(block) > 0:
        blocks.append(block)
    start = end + 1

# ============ PHẦN B: VTH EXTRACTION (chuẩn) ============
df_vth = pd.read_csv(args.vth, sep='\t').dropna(subset=["V(vin)", "Id(M1)"])
Vgs = df_vth["V(vin)"].values
Id_vth = df_vth["Id(M1)"].values

sort_idx = np.argsort(Vgs)
Vgs = Vgs[sort_idx]
Id_vth = Id_vth[sort_idx]

_, uniq_idx = np.unique(Vgs, return_index=True)
Vgs = Vgs[uniq_idx]
Id_vth = Id_vth[uniq_idx]

gm = np.gradient(Id_vth, Vgs)
idx = np.argmax(gm)
Vgs_t, Id_t, gm_max = Vgs[idx], Id_vth[idx], gm[idx]
Vth = Vgs_t - Id_t / gm_max

Vds_used = df_vth["V(vdd)"].iloc[0] if "V(vdd)" in df_vth.columns else "?"
print(f"Vth = {Vth:.4f} V   (đo tại Vds = {Vds_used}V, độ phân giải Vgs = {np.diff(Vgs).mean():.4f}V)")

# ============ VẼ 2 SUBPLOT ============
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Subplot 1: family curves ---
colors = plt.cm.viridis(np.linspace(0, 0.9, len(blocks)))
for block, c in zip(blocks, colors):
    vgs_val = block["V(vin)"].iloc[0]
    ax1.plot(block["V(vdd)"], block["Id(M1)"], color=c, label=f"Vgs={vgs_val:.1f}V")
ax1.set_xlabel("Vds (V)")
ax1.set_ylabel("Id (A)")
ax1.set_title("Id–Vds family curves")
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

# --- Subplot 2: Vth extraction ---
tangent = Id_t + gm_max * (Vgs - Vgs_t)
ax2.plot(Vgs, Id_vth, color='#2a78d6', label="Id–Vgs (data)")
ax2.plot(Vgs, tangent, '--', color='#eb6834', label="Tiếp tuyến (gm max)")
ax2.axhline(0, color='black', linewidth=0.8)
ax2.axvline(Vth, color='red', linestyle=':', label=f"Vth = {Vth:.3f}V")
ax2.set_ylim(min(Id_vth)*1.2, max(Id_vth)*1.2)
ax2.set_xlabel("Vgs (V)")
ax2.set_ylabel("Id (A)")
ax2.set_title(f"Vth extraction (linear extrapolation)")
ax2.legend(fontsize=8)
ax2.grid(alpha=0.3)

fig.suptitle("NMOS Characterization")
fig.tight_layout()
fig.savefig("MOSFET_full_analysis.png", dpi=300, bbox_inches='tight')
plt.show()