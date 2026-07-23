# Lộ Trình Học Matplotlib (Lý Thuyết + Thực Hành)

**Thời lượng gợi ý:** 5 tuần, ~1-1.5 giờ/ngày (có thể co giãn tùy tốc độ)
**Điều kiện tiên quyết:** Biết Python cơ bản (list, dict, hàm, vòng lặp)

---

## TUẦN 1: Nền tảng — NumPy & Kiến trúc Matplotlib

### Ngày 1-2: NumPy tối thiểu cần biết
**Lý thuyết:**
- Tạo mảng: `np.array()`, `np.linspace()`, `np.arange()`
- Random: `np.random.seed()`, `np.random.rand()`, `np.random.randn()`
- Toán tử vector hóa: `x**2`, `np.sin(x)`

**Thực hành:**
```python
import numpy as np

# Bài tập 1: Tạo dữ liệu
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2 / 10

# Bài tập 2: Dữ liệu ngẫu nhiên có seed cố định
np.random.seed(42)
data = np.random.randn(1000)
```
✅ **Mục tiêu:** Tự tạo được 3 bộ dữ liệu mẫu (tuyến tính, sin/cos, ngẫu nhiên) mà không cần tra Google.

---

### Ngày 3-4: Figure, Axes và 2 phong cách code
**Lý thuyết:**
- `Figure` = khung giấy tổng thể, `Axes` = một biểu đồ con trong khung đó
- Phong cách **pyplot** (nhanh, ít kiểm soát) vs **Object-Oriented — OO** (nên dùng chính)
- Anatomy: Axes, Axis, Spine, Tick, Label, Legend, Title

**Thực hành — làm lại CÙNG một biểu đồ bằng cả 2 cách để thấy sự khác biệt:**
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Cách 1: pyplot style
plt.plot(x, y)
plt.title("Sin wave - pyplot style")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()

# Cách 2: OO style (nên tập thói quen dùng cách này)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sin wave - OO style")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
plt.show()
```
✅ **Mục tiêu:** Giải thích được vì sao OO style tốt hơn khi có nhiều biểu đồ con. Từ giờ **luôn dùng OO style**.

---

### Ngày 5-7: Ôn tập + Dự án mini #1
**Thực hành — Dự án:** Vẽ 1 figure có 4 đường (sin, cos, tuyến tính, parabol) trên cùng 1 axes, mỗi đường có màu, label, linestyle khác nhau, có legend, title, grid.

```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.sin(x), color='tab:blue', linestyle='-', label='sin(x)')
ax.plot(x, np.cos(x), color='tab:orange', linestyle='--', label='cos(x)')
ax.plot(x, x/5, color='tab:green', linestyle=':', label='x/5')
ax.plot(x, x**2/20, color='tab:red', linestyle='-.', label='x²/20')
ax.legend()
ax.set_title("Dự án mini #1: So sánh 4 hàm số")
ax.grid(True, alpha=0.3)
plt.show()
```

---

## TUẦN 2: Các loại biểu đồ cơ bản

### Ngày 8-9: Line, Scatter, Bar
**Lý thuyết:** `ax.plot()`, `ax.scatter()`, `ax.bar()` / `ax.barh()` — khi nào dùng loại nào

**Thực hành:**
- Vẽ scatter plot với màu điểm phụ thuộc vào 1 biến thứ 3 (dùng `c=` và `cmap=`)
- Vẽ bar chart so sánh doanh thu 5 sản phẩm giả định

### Ngày 10-11: Histogram, Pie, Box/Violin
**Lý thuyết:** `ax.hist()`, `ax.pie()`, `ax.boxplot()`

**Thực hành:**
- Vẽ histogram phân phối dữ liệu ngẫu nhiên (thử nhiều giá trị `bins`)
- Vẽ boxplot so sánh 3 nhóm dữ liệu

### Ngày 12-14: Dự án mini #2
**Đề bài:** Tạo dataset giả (dùng NumPy) mô phỏng "điểm thi của 200 học sinh 3 lớp" rồi vẽ:
1. Histogram phân phối điểm
2. Boxplot so sánh 3 lớp
3. Bar chart điểm trung bình mỗi lớp
→ Ghép 3 biểu đồ này lại (dùng kiến thức Tuần 3, có thể làm tạm 1 hàng 3 cột trước, tối ưu sau)

---

## TUẦN 3: Tùy chỉnh & Bố cục (Subplots/Layout)

### Ngày 15-16: Tùy chỉnh chi tiết
**Lý thuyết:**
- `set_xlim/ylim`, tick, tick label (`set_xticks`, `set_xticklabels`)
- `annotate()`, `text()` để chú thích
- Colormap khi vẽ heatmap/scatter

**Thực hành:** Thêm annotation chỉ vào điểm cực đại/cực tiểu của 1 đường sin đã vẽ ở Tuần 1.

### Ngày 17-18: Subplots & GridSpec
**Lý thuyết:**
- `plt.subplots(nrows, ncols)`, `sharex`/`sharey`
- `GridSpec` cho layout không đều
- `tight_layout()` / `constrained_layout=True`

**Thực hành:**
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8), constrained_layout=True)
axes[0, 0].plot(x, np.sin(x))
axes[0, 1].scatter(x, np.cos(x), s=10)
axes[1, 0].hist(np.random.randn(500), bins=30)
axes[1, 1].bar(['A', 'B', 'C'], [3, 7, 5])
for ax, title in zip(axes.flat, ['Sin', 'Scatter', 'Hist', 'Bar']):
    ax.set_title(title)
plt.show()
```

