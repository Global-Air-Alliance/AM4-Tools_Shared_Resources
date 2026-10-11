AM4 Streckenrechner – Spieldaten (Quelle: github.com/abc8747/am4, Stand Aug 2026)

airports.json       3907 Flughäfen, Reihenfolge = Datenbank-Index (0..3906)
                    Felder: name, fullname, country, iata, icao, lat, lng, rwy (ft)
demand/<idx>.bin    Nachfrage ab Flughafen <idx> zu allen 3907 Flughäfen:
                    je Ziel 3 x uint16 little-endian (Y, J, F) = 23'442 Bytes/Datei
                    Wert fuer Ziel k liegt bei Byte-Offset k*6.

Neu erzeugen: build_data.py (benoetigt pandas + pyarrow und das am4-Repo).
