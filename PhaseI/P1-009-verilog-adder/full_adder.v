// full_adder.v ? Used half_adder had delay, increasing
module full_adder ( output sum, cout, input cin, a, b);
    wire s1, c1, c2;
    half_adder ha1 (.a(a), .b(b), .sum(s1), .carry(c1));
    half_adder ha2 (.a(s1), .b(cin), .sum(sum), .carry(c2));
    assign #1 cout = c1 | c2;
endmodule

module tb_full_adder;
 reg a = 1'b0, b = 1'b0;
 reg cin = 1'b0;
 wire sum, carry;
 integer x, y, z;
 full_adder fa(sum, carry, cin, a, b);

 initial begin
  #5 $display("-----------------");
  #5 $display("| ci a b | s co |");
  #5 $display("-----------------");
  for (x=0;x<=1;x=x+1) begin
   for (y=0;y<=1;y=y+1) begin
    for (z=0;z<=1;z=z+1) begin
     #5 $display("| %b  %b %b | %b %b  |", cin, a, b, sum, carry);
     b = b+1;
    end
    a = a+1;
   end
   cin = cin+1;
  end
  #5 $display("-----------------");
 end
endmodule
  