#!/usr/bin/env python

def get_options():
    import argparse

    description = 'From molecule Chembl IDs to full details'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('molecules', action='store',
                        help='Molecules table (must have a "molecule_chembl_id" column)')
    
    return parser.parse_args()

if __name__ == "__main__":
    options = get_options()

    import sys
    import pandas as pd
    from chembl_webresource_client.new_client import new_client
    
    m = pd.read_table(options.molecules)
    h = True
    total = len(m['molecule_chembl_id'].unique())
    for i, mid in enumerate(m['molecule_chembl_id'].unique()):
        sys.stderr.write('%d/%d %s\n' % (i, total, mid))
        res = new_client.molecule.get(mid)
        if len(res) == 0:
            continue
        n = pd.Series(res).to_frame().T
        if h:
            n.to_csv(sys.stdout,
                     sep='\t',
                     header=True,
                     index=False)
            h = False
        else:
            n.to_csv(sys.stdout,
                     sep='\t',
                     header=False,
                     index=False)
