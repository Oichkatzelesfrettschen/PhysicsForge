"""
Script to add figure environments and labels to figure modules
"""
from pathlib import Path

# Mapping of figure files to labels and captions
FIGURE_UPDATES = {
    'modules/figures/fig_casimir_enhancement.tex': {
        'label': 'fig:casimir-enhancement',
        'caption': 'Casimir force enhancement for various fractal plate geometries showing 15-25% deviations from standard predictions at micron separations.'
    },
    'modules/figures/fig_zpe_coherence.tex': {
        'label': 'fig:zpe-coherence',
        'caption': 'ZPE coherence optimization as a function of quantum foam density parameter $\\kappa$, showing optimal value $\\kappa_{\\text{opt}} \\approx 0.90$.'
    },
}

def wrap_figure_with_environment(filepath, label, caption):
    """Wrap tikzpicture in figure environment with label and caption"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has figure environment
        if '\\begin{figure}' in content:
            print(f"Skipping {filepath} - already has figure environment")
            return False

        # Add figure environment at the beginning
        new_content = '\\begin{figure}[htbp]\n\\centering\n' + content

        # Add caption and label at the end
        new_content = new_content.rstrip() + '\n'
        new_content += f'\\caption{{{caption}}}\n'
        new_content += f'\\label{{{label}}}\n'
        new_content += '\\end{figure}\n'

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Added figure environment to {filepath}")
        return True

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    count = 0
    for filepath, meta in FIGURE_UPDATES.items():
        if wrap_figure_with_environment(filepath, meta['label'], meta['caption']):
            count += 1

    print(f"\nProcessed {count} figure files")

if __name__ == "__main__":
    main()
