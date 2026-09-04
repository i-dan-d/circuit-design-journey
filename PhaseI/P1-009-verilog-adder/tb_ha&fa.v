module tb_ha_fa;
 reg a=1'b0,b=1'b0;
 reg cin=1'b0;
 wire sumha, carryha;
 wire sumfa, carryfa;
 half_adder ha(sumha, carryha, a, b);
 full_adder fa(sumfa, carryfa, cin, a, b);
 integer x,y;
 initial begin
  for(x=0;x<=1;x=x+1) begin
   for(y=0;y<=1;y=y+1) begin
    a = x;b = y;
    #10;
   end
  end
 end
endmodule
 
 