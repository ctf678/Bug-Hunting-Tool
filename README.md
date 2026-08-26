# Bug-Hunting-Tool

This is an automation tool for bug hunting, which includes subdomain enumeration and security checks. I created it to simplify bug hunting and automate common tasks like subdomain discovery and directory brute-forcing.

---

## Changes

I adapted various open-source tools and modified the output format to make it better for my testing purposes. Here's what I added:

- Subdomain enumeration using Subfinder
- Directory brute-forcing for potential vulnerabilities
- SSL/TLS checks

---

## Installation

To install this tool, clone the repository using the following command:

```bash
git clone https://github.com/ctf678/Bug-Hunting-Tool.git

Then, install dependencies (if any) using:
pip install -r requirements.txt

Usage:
To run the tool, use the following command:
python3 subdomain_finder.py
Enter the target domain when prompted, and the tool will begin scanning for subdomains and
vulnerabilities.


 ## License:

This project is licensed under the MIT License - see the LICENSE file for details.

### Key Points:
1. **Title**: Use `#` for the main title (Bug-Hunting-Tool).
2. **Sections**: Separate each section using `---` (for example, after the "Changes" section).
3. **Code**: Enclose commands and code snippets in triple backticks (```bash or ```python),
 and for inline code use single backticks (`).
4. **Bullet Points**: For lists like "Changes", use `-` for each point.
5. **Links**: You can add external links like your "contact" link using markdown syntax `
[alt text](link)`.

With this structure, you will get a neat and easy-to-read `README.md` file with all the




## ---

## Created By

Parikshit Singh - Creator of this Bug-Hunting-Tool. 


## If you have any questions or need help, feel free to open an issue in this repository
or ping me via [Discord](https://discord.gg/tzfCpFFF).


python3 opendoor.py \
  --host https://syncvibe.xr.com \
  --scan directories \
  --wordlist /path/to/your/wordlist.txt \
  --extensions php,html,txt,json,xml,bak,old,backup,zip,tar,gz,pem,key \
  --recursive \
  --recursive-depth 4 \
  --recursive-status 200,301,302,307,308,401,403 \
  --threads 30 \
  --timeout 15 \
  --retries 2 \
  --keep-alive \
  --follow-redirects \
  --accept-cookies \
  --auto-calibrate \
  --calibration-samples 8 \
  --fingerprint \
  --waf-detect \
  --waf-safe-mode \
  --sniff endpoint,secret,file,indexof,shadow \
  --include-status 200-399,401,403 \
  --random-agent \
  --crawl \
  --reports json,txt,html \
  --reports-dir ./reports

-----------------------------------------------------------------------------------------------------------------------------



TARGET:
syncvibe.xr.com

IMPORTANT:
- Work only against the authorized CPENT lab target.
- Do not start with complicated exploitation.
- These challenges strongly suggest that the required information is available through files, backups, archives, or exposed web directories.
- Record every useful directory/file you discover.
- Do not guess the final answers. Extract them from the evidence.

============================================================
CHALLENGE 48 — MARIA'S REGION
============================================================

QUESTION:
Identify Maria's Region from:

TKT-TKT-004_Emergency_Staging.md

on syncvibe.xr.com.

The answer format is:

Xxxxx XxxXx


STEP 1 — RESOLVE THE HOST
-------------------------

Run:

nslookup syncvibe.xr.com

Also:

dig syncvibe.xr.com


STEP 2 — CHECK HTTP/HTTPS
-------------------------

Run:

curl -I http://syncvibe.xr.com

Then:

curl -I https://syncvibe.xr.com

If HTTPS gives certificate problems, try:

curl -k -I https://syncvibe.xr.com


STEP 3 — CHECK ROBOTS AND SITEMAP
---------------------------------

Run:

curl -s http://syncvibe.xr.com/robots.txt

curl -s http://syncvibe.xr.com/sitemap.xml

If HTTPS is being used:

curl -sk https://syncvibe.xr.com/robots.txt

curl -sk https://syncvibe.xr.com/sitemap.xml


Look for references to directories such as:

backup
backups
files
documents
docs
uploads
downloads
archive
archives
staging
reports
incident
ssh
keys


STEP 4 — DIRECTORY ENUMERATION
------------------------------

Run:

ffuf -u http://syncvibe.xr.com/FUZZ -w /usr/share/wordlists/dirb/common.txt

If HTTPS:

ffuf -k -u https://syncvibe.xr.com/FUZZ -w /usr/share/wordlists/dirb/common.txt


If that wordlist does not exist, check:

ls /usr/share/wordlists/

and:

find /usr/share/wordlists -type f | head -30


Pay special attention to:

/backup
/backups
/files
/docs
/documents
/uploads
/downloads
/archive
/archives
/staging
/reports
/incident
/ssh
/keys


STEP 5 — TRY THE KNOWN FILE DIRECTLY
------------------------------------

Because the filename is already known, try:

curl -s http://syncvibe.xr.com/TKT-TKT-004_Emergency_Staging.md

Then try likely directories:

curl -s http://syncvibe.xr.com/docs/TKT-TKT-004_Emergency_Staging.md

curl -s http://syncvibe.xr.com/files/TKT-TKT-004_Emergency_Staging.md

curl -s http://syncvibe.xr.com/backup/TKT-TKT-004_Emergency_Staging.md

curl -s http://syncvibe.xr.com/backups/TKT-TKT-004_Emergency_Staging.md

curl -s http://syncvibe.xr.com/uploads/TKT-TKT-004_Emergency_Staging.md

curl -s http://syncvibe.xr.com/staging/TKT-TKT-004_Emergency_Staging.md

curl -s http://syncvibe.xr.com/reports/TKT-TKT-004_Emergency_Staging.md


If HTTPS:

curl -sk https://syncvibe.xr.com/<PATH>/TKT-TKT-004_Emergency_Staging.md


Replace <PATH> with the directory you discover.


STEP 6 — SEARCH DOWNLOADED CONTENT
----------------------------------

If you have downloaded the website/files:

find . -type f -iname '*TKT*TKT*004*'

Also:

find . -type f | grep -Ei 'TKT|Emergency|Staging'


STEP 7 — READ THE FILE
----------------------

Once you find it:

cat TKT-TKT-004_Emergency_Staging.md

or:

less TKT-TKT-004_Emergency_Staging.md


Search directly for Maria:

grep -ni "Maria" TKT-TKT-004_Emergency_Staging.md

Also:

grep -niE "Maria|Region" TKT-TKT-004_Emergency_Staging.md


WHAT YOU NEED:
Find the entry for Maria and identify her Region.

DO NOT submit:
- Maria's name
- the whole sentence
- the field name "Region"

Submit ONLY the region value.

Check capitalization carefully.


============================================================
CHALLENGE 49 — KWAME'S SECURITY PASSPHRASE
============================================================

QUESTION:

Identify the security passphrase associated with user:

kwame

from SSH key backups stored on syncvibe.xr.com.

Then submit the LAST 5 CHARACTERS.

Answer format:

NxXxx


STEP 1 — LOOK FOR BACKUP DIRECTORIES
------------------------------------

Run:

ffuf -u http://syncvibe.xr.com/FUZZ -w /usr/share/wordlists/dirb/common.txt

Look especially for:

backup
backups
ssh
keys
ssh-backups
archive
archives
old
config
files


STEP 2 — ENUMERATE DISCOVERED DIRECTORIES
-----------------------------------------

If you discover something like:

/backup/

then enumerate it:

ffuf -u http://syncvibe.xr.com/backup/FUZZ -w /usr/share/wordlists/dirb/common.txt


Do the same for:

/backups/
/ssh/
/keys/
/archive/
/archives/
/old/
/files/


STEP 3 — SEARCH FOR SSH/KEY FILES
----------------------------------

If files have been downloaded:

find . -type f | grep -Ei 'ssh|key|backup|kwame'

Also:

find . -type f | grep -Ei '\.pem$|\.key$|id_rsa|authorized_keys|known_hosts'


STEP 4 — SEARCH FOR KWAME
-------------------------

This is VERY important.

Run:

grep -Rni "kwame" .

Then:

grep -RniE "kwame|passphrase|password|ssh" .


If you find a directory containing backup files:

grep -Rni "kwame" <directory>/

Then:

grep -RniE "passphrase|password" <directory>/


The challenge says:

"security passphrase associated with user kwame"

So do NOT simply take the first passphrase you find.

Make sure the passphrase belongs to KWAME.


STEP 5 — IF YOU FIND A ZIP ARCHIVE
----------------------------------

First inspect it:

unzip -l <archive>.zip


Do not immediately assume the archive contains the answer.

Then extract:

mkdir extracted

unzip <archive>.zip -d extracted


Search:

grep -Rni "kwame" extracted/

and:

grep -RniE "passphrase|password|ssh" extracted/


STEP 6 — IF YOU FIND SSH PRIVATE KEYS
-------------------------------------

Inspect the file:

file <keyfile>

head -n 5 <keyfile>


Search surrounding files for:

grep -Rni "kwame" .

Do not assume every SSH key belongs to kwame.


STEP 7 — EXTRACT THE LAST FIVE CHARACTERS
-----------------------------------------

Once the EXACT security passphrase for kwame is known:

echo -n 'ACTUAL_PASSPHRASE' | tail -c 5


OR:

python3 -c "s='ACTUAL_PASSPHRASE'; print(s[-5:])"


For example, if the actual passphrase were:

AbC12xYz9Q

then:

s[-5:]

would produce:

Yz9Q

BUT COUNT CAREFULLY — the answer must contain exactly FIVE characters.

The example above is intentionally only demonstrating the method.


FINAL CHECK:
- Correct user = kwame
- Correct SSH backup
- Correct security passphrase
- Exactly LAST 5 characters
- Preserve uppercase/lowercase
- Do not include quotes
- Do not include spaces unless they are genuinely part of the final five characters


============================================================
CHALLENGE 50 — MASTER EMERGENCY SYSTEM OVERRIDE KEY
============================================================

QUESTION:

Identify:

incident_rep_master.zip

on syncvibe.xr.com.

Extract its contents.

Use the hint in:

Hint.txt

Then determine the FIRST FIVE CHARACTERS of:

MASTER EMERGENCY SYSTEM OVERRIDE KEY

Answer format:

XNxXN


STEP 1 — FIND THE ZIP
---------------------

Search the discovered directories for:

incident_rep_master.zip


Try likely locations:

curl -I http://syncvibe.xr.com/incident_rep_master.zip

curl -I http://syncvibe.xr.com/backup/incident_rep_master.zip

curl -I http://syncvibe.xr.com/backups/incident_rep_master.zip

curl -I http://syncvibe.xr.com/files/incident_rep_master.zip

curl -I http://syncvibe.xr.com/downloads/incident_rep_master.zip

curl -I http://syncvibe.xr.com/archives/incident_rep_master.zip

curl -I http://syncvibe.xr.com/incident/incident_rep_master.zip

curl -I http://syncvibe.xr.com/reports/incident_rep_master.zip


If you discover the exact URL:

wget http://syncvibe.xr.com/<PATH>/incident_rep_master.zip


For HTTPS:

wget --no-check-certificate https://syncvibe.xr.com/<PATH>/incident_rep_master.zip


STEP 2 — VERIFY THE ZIP
-----------------------

Run:

file incident_rep_master.zip


Then:

unzip -l incident_rep_master.zip


DO NOT immediately start guessing.

Look at all filenames inside the archive.


Especially look for:

Hint.txt
master
emergency
override
incident
report
key
config


STEP 3 — EXTRACT
-----------------

mkdir incident_master

unzip incident_rep_master.zip -d incident_master


Then:

find incident_master -type f -print


STEP 4 — FIND HINT.TXT
----------------------

Run:

find incident_master -iname 'Hint.txt' -print


If it is directly inside:

cat incident_master/Hint.txt


If it is somewhere else:

cat "<FULL_PATH_TO_HINT.TXT>"


IMPORTANT:

READ THE HINT FIRST.

The question explicitly tells you:

"use the hint provided in Hint.txt on the server"

So the hint is likely important for determining where/how to obtain the override key.


STEP 5 — SEARCH FOR THE KEY
---------------------------

First:

grep -Rni "MASTER EMERGENCY SYSTEM OVERRIDE KEY" incident_master/


If that doesn't return anything:

grep -Rni "EMERGENCY" incident_master/


Then:

grep -Rni "OVERRIDE" incident_master/


Then:

grep -Rni "MASTER" incident_master/


Then:

grep -Rni "KEY" incident_master/


Also:

grep -RniE "MASTER|EMERGENCY|OVERRIDE|KEY" incident_master/


STEP 6 — CHECK FILE TYPES
--------------------------

Run:

find incident_master -type f -exec file {} \;


If a suspicious file is binary, use:

strings <filename>


For example:

strings <filename> | grep -iE "master|emergency|override|key"


If necessary:

strings <filename> | less


STEP 7 — IDENTIFY THE ACTUAL KEY VALUE
--------------------------------------

You are looking for the VALUE associated with:

MASTER EMERGENCY SYSTEM OVERRIDE KEY

For example, suppose the evidence says:

MASTER EMERGENCY SYSTEM OVERRIDE KEY: A7xP9KLM123...

Then the answer would be:

A7xP9


NOT:

MASTE

NOT:

EMERG

NOT the complete key.


STEP 8 — TAKE FIRST FIVE CHARACTERS
-----------------------------------

Once the exact key is identified:

echo -n 'ACTUAL_OVERRIDE_KEY' | cut -c1-5


OR:

python3 -c "s='ACTUAL_OVERRIDE_KEY'; print(s[:5])"


Make sure the result contains exactly FIVE characters.


============================================================
USEFUL SEARCH COMMANDS
============================================================

If you have downloaded a large amount of content, these commands are extremely useful.


SEARCH FILENAMES:

find . -type f | grep -Ei 'TKT|Emergency|Staging|SSH|key|backup|kwame|incident|master|hint'


SEARCH FOR MARIA:

grep -Rni "Maria" .


SEARCH FOR KWAME:

grep -Rni "kwame" .


SEARCH FOR REGION:

grep -Rni "Region" .


SEARCH FOR PASSPHRASES:

grep -RniE "passphrase|password|security passphrase" .


SEARCH FOR OVERRIDE:

grep -RniE "override|emergency|master" .


SEARCH FOR THE EXACT CHALLENGE 50 PHRASE:

grep -Rni "MASTER EMERGENCY SYSTEM OVERRIDE KEY" .


FIND ZIP FILES:

find . -type f -iname '*.zip'


FIND SSH FILES:

find . -type f | grep -Ei 'ssh|id_rsa|\.pem$|\.key$'


FIND MARKDOWN FILES:

find . -type f -iname '*.md'


============================================================
IF FFUF RETURNS TOO MANY RESULTS
============================================================

First determine what a normal non-existent page looks like.

Run:

curl -i http://syncvibe.xr.com/this-page-definitely-does-not-exist-123456


Look at:

HTTP status
Content length
Response size


Then use ffuf filters if required.

For example, if the normal 404 has a particular response size:

ffuf -u http://syncvibe.xr.com/FUZZ \
     -w /usr/share/wordlists/dirb/common.txt \
     -fs <SIZE>


Replace <SIZE> with the normal 404 response size.


============================================================
IF A DIRECTORY IS FOUND
============================================================

Suppose ffuf discovers:

/backup/


Do NOT stop there.

Enumerate inside it:

ffuf -u http://syncvibe.xr.com/backup/FUZZ \
     -w /usr/share/wordlists/dirb/common.txt


If it discovers:

/backup/files/


Enumerate again:

ffuf -u http://syncvibe.xr.com/backup/files/FUZZ \
     -w /usr/share/wordlists/dirb/common.txt


The important principle is:

DISCOVER DIRECTORY
       ↓
ENUMERATE DIRECTORY
       ↓
FIND FILE
       ↓
DOWNLOAD/READ FILE
       ↓
SEARCH CONTENT
       ↓
EXTRACT REQUIRED VALUE


============================================================
IF THE FILE IS FOUND BUT HTTP DOWNLOAD FAILS
============================================================

First inspect headers:

curl -I http://syncvibe.xr.com/<PATH>/<FILE>


Try:

curl -v http://syncvibe.xr.com/<PATH>/<FILE>


If HTTPS:

curl -vk https://syncvibe.xr.com/<PATH>/<FILE>


If authentication is required, do not start guessing credentials.

Look at the discovered application/pages for the intended CPENT lab access mechanism.


============================================================
FINAL EXAM STRATEGY
============================================================

Do these in order:

1. Resolve:

nslookup syncvibe.xr.com


2. Identify HTTP/HTTPS:

curl -I http://syncvibe.xr.com
curl -I https://syncvibe.xr.com


3. Check:

curl -s http://syncvibe.xr.com/robots.txt
curl -s http://syncvibe.xr.com/sitemap.xml


4. Enumerate:

ffuf -u http://syncvibe.xr.com/FUZZ -w /usr/share/wordlists/dirb/common.txt


5. Find useful directories.

6. Enumerate those directories again.

7. Search specifically for:

TKT-TKT-004_Emergency_Staging.md
incident_rep_master.zip
SSH backups
kwame
Hint.txt


8. Challenge 48:

TKT-TKT-004_Emergency_Staging.md
        ↓
Maria
        ↓
Region
        ↓
SUBMIT REGION


9. Challenge 49:

SSH backup
        ↓
kwame
        ↓
security passphrase
        ↓
LAST 5 CHARACTERS
        ↓
SUBMIT


10. Challenge 50:

incident_rep_master.zip
        ↓
unzip
        ↓
Hint.txt
        ↓
follow hint
        ↓
MASTER EMERGENCY SYSTEM OVERRIDE KEY
        ↓
FIRST 5 CHARACTERS
        ↓
SUBMIT


============================================================
FINAL CHECK BEFORE SUBMITTING
============================================================

CHALLENGE 48:

[ ] Found the correct TKT-TKT-004_Emergency_Staging.md
[ ] Found Maria's entry
[ ] Identified Maria's Region
[ ] Only the Region is being submitted
[ ] Capitalization matches
[ ] Answer matches Xxxxx XxxXx


CHALLENGE 49:

[ ] Found SSH key backups
[ ] Confirmed the information belongs to kwame
[ ] Identified the security passphrase
[ ] Took exactly the LAST 5 characters
[ ] Case preserved
[ ] Answer matches NxXxx


CHALLENGE 50:

[ ] Found incident_rep_master.zip
[ ] Extracted it
[ ] Read Hint.txt
[ ] Followed the hint
[ ] Identified the actual MASTER EMERGENCY SYSTEM OVERRIDE KEY
[ ] Took exactly the FIRST 5 characters
[ ] Case/numbers preserved
[ ] Answer matches XNxXN


DO NOT GUESS THE ANSWERS.

The objective is to obtain the actual evidence from the CPENT lab server and then extract exactly the portion requested by the challenge.

