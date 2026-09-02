module demux421(output reg [3:0] D, input  IN, input wire [1:0] S);
 always @(*) begin
  D[0] = (IN&~S[1]&~S[0]);
  D[1] = (IN&~S[1]&S[0]);
  D[2] = (IN&S[1]&~S[0]);
  D[3] = (IN&S[1]&S[0]);
 end
endmodule

module tb_demux421;
 wire [3:0] out;
 reg [1:0] S=2'b00;
 reg IN = 1'b0;
 integer x, y;
 demux421 mydemux421(out, IN, S);

 initial begin
  
  $display("+--------------------------+");
  $display("| IN S1  S0  | O3 O2 O1 O0 |");
  $display("+--------------------------+");

  for (y=0; y<=1; y=y+1) begin
   for (x=0; x<4; x=x+1) begin
    #5 $display("| %b  %b   %b   | %b  %b  %b  %b |",IN, S[1], S[0], out[3], out[2], out[1], out[0]);
    S = S+1;
   end
   IN = IN+1;
  end
  $display("+--------------------------+");
 end
endmodule
  
