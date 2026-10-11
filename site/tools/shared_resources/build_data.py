"""Erzeugt data/airports.json und data/demand/<idx>.bin aus abc8747/am4.
Aufruf: python3 build_data.py <pfad-zu-am4/src/am4/utils/data> [ausgabeordner]"""
import sys, os, json
import numpy as np, pandas as pd
src = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else 'data'
a = pd.read_parquet(os.path.join(src, 'airports.parquet'))
r = pd.read_parquet(os.path.join(src, 'routes.parquet'))  # oberes Dreieck (i<j), zeilenweise
N = len(a); assert len(r) == N * (N - 1) // 2
os.makedirs(os.path.join(out, 'demand'), exist_ok=True)
aps = [[x.name, x.fullname, x.country, x.iata, x.icao, round(x.lat, 5), round(x.lng, 5), int(x.rwy)] for x in a.itertuples()]
json.dump({'source': 'abc8747/am4 (airports.parquet, routes.parquet)',
           'fields': ['name', 'fullname', 'country', 'iata', 'icao', 'lat', 'lng', 'rwy'], 'airports': aps},
          open(os.path.join(out, 'airports.json'), 'w', encoding='utf-8'), separators=(',', ':'), ensure_ascii=False)
M = np.zeros((N, N, 3), dtype='<u2'); i, j = np.triu_indices(N, 1)
d = r[['yd', 'jd', 'fd']].to_numpy().astype('<u2'); M[i, j] = d; M[j, i] = d
for k in range(N): M[k].tofile(os.path.join(out, 'demand', f'{k}.bin'))
print(f'{N} Flughaefen, {len(r)} Strecken -> {out}/')
