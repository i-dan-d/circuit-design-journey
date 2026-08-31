module behavioral(out, a, b);
 output out;
 input a, b;
 reg out;
 always  @(a or b) out = a & b;
endmodule