### Ngày 19-21: Dự án mini #3 — Dashboard 4 biểu đồ
**Đề bài:** Dùng `GridSpec`, tạo 1 layout gồm:
- 1 biểu đồ lớn ở trên (chiếm cả chiều ngang)
- 3 biểu đồ nhỏ ở dưới
Tự chọn dữ liệu và loại chart phù hợp.

---

## TUẦN 4: Style, Export & Tích hợp Pandas

### Ngày 22-23: Style & rcParams
**Lý thuyết:**
- `plt.style.use('ggplot')`, `'seaborn-v0_8'`, `'dark_background'`
- `plt.rcParams` để set font, size mặc định toàn cục

**Thực hành:** Vẽ lại Dự án mini #1 với 3 style khác nhau, so sánh trực quan.

### Ngày 24-25: Lưu và xuất hình chuyên nghiệp
**Lý thuyết:**
- `savefig(path, dpi=300, bbox_inches='tight')`
- Phân biệt PNG (raster) vs SVG/PDF (vector)

**Thực hành:** Xuất 1 biểu đồ ra cả 3 định dạng, so sánh chất lượng khi zoom.

### Ngày 26-28: Tích hợp Pandas — Dự án mini #4
**Lý thuyết:** `DataFrame.plot()`, vẽ trực tiếp từ Series

**Thực hành:** Lấy 1 bộ dữ liệu CSV thật (ví dụ giá cổ phiếu, dân số, thời tiết) → dùng Pandas đọc dữ liệu → vẽ biểu đồ xu hướng theo thời gian bằng matplotlib (không phải `.plot()` mặc định, mà `fig, ax = plt.subplots()` rồi vẽ từ DataFrame để giữ quyền kiểm soát).

---

## TUẦN 5: Dự án tổng hợp

### Ngày 29-33: Dự án lớn — Báo cáo trực quan hoàn chỉnh
**Đề bài:** Chọn 1 bộ dữ liệu thật bạn quan tâm (kinh doanh, thể thao, tài chính, sức khỏe...) và tạo 1 "báo cáo" gồm:
1. Trang tổng quan: dashboard 4-6 biểu đồ (dùng GridSpec)
2. Áp dụng style nhất quán, màu sắc có chủ đích
3. Annotation làm nổi bật insight quan trọng
4. Xuất ra file PDF/PNG chất lượng cao để "trình bày"

### Ngày 34-35: Rà soát & mở rộng
- Xem lại toàn bộ code đã viết, refactor cho gọn
- Chọn 1 hướng nâng cao để khám phá thêm: Animation (`FuncAnimation`), 3D plot, hoặc Seaborn

---

## Checklist tự đánh giá cuối lộ trình
- [ ] Luôn dùng được OO style (`fig, ax = plt.subplots()`) thay vì pyplot state-based
- [ ] Vẽ thành thạo 6+ loại biểu đồ (line, scatter, bar, hist, pie, box)
- [ ] Tự bố cục được dashboard nhiều biểu đồ bằng GridSpec
- [ ] Tùy chỉnh được màu, style, annotation theo ý muốn
- [ ] Xuất được file chất lượng cao (dpi, định dạng phù hợp)
- [ ] Vẽ được trực tiếp từ dữ liệu Pandas thực tế
- [ ] Hoàn thành 1 dự án tổng hợp từ đầu đến cuối

## Nguồn tham khảo khi cần tra cứu
- Matplotlib official docs & gallery: matplotlib.org (phần "Examples" rất hữu ích để copy-chỉnh-sửa)
- Cheat sheet chính thức của Matplotlib (tìm "matplotlib cheat sheet" trên trang chủ)