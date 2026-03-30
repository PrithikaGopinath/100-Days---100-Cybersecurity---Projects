# 🔎 OSINT — Open Source Intelligence

> **Domain:** OSINT (Open Source Intelligence)  
> **Difficulty:** Beginner → Intermediate  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is OSINT?

OSINT (Open Source Intelligence) is the collection and analysis of information from **publicly available sources** to produce actionable intelligence. In cybersecurity, OSINT is used by:

- **Attackers** — to gather information on targets before launching an attack
- **Defenders** — to understand their own exposure
- **Investigators** — to track threat actors or support incident response
- **Pen testers** — for reconnaissance during ethical hacking engagements

*If it's publicly available, it's fair game — and attackers will find it.*

---

## 🧱 Core Concepts

### 1. The Intelligence Cycle

```
  ┌─────────────┐
  │  Planning   │  ← Define what you need to find
  └──────┬──────┘
         ↓
  ┌─────────────┐
  │  Collection │  ← Gather raw data from sources
  └──────┬──────┘
         ↓
  ┌─────────────┐
  │  Processing │  ← Organize and filter data
  └──────┬──────┘
         ↓
  ┌─────────────┐
  │  Analysis   │  ← Draw conclusions, find patterns
  └──────┬──────┘
         ↓
  ┌─────────────┐
  │Dissemination│  ← Report and act on findings
  └─────────────┘
```

---

### 2. OSINT Sources

#### 🔹 People & Identity
- **Social media** — LinkedIn, Twitter/X, Instagram, Facebook
- **People search engines** — Pipl, Spokeo, WhitePages
- **Username search** — Sherlock, WhatsMyName
- **Email lookup** — Hunter.io, Phonebook.cz
- **Data breaches** — HaveIBeenPwned, DeHashed

#### 🔹 Organizations & Companies
- **Company websites** — About pages, team listings, tech stack clues
- **LinkedIn** — Org structure, employees, technologies used, hiring patterns
- **Whois records** — Domain registration info
- **Job listings** — Reveal internal technologies, infrastructure ("must know Kubernetes, CrowdStrike, Splunk")
- **Companies House / SEC** — Corporate filings, ownership

#### 🔹 Technical / Infrastructure
- **Shodan** — Search engine for internet-connected devices
- **Censys** — Similar to Shodan, more certificate-focused
- **DNS records** — MX, TXT, A, CNAME records reveal email provider, CDN, etc.
- **Certificate Transparency logs** — Enumerate subdomains via crt.sh
- **Archive.org** — Wayback Machine for old website versions
- **BuiltWith / Wappalyzer** — Technology fingerprinting

#### 🔹 Geolocation
- **Google Maps / Street View** — Image location verification
- **GeoGuessr techniques** — Road signs, license plates, terrain
- **Exif data** — GPS coordinates in photo metadata
- **IP geolocation** — Approximate location from IP address

---

### 3. Footprinting a Target (Pen Test Recon)

A structured OSINT approach during a pen test engagement:

#### Step 1: Passive DNS Enumeration
```bash
# Find subdomains via certificate transparency
curl "https://crt.sh/?q=%.example.com&output=json" | jq '.[].name_value'

# DNS lookup
dig example.com ANY
nslookup -type=MX example.com

# Reverse DNS
host 93.184.216.34
```

#### Step 2: WHOIS
```bash
whois example.com
# Returns: registrar, creation date, contact info (if not privacy-protected)
```

#### Step 3: Email Harvesting
```bash
# theHarvester - collects emails, subdomains, IPs
theHarvester -d example.com -b google,linkedin,bing -l 500
```

#### Step 4: Shodan Search
```
org:"Target Company Name"
ssl.cert.subject.cn:"example.com"
hostname:"example.com"
```

#### Step 5: Google Dorking (Advanced Google Queries)
```
site:example.com filetype:pdf
site:example.com inurl:admin
site:example.com intitle:"index of"
"@example.com" filetype:xls
"example.com" "password" filetype:txt
```

---

### 4. Google Dorking Cheat Sheet

| Operator      | Example                                | Effect                                    |
|---------------|----------------------------------------|-------------------------------------------|
| `site:`       | `site:gov.uk filetype:pdf`             | Limit to specific domain                  |
| `filetype:`   | `filetype:xlsx "confidential"`         | Find specific file types                  |
| `inurl:`      | `inurl:admin login`                    | URL must contain keyword                  |
| `intitle:`    | `intitle:"index of" "parent directory"`| Page title contains keyword               |
| `intext:`     | `intext:"password" site:pastebin.com`  | Page text contains keyword                |
| `cache:`      | `cache:example.com`                    | Google's cached version                   |
| `link:`       | `link:example.com`                     | Pages linking to domain                   |
| `""`          | `"John Smith" "example.com"`           | Exact phrase                              |
| `-`           | `site:example.com -www`                | Exclude term                              |

