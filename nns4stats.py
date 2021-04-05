from operator import itemgetter
import csv

# Starting number of chains on main and 3p server for season 4
smartchains = 29
thirdchains = 4

thirdparty = ['CHIPS', 'EMC2', 'VRSC', 'AYA', 'MCL', 'GLEEC', 'PBC', 'HUSH3']

# @see https://github.com/KomodoPlatform/dPoW/pull/280/files
scoring_epochs = {
    "Season_4": {
        "season_start": 1592146800,
        "season_start_comment": "https://github.com/KomodoPlatform/komodo/blob/master/src/komodo_globals.h#L47",
        "season_end": 1617364800,
        "season_end_comment": "April 2nd 2021 12pm GMT https://github.com/KomodoPlatform/dPoW/commit/24b45ea5e61098fe221d2b68560778fcc72952aa#diff-ef72250c1397f6c2f24aa881988b3fe8d2d9edf7b338e9889321fa91f5c1c9acR187",
        "Servers": {
            "dPoW-Mainnet": {
                "RFOX": {
                    "end_time": 1613769736,
                    "end_time_comment": "Fri Feb 19 22:22:16 2021 +0100 commit 1c3d3cd06fd2cacc4112c5165d20e9e9fa4dadf0"
                },
                "PGT": {
                    "end_time": 1616250930,
                    "end_time_comment": "Sat Mar 20 15:35:30 2021 +0100 commit b70d11a3f356ab2aa7925ba6307a5397ab9623a0"
                },
                "STBL": {
                    "end_time": 1616250930,
                    "end_time_comment": "Sat Mar 20 15:35:30 2021 +0100 commit b70d11a3f356ab2aa7925ba6307a5397ab9623a0"
                },
                "GLEEC": {
                    "start_time": 1617181776,
                    "start_time_comment": "Tue Mar 30 17:09:36 2021 +0800 commit 677700939d5711286f69e1c9bb438ad05782230f +24hrs"
                },
                "VOTE2021": {
                    "start_time": 1617181776,
                    "start_time_comment": "Tue Mar 30 17:09:36 2021 +0800 commit 677700939d5711286f69e1c9bb438ad05782230f +24hrs"
                }
            },
            "dPoW-3P": {
                "PBC": {
                    "start_time": 1606390840,
                    "start_time_comment": "Wed Nov 25 12:40:40 2020 +0100 commit 774d6aaba0f1ad78f8cf4f6a6591ecd344ff1a60 +24hrs"
                },
                "HUSH3": {
                    "start_time": 1593331689,
                    "start_time_comment": "Sat Jun 27 10:08:09 2020 +0200 commit 09bbc0055be462ad53dbe2c0af2d7202a9c362eb +24hrs",
                    "end_time": 1603623834,
                    "end_time_comment": "Sun Oct 25 12:03:54 2020 +0100 commit 3efe36aa528495223633a560c7d457a31b3a94c3"
                },
                "GLEEC": {
                    "start_time": 1603710234,
                    "start_time_comment": "Sun Oct 25 12:03:54 2020 +0100 commit 3efe36aa528495223633a560c7d457a31b3a94c3 +24hrs"
                },
                "MCL": {
                    "start_time": 1593331689,
                    "start_time_comment": "Sat Jun 27 10:08:09 2020 +0200 commit 09bbc0055be462ad53dbe2c0af2d7202a9c362eb +24hrs"
                }
            }
        }
    }
}

notaries = [
    {'id': 0, 'name': 'alien_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 1, 'name': 'alien_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 2, 'name': 'strob_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 3, 'name': 'titomane_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 4, 'name': 'fullmoon_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 5, 'name': 'phba2061_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 6, 'name': 'fullmoon_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 7, 'name': 'fullmoon_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 8, 'name': 'madmax_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 9, 'name': 'titomane_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 10, 'name': 'cipi_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 11, 'name': 'indenodes_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 12, 'name': 'decker_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 13, 'name': 'indenodes_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 14, 'name': 'madmax_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 15, 'name': 'chainzilla_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 16, 'name': 'peer2cloud_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 17, 'name': 'pirate_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 18, 'name': 'webworker01_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 19, 'name': 'zatjum_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 20, 'name': 'titomane_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 21, 'name': 'chmex_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 22, 'name': 'indenodes_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 23, 'name': 'patchkez_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 24, 'name': 'metaphilibert_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 25, 'name': 'etszombi_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 26, 'name': 'pirate_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 27, 'name': 'metaphilibert_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 28, 'name': 'indenodes_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 29, 'name': 'chainmakers_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 30, 'name': 'mihailo_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 31, 'name': 'tonyl_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 32, 'name': 'alien_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 33, 'name': 'pungocloud_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 34, 'name': 'node9_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 35, 'name': 'smdmitry_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 36, 'name': 'nodeone_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 37, 'name': 'gcharang_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 38, 'name': 'cipi_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 39, 'name': 'etszombi_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 40, 'name': 'pbca26_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 41, 'name': 'mylo_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 42, 'name': 'swisscertifiers_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 43, 'name': 'marmarachain_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 44, 'name': 'karasugoi_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 45, 'name': 'phm87_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 46, 'name': 'oszy_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 47, 'name': 'chmex_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 48, 'name': 'dragonhound_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 49, 'name': 'strob_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 50, 'name': 'madmax_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 51, 'name': 'dudezmobi_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 52, 'name': 'daemonfox_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 53, 'name': 'nutellalicka_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 54, 'name': 'starfleet_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 55, 'name': 'mrlynch_AR', 'region': 'AR', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 56, 'name': 'greer_NA', 'region': 'NA', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 57, 'name': 'mcrypt_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 58, 'name': 'decker_EU', 'region': 'EU', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 59, 'name': 'dappvader_SH', 'region': 'SH', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 60, 'name': 'alright_DEV', 'region': 'DEV', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 61, 'name': 'artemii235_DEV', 'region': 'DEV', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 62, 'name': 'tonyl_DEV', 'region': 'DEV', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0},
    {'id': 63, 'name': 'decker_DEV', 'region': 'DEV', 'btc': 0, 'smartchain': 0, 'thirdparty': 0, 'score': 0}
]

