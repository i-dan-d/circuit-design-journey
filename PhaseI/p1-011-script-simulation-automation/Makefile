# # ==========================================
# # MAKEFILE FOR MODELSIM AUTOMATION (WSL)
# # ==========================================
COMPILER = 


TB_SRC    ?= ../p1-010-verilog-decoder-encoder-multiplexer-demultiplexer/decoder.v
TB_MODULE ?= tb_decoder328
LOG_FILE  ?= transcript.log
TEMP_DIR = temp
WORK_DIR = work
PYTHON_CR = main.py
all:clean report
compile:
	mkdir -p $(TEMP_DIR)
	vlib.exe $(WORK_DIR)
	vlog.exe $(TB_SRC)
simulation: compile
	vsim.exe -c $(TB_MODULE) -do "transcript file $(TEMP_DIR)/$(LOG_FILE); run -all; quit -f" 
	

report: simulation
	python.exe $(PYTHON_CR) --log ./$(TEMP_DIR)/$(LOG_FILE)

clean:
	rm -rf $(WORK_DIR)/*
	rm -rf $(TEMP_DIR)/$(LOG_FILE)

.PHONY: all compile sim report clean