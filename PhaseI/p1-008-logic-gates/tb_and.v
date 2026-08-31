module tb_and;
 wire out;
 reg a , b;
 
 //dataflow dtf(out, a,b);
 //gate_level gl(out, a,b);
 behavioral bhvr(out, a,b);
 initial begin
  $monitor("a = %b, b = %b | out = %b", a, b, out);
  a = 0; b = 0;
  #10 a = 0; b = 1;
  #10 a = 1; b = 0;
  #10 a = 1; b = 1;
  #10 $finish;
  end
endmodule
