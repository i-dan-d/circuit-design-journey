module mux421(output reg out, input wire [3:0] IN, input wire [1:0] S);
 always @(*) begin
  out = (IN[0]&~S[1]&~S[0]) | (IN[1]&~S[1]&S[0]) | (IN[2]&S[1]&~S[0]) | (IN[3]&S[1]&S[0]);
 end
endmodule
module tb_mux421;
 wire out;
 reg [3:0] IN;
 reg [1:0] S = 2'b00;
 integer x;
 mux421 my_mux(out, IN, S);
 initial  begin
  IN[3]=1;IN[2]=0;IN[1]=1;IN[0]=0;
  for (x=0; x<4; x=x+1) begin
   #5;
   if (out === IN[x]) begin
    $display("PASSED| %b   %b   |   %b   |", S[1], S[0], out);
   end
   else begin
    $display("FAILED| %b   %b   |   %b   |", S[1], S[0], out);
   end
   S = S+1;
  end
 end
endmodule