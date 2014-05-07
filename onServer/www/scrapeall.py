import os
import re
import sys

# Apologies for the shit code. <3

# ==================================================================
# ============================== DATA ==============================
# ==================================================================
clusternames = ["SERVERS", "GHC 5201", "GHC 3000", "GHC 5205", "GHC 5208"]

clusters = {
"SERVERS": [
  "unix1.andrew.cmu.edu",
  "unix2.andrew.cmu.edu",
  "unix3.andrew.cmu.edu",
  "unix4.andrew.cmu.edu",
  "unix5.andrew.cmu.edu",
  "unix6.andrew.cmu.edu"
  ],

"GHC 5201": [
  "ghc01.ghc.andrew.cmu.edu",
  "ghc02.ghc.andrew.cmu.edu",
  "ghc03.ghc.andrew.cmu.edu",
  "ghc04.ghc.andrew.cmu.edu",
  "ghc05.ghc.andrew.cmu.edu",
  "ghc06.ghc.andrew.cmu.edu",
  "ghc07.ghc.andrew.cmu.edu",
  "ghc08.ghc.andrew.cmu.edu",
  "ghc09.ghc.andrew.cmu.edu",
  "ghc10.ghc.andrew.cmu.edu",
  "ghc11.ghc.andrew.cmu.edu",
  "ghc12.ghc.andrew.cmu.edu",
  "ghc13.ghc.andrew.cmu.edu",
  "ghc14.ghc.andrew.cmu.edu",
  "ghc15.ghc.andrew.cmu.edu",
  "ghc16.ghc.andrew.cmu.edu",
  "ghc17.ghc.andrew.cmu.edu",
  "ghc18.ghc.andrew.cmu.edu",
  "ghc19.ghc.andrew.cmu.edu",
  "ghc20.ghc.andrew.cmu.edu",
  "ghc21.ghc.andrew.cmu.edu",
  "ghc22.ghc.andrew.cmu.edu",
  "ghc23.ghc.andrew.cmu.edu",
  "ghc24.ghc.andrew.cmu.edu",
  "ghc25.ghc.andrew.cmu.edu",
  ],

"GHC 3000": [
  "ghc27.ghc.andrew.cmu.edu",
  "ghc28.ghc.andrew.cmu.edu",
  "ghc29.ghc.andrew.cmu.edu",
  "ghc30.ghc.andrew.cmu.edu",
  "ghc31.ghc.andrew.cmu.edu",
  "ghc32.ghc.andrew.cmu.edu",
  "ghc33.ghc.andrew.cmu.edu",
  "ghc34.ghc.andrew.cmu.edu",
  "ghc35.ghc.andrew.cmu.edu",
  "ghc36.ghc.andrew.cmu.edu",
  "ghc37.ghc.andrew.cmu.edu",
  "ghc38.ghc.andrew.cmu.edu",
  "ghc39.ghc.andrew.cmu.edu",
  "ghc40.ghc.andrew.cmu.edu",
  "ghc41.ghc.andrew.cmu.edu",
  "ghc42.ghc.andrew.cmu.edu",
  "ghc43.ghc.andrew.cmu.edu",
  "ghc44.ghc.andrew.cmu.edu",
  "ghc45.ghc.andrew.cmu.edu",
  "ghc46.ghc.andrew.cmu.edu",
  "ghc47.ghc.andrew.cmu.edu",
  "ghc48.ghc.andrew.cmu.edu",
  "ghc49.ghc.andrew.cmu.edu",
  "ghc50.ghc.andrew.cmu.edu",
  ],

"GHC 5205": [
  "ghc52.ghc.andrew.cmu.edu",
  "ghc53.ghc.andrew.cmu.edu",
  "ghc54.ghc.andrew.cmu.edu",
  "ghc55.ghc.andrew.cmu.edu",
  "ghc56.ghc.andrew.cmu.edu",
  "ghc57.ghc.andrew.cmu.edu",
  "ghc58.ghc.andrew.cmu.edu",
  "ghc59.ghc.andrew.cmu.edu",
  "ghc60.ghc.andrew.cmu.edu",
  "ghc61.ghc.andrew.cmu.edu",
  "ghc62.ghc.andrew.cmu.edu",
  "ghc63.ghc.andrew.cmu.edu",
  "ghc64.ghc.andrew.cmu.edu",
  "ghc65.ghc.andrew.cmu.edu",
  "ghc66.ghc.andrew.cmu.edu",
  "ghc67.ghc.andrew.cmu.edu",
  "ghc68.ghc.andrew.cmu.edu",
  "ghc69.ghc.andrew.cmu.edu",
  "ghc70.ghc.andrew.cmu.edu",
  "ghc71.ghc.andrew.cmu.edu",
  "ghc72.ghc.andrew.cmu.edu",
  "ghc73.ghc.andrew.cmu.edu",
  "ghc74.ghc.andrew.cmu.edu",
  "ghc75.ghc.andrew.cmu.edu",
  "ghc76.ghc.andrew.cmu.edu",
  ],

"GHC 5208": [
  "ghc86.ghc.andrew.cmu.edu",
  "ghc87.ghc.andrew.cmu.edu",
  "ghc88.ghc.andrew.cmu.edu",
  "ghc89.ghc.andrew.cmu.edu",
  "ghc90.ghc.andrew.cmu.edu",
  "ghc91.ghc.andrew.cmu.edu",
  "ghc92.ghc.andrew.cmu.edu",
  "ghc93.ghc.andrew.cmu.edu",
  "ghc94.ghc.andrew.cmu.edu",
  "ghc95.ghc.andrew.cmu.edu",
  "ghc96.ghc.andrew.cmu.edu",
  "ghc97.ghc.andrew.cmu.edu",
  "ghc98.ghc.andrew.cmu.edu",
  "ghc99.ghc.andrew.cmu.edu",
  ]}

