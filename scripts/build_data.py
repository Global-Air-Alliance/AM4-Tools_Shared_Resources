"""Builds data/airports.json and data/demand/<idx>.bin from abc8747/am4.
Call: python3 scripts/build_data.py <path-to-am4/src/am4/utils/data> [output folder]"""
import sys, os, json
import numpy as np, pandas as pd
src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else 'data'
a = pd.read_parquet(os.path.join(src, 'airports.parquet'))
r = pd.read_parquet(os.path.join(src, 'routes.parquet'))  # upper triangle (i<j), row by row
N = len(a); assert len(r) == N * (N - 1) // 2
os.makedirs(os.path.join(out, 'demand'), exist_ok=True)
aps = [[x.name, x.fullname, x.country, x.iata, x.icao, round(x.lat, 5), round(x.lng, 5), int(x.rwy)] for x in a.itertuples()]
json.dump({'source': 'abc8747/am4 (airports.parquet, routes.parquet)',
           'fields': ['name', 'fullname', 'country', 'iata', 'icao', 'lat', 'lng', 'rwy'], 'airports': aps},
          open(os.path.join(out, 'airports.json'), 'w', encoding='utf-8'), separators=(',', ':'), ensure_ascii=False)
M = np.zeros((N, N, 3), dtype='<u2'); i, j = np.triu_indices(N, 1)
d = r[['yd', 'jd', 'fd']].to_numpy().astype('<u2'); M[i, j] = d; M[j, i] = d
for k in range(N): M[k].tofile(os.path.join(out, 'demand', f'{k}.bin'))
print(f'{N} airports, {len(r)} routes -> {out}/')
