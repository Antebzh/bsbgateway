import logging
logging.basicConfig(level='DEBUG', format='%(levelname)s %(name)s:%(lineno)d -- %(message)s')

# Bus adress offset of Gateway. DO NOT USE 0!!
# Gateway will use:
# This address for logging
# This address + 1 for cmdline requests
# This address + 2 for webinterface requests
bus_address = 23

# Haupttakt. Signale koennen nicht oefter geloggt werden. Entspricht min. Zeitaufloesung.
# Einheit: Sekunden
atomic_interval = 5

# Pfad wo die tracefiles abgelegt werden
# (Dateiname = <disp_id>.trace )
tracefile_dir = 'traces'

# zu loggende Felder und Loginterval in Sekunden.
# Liste von Tupeln: (Disp_ID, Interval).
# Die Disp_ID kann am Heizungskontrollpanel oder in bsb_fields.py
# nachgeschlagen werden.
# Intervall in Sekunden, MUSS ganzzahliges Vielfaches des atomic_interval sein!!!
loggers = [
    (8510, 5), # Kollektortemperatur
    (8310, 300), # Kesseltemperatur
    (8830, 300), # TW-Temperatur 1
    (8832, 300), # TW-Temperatur unten
    (8743, 300), # Vorlauftemp. 1
    (8700, 300), # Aussentemperatur
    (8003, 300), # Status TW
    (8007, 5), # Status Solar
]

# Trigger fuer Email-Ausloesung.
# Tupel (Disp_ID, Triggertyp, Schwellwert(e))
# Triggertypen: 'rising_edge', 'falling_edge' (1 Schwellwert)
#  Schwellwert = in Einheiten des decodierten Feldwertes.
# Nach jeder Triggerausloesung gelten 6 Std. Totzeit.
# Der Trigger funktioniert nur wenn fuer das Feld auch ein Logger definiert ist!

triggers = [
# Example: notify when value of 8700 falls below 10.0.
#    (8700, 'falling_edge', 10.0),
]

# Email recipient
emailaddress = 'recipient@domain.com'

# SMTP server and credentials for sending email notifications
emailserver = 'smtp.domain.com'
emailcredentials = ('loginname', 'password')


import bsbgateway
bsbgateway.run(globals())