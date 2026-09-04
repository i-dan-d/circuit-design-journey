Subtasks

Half Adder: sum = A XOR B, carry = A AND B

Full Adder: sum = A XOR B XOR Cin, Carry out logic

Ripple Carry Adder 4-bit: kết nối 4 Full Adder

Hiểu tại sao Ripple Carry chậm: carry phải ripple qua từng FA

Carry Lookahead Adder concept: generate và propagate

Testbench: test tất cả combination, bao gồm overflow

Python: script verify output của simulation tự động

Done When

4-bit ripple carry adder: testbench pass 100% (tất cả 256 input combinations), có timing comparison với Half Adder trong waveform