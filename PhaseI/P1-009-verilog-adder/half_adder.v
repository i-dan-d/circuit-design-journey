module half_adder(sum, carry, a, b);
 output reg sum, carry;
 input wire a, b;

 assign #1 sum = (a^b);
 assign #1 carry = (a&b);
endmodule