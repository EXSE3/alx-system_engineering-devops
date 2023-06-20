#!/bin/bash

touch "$1"; chmod u+x "$1";
echo "#!/usr/bin/env bash" >> "$1"
echo "Bash script that" >> "$1"
vi "$1"
