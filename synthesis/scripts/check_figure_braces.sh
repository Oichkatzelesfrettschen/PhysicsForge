#!/bin/bash
# Check brace balance in figure files

for fig in fig_e7_e8_comparison fig_e6_dynkin_diagram fig_gem_field_lines fig_conflict_resolution_tree fig_dimensional_tower fig_nodespace_graph fig_scalar_field_hierarchy fig_f4_root_projection; do
  file="modules/figures/${fig}.tex"
  if [ -f "$file" ]; then
    balance=$(python3 scripts/find_brace_errors.py "$file" 2>&1 | grep "Final balance" | awk '{print $3}')
    echo "$fig: $balance"
  else
    echo "$fig: FILE NOT FOUND"
  fi
done
