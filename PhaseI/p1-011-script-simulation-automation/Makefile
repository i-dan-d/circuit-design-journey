# ==========================================
# MAKEFILE FOR MODELSIM AUTOMATION (WINDOWS)
# ==========================================

export TMP = C:/temp
export TEMP = C:/temp

SIM = vsim
VSIM_FLAGS = -c -do "transcript file transcript.log; run -all; quit -f"
PYTHON = python

TB_SRC    = F:/Circuit_Design/circuit-design-journey/PhaseI/p1-010-verilog-decoder-encoder-multiplexer-demultiplexer/decoder.v
TB_MODULE = tb_decoder328
LOG_FILE  = transcript.log

all: report

# 1. Sử dụng mkdir -p chuẩn Bash/Linux
compile:
	mkdir -p C:/temp
	vlib work
	vlog $(TB_SRC)

# 2. Chạy mô phỏng ModelSim
sim: compile
	$(SIM) $(VSIM_FLAGS) $(TB_MODULE)

# 3. Phân tích kết quả bằng Python Script
report: sim
	$(PYTHON) main.py --log $(LOG_FILE)

# 4. Dọn dẹp thư mục làm việc
clean:
	rm -rf work $(LOG_FILE) *.wlf vsim.wlf C:/temp

.PHONY: all compile sim report clean