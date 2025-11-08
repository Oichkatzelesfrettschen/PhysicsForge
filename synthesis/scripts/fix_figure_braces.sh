#!/bin/bash
# Fix \end{figure> typo in all figure files

for fig in fig_e6_dynkin_diagram fig_gem_field_lines fig_conflict_resolution_tree fig_dimensional_tower fig_nodespace_graph fig_scalar_field_hierarchy fig_f4_root_projection; do
  file="modules/figures/${fig}.tex"
  if [ -f "$file" ]; then
    # Replace \end{figure> with \end{figure}
    sed -i 's/\\end{figure>/\\end{figure}/g' "$file"
    echo "Fixed: $fig"
  fi
done

echo ""
echo "Verification:"
for fig in fig_e6_dynkin_diagram fig_gem_field_lines fig_conflict_resolution_tree fig_dimensional_tower fig_nodespace_graph fig_scalar_field_hierarchy fig_f4_root_projection; do
  file="modules/figures/${fig}.tex"
  balance=$(python3 scripts/find_brace_errors.py "$file" 2>&1 | grep "Final balance" | awk '{print $3}')
  echo "$fig: $balance"
done
