#!/usr/bin/env python

def get_options():
    import argparse

    description = 'From protein Chembl IDs to other tables'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('proteins', action='store',
                        help='Protein table (must have a "target_chembl_id" column)')
    
    return parser.parse_args()

if __name__ == "__main__":
    options = get_options()

    import sys
    import pandas as pd
    from chembl_webresource_client.new_client import new_client
    
    m = pd.read_table(options.proteins)
    h = True
    for tid in m['target_chembl_id'].unique():
        res = new_client.mechanism.filter(target_chembl_id__exact=tid)
        if len(res) == 0:
            continue
        n = pd.concat([pd.Series(x).to_frame().T for x in res])
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