# ======================================================================
# ============================== SCRAPERS ==============================
# ======================================================================
def whoScrape(filename):
  entry = re.compile(
    r"""(?P<andrewid>\S+)\s+(?P<terminal>(tty\d+)|(pts/\d+)).*$""", re.VERBOSE)

  users = {}
  available = True

  # extract
  with open(filename) as f:
    for line in f:
      match = entry.match(line)
      if match:
        andrewid = match.group('andrewid')
        terminal = match.group('terminal')
        if andrewid not in users:
          users[andrewid] = []
        users[andrewid].append(terminal)
        if 'tty' in terminal:
          available = False

  return (available, len(users))

def psauxScrape(filename):
  entry = re.compile(
    r""".{16}
    (?P<CPU>\d{1,2}.\d)\s\s+
    (?P<MEM>\d{1,2}.\d)\s\s+
    .+$""", re.VERBOSE)

  processes = []
  CPUSum = 0.0
  MEMSum = 0.0

  with open(filename) as f:
    for line in f:
      m = entry.match(line)
      if m:
        CPUSum += float(m.group('CPU'))
        MEMSum += float(m.group('MEM'))

  return (CPUSum, MEMSum)

# ========================================================================
# ================================ SCRIPT ================================
# ========================================================================
def colorText(percent):
  n = int(percent)
  R = (255*n)/100
  G = (255*(100-n))/100;
  B = 0
  return "<font color=#%02x%02x%02x>%1.2f%%</font>" % (R, G, B, percent)

def scrapeAll(inputDir, outputFile):
  whoRecord = re.compile(r"""who_(?P<address>\S*).txt$""", re.VERBOSE)
  psauxRecord = re.compile(r"""psaux_(?P<address>\S*).txt$""", re.VERBOSE)

  files = [f for f in os.listdir(inputDir)]
  output = open(outputFile, 'w')

  computers = {}

  os.chdir(inputDir)
  for filename in files:
    whofile = whoRecord.match(filename)
    psauxfile = psauxRecord.match(filename)
    if whofile:
      address = whofile.group('address')
      (available, numUsers) = whoScrape(filename)
      if available:
        availableStr = '<font color=#00ff00>Yes</font>'
      else:
        availableStr = '<font color=#ff0000>No</font>'

      if address in clusters["SERVERS"]:
        availableStr = "N/A"

      if address not in computers:
        computers[address] = {}
      computers[address]["available"] = availableStr
      computers[address]["numUsers"] = str(numUsers)
    if psauxfile:
      address = psauxfile.group('address')
      (CPU, MEM) = psauxScrape(filename)
      if address not in computers:
        computers[address] = {}
      computers[address]["CPU"] = colorText(CPU)
      computers[address]["MEM"] = colorText(MEM)

  for clustername in clusternames:
    output.write("<h1>%s</h1>\n" % clustername)
    output.write('<table border="1" cellpadding="5" align="center">\n')
    output.write("""
    <tr>
      <th>Address</th>
      <th>Available</th>
      <th>Users Logged In</th>
      <th>CPU</th>
      <th>MEM</th>
    </tr>\n""")
    for address in clusters[clustername]:
      if address in computers:
        try:
          output.write("<tr>")
          available = computers[address]["available"]
          numUsers = computers[address]["numUsers"]
          CPU = computers[address]["CPU"]
          MEM = computers[address]["MEM"]
          line = """
          <td>%s</td>
          <td align="center">%s</td>
          <td align="center">%s</td>
          <td align="center">%s</td>
          <td align="center">%s</td>\n"""
          output.write(line % (address, available, numUsers, CPU, MEM))
          output.write("</tr>")
        except KeyError:
          # data collection error, or other problem. just skip this computer
          pass
    output.write("</table>\n")

  output.close()

if __name__ == "__main__":
  scrapeAll(sys.argv[1], sys.argv[2])
