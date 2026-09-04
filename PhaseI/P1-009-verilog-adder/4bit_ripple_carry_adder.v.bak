module ripple_carry_adder4bit(cout, sum, cin, a, b);
 output [3:0] cout, sum;
 input cin;
 input [3:0] a, b;
 full_adder fa0(sum[0], cout[0], cin, a[0], b[0]);
 full_adder fa1(sum[1], cout[1], cout[0], a[1], b[1]);
 full_adder fa2(sum[2], cout[2], cout[1], a[2], b[2]);
 full_adder fa3(sum[3], cout[3], cout[2], a[3], b[3]);
endmodule

module tb_ripple_carry_adder4bit;
 reg [3:0] a=4'd0, b=4'd0;
 reg cin =1'b0;
 wire [3:0] sum ;
 wire [3:0] cout;
 integer x, y, errors = 0;

 ripple_carry_adder4bit CRA(cout, sum, cin, a, b);
 initial begin
  for (x=0; x<16; x=x+1) begin
   for (y=0; y<16; y=y+1) begin
    #3;
    if ({cout[3], sum} !== (a + b + cin)) begin
     errors = errors+1;
     $display("FAILED| %b + %b = %b <=> %d + %d = %d |", a, b, {cout[3], sum}, a, b, {cout[3], sum});
    end
    else $display("PASS| %b + %b = %b <=> %d + %d = %d |", a, b, {cout[3], sum}, a, b, {cout[3], sum});
    b = b+1;
   end
   a = a+1;
  end
 end
endmodule
 