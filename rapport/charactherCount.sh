#!/bin/bash

testNumber=$( tail -n +150 main.tex | detex | sed "s/^\s*//g;s/\s*$//g" | tr "\n" " " | sed "s/STOPSTOP/\n/g" | head -n 1 | wc -c ) && echo -n "$testNumber " && bc <<< "scale=3;$testNumber/2400"
