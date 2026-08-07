# Circuit Design Journey
A personal learning repository documenting my journey through circuit design concepts, from version control fundamentals to hands-on practical projects.

---

## LTSpice MOSFET Visualizer
A Python mini-project for analyzing and visualizing MOSFET characteristics from LTSpice simulation data. This tool computes threshold voltage (Vth) and plots Id–Vds family curves side by side, using two separate LTSpice simulations optimized for each purpose.

### Features
- **Threshold Voltage Extraction**: Compute Vth for NMOS/PMOS using the linear extrapolation method (max gm tangent) on a dedicated Vgs sweep
- **Id–Vds Family Curves**: Visualize multiple Vgs curves on a single plot, showing triode and saturation regions
- **Dual-Simulation Workflow**: Separates "accurate Vth" data (fine Vgs step, small fixed Vds) from "readable plot" data (coarse Vgs step, full Vds sweep) — avoids the resolution/readability trade-off in a single sweep
- **CSV/TXT Data Support**: Reads tab-separated data exported from LTSpice (`File → Export data as text`)

### Prerequisites
- Python 3.x
- LTSpice (for circuit simulation and data export)
- Required Python packages (to be installed via pip):
  - `pandas`
  - `matplotlib`
  - `numpy`

### Installation
1. **Clone or download this repository**
   ```bash
   git clone https://github.com/i-dan-d/circuit-design-journey.git
   cd circuit-design-journey
   ```
2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

This tool requires **two separate LTSpice simulations**, because accurate Vth extraction and a readable family-curve plot need different sweep resolutions:

| Purpose | Sweep setup | Why |
|---|---|---|
| Family curves (plot) | `.dc Vdd 0 5 0.02 Vin 0 2 0.4` | Coarse Vgs steps keep the plot readable; full Vds range shows triode + saturation |
| Vth extraction (accuracy) | `.dc Vin 0 3 0.005` with `Vdd` fixed at a small DC value (e.g. 0.05V) | Fine Vgs resolution and deep-triode Vds give an accurate max-gm tangent point |

1. **Run the family-curve simulation in LTSpice**
   - Sweep `Vdd` (Vds) across the full range, with `Vin` (Vgs) as the outer/step variable at coarse steps
   - Export as text (e.g. `family_curves.txt`)

2. **Run the Vth-extraction simulation in LTSpice**
   - Fix `Vdd` at a small constant value (deep triode region, e.g. 0.05V)
   - Sweep `Vin` alone with a fine step (e.g. 0.005V)
   - Export as text (e.g. `vth_data.txt`)

3. **Run the visualizer**
   ```bash
   python ".\python\LTSpice data visualizer\main.py" -f "family_curves.txt" -t "vth_data.txt"
   ```

4. **View the generated output**
   - Console prints the extracted Vth value, the Vds it was measured at, and the Vgs resolution used
   - A single figure with two subplots is saved as `MOSFET_full_analysis.png`:
     - Left: Id–Vds family curves across multiple Vgs values
     - Right: Id–Vgs curve with the max-gm tangent line and Vth marked

### Project Structure
```
circuit-design-journey/
├── python/
│   └── LTSpice data visualizer/
│       ├── main.py
│       └── [supporting modules]
└── README.md
```

### Notes
- Requires two LTSpice export files per analysis (family curves + dedicated Vth sweep) — a single combined sweep is not recommended, since a nested `.dc Vdd ... Vin ...` sweep holds Vgs constant across repeated Vds blocks, which breaks `np.gradient`-based Vth extraction (repeated/non-monotonic x-values cause division by zero)
- Currently tested with LTSpice export formats (tab-separated `.txt`)
- Supports both NMOS and PMOS transistor models
- This project was created as part of my circuit design studies

### Learning Resources
- Version Control & Git: [Missing CSAIL MIT](https://missing.csail.mit.edu/) - Highly recommended for understanding Git and version control

### Future Improvements
- [ ] Add GUI interface
- [ ] Support additional file formats
- [ ] Extended transistor model support (BSIM3/4 from real PDKs)
- [ ] Second-derivative method for Vth extraction (more robust for short-channel devices)
- [ ] Performance optimization for large datasets

---
**Last Updated**: August 7, 2026