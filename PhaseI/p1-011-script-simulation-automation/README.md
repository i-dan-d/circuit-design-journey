Before runing: install Modelsim, make.exe (In this DIR I used WSL to run Makefile)
In this issue, I was learn how to automation the simulation.
The first, I used default ouput format for $display in Modelsim
Comparison actual and expected, and cout pass/fail.
Used Python to exprting report: total, pass rate, list of fail case
![Simulation report automation scrip](./Show_simulation_autumation_check_results.png)
And in the end, itergrate, add into Makefile to run auto affter saved Verilog file.
![Show how Makefile work to compile, and simulate automation](./Show_how_Makefile_run.png)
