# arg-check-tools
Simple tools to analyze a long list of argument flags passed to a command.

# Motivation
I got tired of “eyeballing” differences between the long list of flags passed to a test script. The list of flags, or in this case the run arguments, are different for various tests. I wrote this script to better understand what is different. I have used this for the arguments to a particular test script so far, but it should also work for any list of arguments that use dash (-) flags.
 
## Here is how you can run it:
 
arg_diff.py <file1> <file2>
 
## Here is an example of the output:
 
arg_diff.py RunArgs_test1 RunArgs_test2
``` 
-dump
        < <FLAGNOTFOUND>
        >
-lsf_rusage
        < <FLAGNOTFOUND>
        > mem=65000
-ncelaboptions
        < -notimingchecks -timescale 1ps/1ps
        > -SDF_NOPAthedge -maxdelays -sdf_cmd_file $WORKAREA/sdf_cmds -timescale 1ps/1ps -warnmax 0
-ncvlogoptions
        < +define+NO_DPI_REG_LEAF_REGISTER +define+NO_DPI_REG_LEAF_REGISTER
        > +define+NO_DPI_REG_LEAF_REGISTER -nonotifier
-seed
        < 54321
        > 305008
-simargs
        < +SERDES_FREQ=25 +TB_MODE=1 +UVM_TESTNAME=gatesim_test +UVM_VERBOSITY=UVM_MEDIUM +dump_start=82700 +dump_stop=83700 +no_gen_fifo_eot_checks +set_values_brute_force+100 +set_values_delay+50 +uvm_set_config_int=\*,reset_assert_cycles,600
        > +UVM_MAX_QUIT_COUNT=50000 +UVM_TESTNAME=gatesim_test +UVM_VERBOSITY=UVM_HIGH +dump_start=2400 +dump_stop=8000 +set_values_brute_force+10 +set_values_delay+4 +uvm_set_config_int=\*,reset_assert_cycles,3500 +uvm_set_config_int=\*,reset_deassert_cycles,100
-tCat
        < gates_fakesdview_
        > gates_funcview_
-vcomp
        < +define+BEHAV_SRAM +define+ERRTIME=10000 +define+ERRTIME=10000 +define+ERR_TIME=10000 +define+ERR_TIME=10000 +define+GATESIM +define+GATESIM +define+GATE_SIM +define+GATE_SIM +define+SET_VALUES_ZEROS_ALL +define+UVM_NO_DEPRECATED +define+UVM_NO_DEPRECATED +define+UVM_NO_SYSTEMC +define+UVM_REG_DATA_WIDTH=96 +define+approximate +define+approximate
        > +define+BEHAV_SRAM +define+BEHAV_SRAM +define+ERRTIME=10000 +define+ERR_TIME=10000 +define+GATESIM +define+GATE_SIM +define+GATE_SIM +define+SET_VALUES_ZEROS_ALL +define+UVM_NO_DEPRECATED +define+UVM_NO_DEPRECATED +define+UVM_NO_SYSTEMC +define+UVM_REG_DATA_WIDTH=96 +define+approximate +define+approximate
```        
