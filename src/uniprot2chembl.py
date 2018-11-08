#!/usr/bin/env python

def get_options():
    import argparse

    description = 'Retrieve CHEMBL IDs from uniprot IDs'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('uniprots', action='store',
                        help='Uniprot IDs input file (one per line)')
    
    return parser.parse_args()

if __name__ == "__main__":
    options = get_options()

    import sys
    from chembl_webresource_client.new_client import new_client
    
    uniprots = {x.rstrip() for x in open(options.uniprots)}

    print('\t'.join(['uniprot_id',
                     'target_chembl_id',
                     'type',
                     'name']))
    for uid in uniprots:
        if uid == '' or set(uid) == set(''):
            continue
        sys.stderr.write('%s\n' % uid)
        records = new_client.target.filter(
                target_components__accession=uid
                )
        for record in records:
            print('\t'.join([uid,
                             record['target_chembl_id'],
                             record['target_type'],
                             record['pref_name']]))