# @see https://discordapp.com/channels/412898016371015680/456828345871761408/828270697692397608
# @see https://download.kmd.sh/s4-stats-txes-time.tar.gz
with open('s4-stats-txes-time.csv', newline='') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in readfile:
        # All need to be within season_start and season_end
        if int(row[4]) < scoring_epochs['Season_4']['season_start'] or int(row[4]) > scoring_epochs['Season_4']['season_end']:
            continue

        # KMD -> BTC static score
        if row[2] == 'KMD':
            count_index = 'btc'
            score_add = 0.0325

        # points for main server
        elif row[2] not in thirdparty:
            count_index = 'smartchain'
            # check if within time range
            if row[2] in scoring_epochs['Season_4']['Servers']['dPoW-Mainnet']:
                start_time_comp = 1592146800 if 'start_time' not in scoring_epochs['Season_4']['Servers']['dPoW-Mainnet'][row[2]] else scoring_epochs['Season_4']['Servers']['dPoW-Mainnet'][row[2]]['start_time']
                end_time_comp = 1617364800 if 'end_time' not in scoring_epochs['Season_4']['Servers']['dPoW-Mainnet'][row[2]] else scoring_epochs['Season_4']['Servers']['dPoW-Mainnet'][row[2]]['end_time']

                if int(row[4]) < start_time_comp or int(row[4]) > end_time_comp:
                    continue

            if int(row[4]) >= 1613769736 and int(row[4]) < 1616250930:
                score_add = 0.8698 / 28 # removed RFOX
            elif int(row[4]) >= 1616250930 and int(row[4]) < 1617181776:
                score_add = 0.8698 / 26 # removed PGT and STBL
            elif int(row[4]) >= 1617181776:
                score_add = 0.8698 / 28 # add GLEEC and VOTE2021
            else:
                score_add = 0.8698 / 29 # starting state with 29 smart chains

        # points for 3p server
        else:
            count_index = 'thirdparty'
            # check if within time range
            if row[2] in scoring_epochs['Season_4']['Servers']['dPoW-3P']:
                start_time_comp = 1592146800 if 'start_time' not in scoring_epochs['Season_4']['Servers']['dPoW-3P'][row[2]] else scoring_epochs['Season_4']['Servers']['dPoW-3P'][row[2]]['start_time']
                end_time_comp = 1617364800 if 'end_time' not in scoring_epochs['Season_4']['Servers']['dPoW-3P'][row[2]] else scoring_epochs['Season_4']['Servers']['dPoW-3P'][row[2]]['end_time']

                if int(row[4]) < start_time_comp or int(row[4]) > end_time_comp:
                    continue

            if int(row[4]) >= 1593331689 and int(row[4]) < 1606390840:
                score_add = 0.0977 / 6 # added HUSH3, MCL then added GLEEC removed HUSH3
            elif int(row[4]) >= 1606390840:
                score_add = 0.0977 / 7 # added PBC
            else:
                score_add = 0.0977 / 4 # starting state with 4 3p coins

        # add points to notaries
        rownotaries = row[1].split(' ')
        for rownotary in rownotaries:
            notaries[int(rownotary, 16)][count_index] += 1
            notaries[int(rownotary, 16)]['score'] += score_add

# sort by score and region
notaries.sort(key=itemgetter('score'), reverse=True)
notaries.sort(key=itemgetter('region'))

# nice output
print('{:2s} {:20s} {:6s} {:>6s} {:>9s} {:>9s} {:>9s}'.format('ID', 'Name', 'Region', 'BTC', 'Smart', 'Third', 'Score'))
current_region = ''
for notarydata in notaries:
    if notarydata['region'] != current_region:
        print('-------------------------------------------------------------------')
        current_region = notarydata['region']
    print('{:2d} {:20s} {:3s} {:9d} {:9d} {:9d} {:9.2f}'.format(notarydata['id'], notarydata['name'], notarydata['region'], notarydata['btc'], notarydata['smartchain'], notarydata['thirdparty'], notarydata['score']))
