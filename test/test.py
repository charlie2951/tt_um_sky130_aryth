# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_alu_crypt(dut):
    """Test the 4-bit ALU with basic operations"""
    
    # 1. Start the clock (10ns period = 100MHz)
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # 2. Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    # 3. Reset sequence
    await Timer(30, unit="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    
    # 4. Example Test Case: Drive ui_in
    # Based on your Verilog tb (ui_in = 8'b00110010)
    # op=4'b0001
    dut.ui_in.value =  0b01111001
    dut.uio_in.value = 0b00011000
    
    # Wait for a few clock cycles for logic to propagate
    for _ in range(5):
        await RisingEdge(dut.clk)

    # 5. Log the output
    output_val = dut.uo_out.value
    dut._log.info(f"ALU Output uo_out: {output_val}")

    # Optional: Basic assertion (Adjust based on your ALU's expected behavior)
    # assert output_val == 5
