
module decoder328(output reg [7:0] out, input [2:0] in,input e);
 always @(*) begin
 #1;
 out[0] = (~in[2] & ~in[1] & ~in[0] & e);
 out[1] = (~in[2] & ~in[1] & in[0] & e);
 out[2] = (~in[2] & in[1] & ~in[0] & e);
 out[3] = (~in[2] & in[1] & in[0] & e);
 out[4] = (in[2] & ~in[1] & ~in[0] & e);
 out[5] = (in[2] & ~in[1] & in[0] & e);
 out[6] = (in[2] & in[1] & ~in[0] & e);
 out[7] = (in[2] & in[1] & in[0] & e);
 end
endmodule

module tb_decoder328;
 wire [7:0] out;
 reg [2:0] in;
 reg e;
 integer x;
 decoder328 dcd328(out, in, e);

 initial begin
  #5 e = 0;
  for (x=0; (x < 8); x=x+1) 
  begin
   #5 in = x;
   if (out === 8'b0) begin
   $display("PASSED| %b %b  %b  %b  | %b %b %b %b %b %b %b %b |", e, in[2], in[1], in[0],
                                                               out[7], out[6], out[5], out[4], out[3], out[2], out[1], out[0]);
   end
   else  begin
    $display("FAILED| %b %b  %b  %b  | %b %b %b %b %b %b %b %b |", e, in[2], in[1], in[0],
                                                               out[7], out[6], out[5], out[4], out[3], out[2], out[1], out[0]);
   end
  end
  #5 e = 1;in=3'b0;
  for (x=0; (x < 8); x=x+1) 
  begin
   in = x;
   #5;
   if (out === (8'b1 << in)) begin
   
   $display("PASSED| %b %b  %b  %b  | %b %b %b %b %b %b %b %b |", e, in[2], in[1], in[0],
                                                               out[7], out[6], out[5], out[4], out[3], out[2], out[1], out[0]);
   end
   else  begin
    $display("FAILED| %b %b  %b  %b  | %b %b %b %b %b %b %b %b |", e, in[2], in[1], in[0],
                                                               out[7], out[6], out[5], out[4], out[3], out[2], out[1], out[0]);
   end
   
  end
 end
endmodule