---

### 5. Social Media OSINT

#### LinkedIn
- Reveals: org hierarchy, employee names, job titles, tech stack (from job posts)
- Company page → "People" tab → browsing employees is OSINT
- Watch for: employees' side projects, open source contributions, GitHub accounts

#### Twitter / X
- Search: `from:username`, `to:username`, `(keyword) since:2023-01-01`
- Geotagged tweets can reveal physical locations
- Network analysis: who they follow, retweet, interact with

#### Instagram / Facebook
- Exif data (though most platforms strip this now)
- Background details in photos — location, infrastructure, schedules
- Social connections

---

### 6. Email OSINT

```
Identify email format:
- first.last@company.com
- f.last@company.com
- firstlast@company.com

Tools: Hunter.io, Phonebook.cz, VoilaNorbert

Verify email exists:
- SMTP enumeration (VRFY command)
- Email verification services

Check breach databases:
- HaveIBeenPwned (safe, privacy-respecting)
- DeHashed (more details, requires account)
```

---

### 7. Image OSINT (IMINT)

```bash
# Extract Exif metadata (GPS, device, timestamp)
exiftool photo.jpg

# Reverse image search
- Google Images (drag and drop)
- TinEye
- Yandex (often better for faces/locations)

# Geolocation from image content
- Look for: street signs, license plates, landmarks, shadows, vegetation
- Tools: Google Street View, Overpass Turbo, SunCalc (sun angle)
```

---

### 8. Shodan for OSINT

Shodan indexes internet-facing devices and their banners.

```
# Find all IPs for a company
org:"Company Name"

# Find exposed databases
port:27017 product:MongoDB
port:9200 product:Elasticsearch

# Find devices with specific certificate
ssl.cert.subject.cn:"target.com"

# Find login pages
http.title:"Login" org:"Target"
```

---

### 9. OSINT Framework

A great mental map of OSINT categories: [osintframework.com](https://osintframework.com/)

Categories include:
- Username → Email → Real Name → Phone → Location
- Domain → IP → Threat Intel → Social Networks
- Documents → Images → Videos → Dark Web

---

## 🛠️ Tools to Know

| Tool              | Purpose                                          |
|-------------------|--------------------------------------------------|
| Maltego           | Visual link analysis for OSINT                   |
| Shodan            | Search engine for exposed devices                |
| theHarvester      | Email, subdomain, IP harvesting                  |
| Recon-ng          | Web reconnaissance framework                     |
| Sherlock          | Username hunting across 300+ social networks     |
| SpiderFoot        | Automated OSINT collection                       |
| crt.sh            | Certificate transparency subdomain enum          |
| ExifTool          | Extract metadata from files                      |
| Wayback Machine   | Archive.org for old website versions             |
| Hunter.io         | Email address finder by domain                   |
| HaveIBeenPwned    | Check if emails appear in breach databases       |

---

## ⚖️ Ethics & Legality

OSINT is **legal** when gathering publicly available information. However:

- ✅ Gathering info on yourself or your own organization
- ✅ Authorized red team/pen test engagements
- ✅ Threat intelligence on known threat actors
- ❌ Stalking, harassment, or targeting individuals without consent
- ❌ Using OSINT findings to facilitate unauthorized access
- ❌ Using data aggregators to build profiles for harmful purposes

**Always stay within scope and follow responsible disclosure practices.**

---

## 📚 Key Terms Glossary

| Term          | Meaning                                                        |
|---------------|----------------------------------------------------------------|
| SIGINT        | Signals Intelligence (electronic communications)              |
| HUMINT        | Human Intelligence (from people)                              |
| GEOINT        | Geospatial Intelligence                                        |
| IMINT         | Imagery Intelligence                                           |
| IOC           | Indicator of Compromise — used in threat intelligence          |
| Dork          | A search query using advanced operators to find specific info  |
| Footprinting  | Mapping the digital footprint of a target                      |
| Recon         | Reconnaissance — the information gathering phase              |

---

## 🔗 Resources

- [OSINT Framework](https://osintframework.com/) ← Must bookmark
- [Trace Labs](https://www.tracelabs.org/) — OSINT CTFs for missing persons
- [Bellingcat](https://www.bellingcat.com/) — Investigative OSINT journalism
- [IntelTechniques by Michael Bazzell](https://inteltechniques.com/)
- [TryHackMe OSINT Path](https://tryhackme.com/)
- [Shodan](https://www.shodan.io/)

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*
