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
    prots = sorted(m['target_chembl_id'].unique())
    chunk_size = 10
    for i in range(0, len(prots), chunk_size):
        sys.stderr.write('%d/%d\n' % (i, len(prots)))
        res = new_client.activity.filter(target_chembl_id__in=prots[i: i+chunk_size])
        if len(res) == 0:
            continue
        for j in range(0, len(res), 1000):
            sys.stderr.write('%d/%d %d/%d\n' % (i, len(prots),
                                                j, len(res)))
            n = pd.concat([pd.Series(x).to_frame().T for x in res[j: j+100]])
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
    sys.stderr.write('%d/%d\n' % (i, len(prots)))
