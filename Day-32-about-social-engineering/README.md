# 🎭 Social Engineering

> **Domain:** Social Engineering  
> **Difficulty:** Beginner → Intermediate  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is Social Engineering?

Social Engineering is the art of manipulating people into divulging confidential information or performing actions that compromise security. It exploits human psychology rather than technical vulnerabilities. It's often said: *"The weakest link in any security system is the human."*

No matter how hardened the technology, if an employee can be tricked into handing over credentials or clicking a malicious link, the whole system falls.

---

## 🧱 Core Concepts

### 1. Why It Works — Psychological Principles

Attackers exploit well-documented psychological biases:

| Principle         | How Attackers Use It                                               |
|-------------------|--------------------------------------------------------------------|
| **Authority**     | "I'm the CEO / IT admin — do this now"                            |
| **Urgency**       | "Your account will be suspended in 24 hours!"                     |
| **Scarcity**      | "Only 2 spots left — act now"                                     |
| **Social Proof**  | "Everyone on your team has already done this"                      |
| **Reciprocity**   | Give something small to make victim feel obligated to help back   |
| **Liking**        | Attacker builds rapport before making the real request            |
| **Fear**          | "You've been hacked — verify your identity immediately"            |
| **Familiarity**   | Use victim's name, personal details to seem legitimate            |

---

### 2. Phishing

The most common social engineering attack. Attackers send fraudulent messages to steal credentials, install malware, or transfer money.

#### Types of Phishing

| Type               | Target       | Description                                                  |
|--------------------|--------------|--------------------------------------------------------------|
| **Phishing**       | Mass         | Generic emails sent to thousands                             |
| **Spear Phishing** | Individual   | Personalized email targeting a specific person               |
| **Whaling**        | Executives   | Spear phishing targeting C-suite (CEO, CFO)                  |
| **Vishing**        | Anyone       | Voice phishing — phone calls                                 |
| **Smishing**       | Anyone       | SMS phishing — text messages                                 |
| **Clone Phishing** | Prior victims| Duplicate a legitimate email, replace links with malicious ones|

#### Anatomy of a Phishing Email

```
From:    "IT Support" <it-support@company-secure.com>   ← Spoofed / look-alike domain
To:      victim@company.com
Subject: [URGENT] Your account will be locked in 2 hours

Hi John,                                                 ← Uses real name (harvested from LinkedIn)

We have detected unusual sign-in activity on your account.
Please verify your identity immediately:                 ← Urgency + fear

→ [Verify Account Now]                                  ← Malicious link

Failure to verify will result in account suspension.    ← Fear / threat

IT Security Team                                         ← Authority
```

#### Red Flags to Identify Phishing
- Sender domain doesn't match official domain
- Urgency or fear-inducing language
- Generic greetings ("Dear User")
- Requests for credentials or personal info
- Hover over link — URL doesn't match what's shown
- Unexpected attachments
- Poor grammar/spelling (though AI is making this less reliable)

---

### 3. Pretexting

Creating a fabricated scenario (pretext) to manipulate the target.

**Examples:**
- Impersonating IT support: "Hi, I'm from the helpdesk. We're doing a security audit and need to verify your password."
- Fake vendor: Calling accounts payable to change bank details for payment
- Fake survey: Collecting personal data under the guise of research

---

### 4. Baiting

Tempting victims with something desirable.

**Physical baiting:**
- USB drives labeled "Employee Salaries Q4" left in a car park → victim plugs it in
- Free software downloads that include malware

**Digital baiting:**
- "Download free software" that bundles malware
- Pirated content carrying malicious payloads

---

### 5. Quid Pro Quo

Offering a service in exchange for information.

**Example:**
- Attacker calls employees pretending to be IT support
- Offers to "fix a problem" (that doesn't exist)
- In exchange: "I just need to verify your credentials to log in and check"

---

### 6. Tailgating / Piggybacking (Physical)

Following an authorized person into a restricted area without proper authentication.

**Example:** Attacker carries boxes and waits near a secure door. An employee swipes in and holds the door — attacker walks straight in.

**Defense:** Mantraps, security awareness training, challenge unfamiliar faces politely.

---

### 7. Business Email Compromise (BEC)

A sophisticated phishing attack targeting businesses, often resulting in large financial losses.

**Common scenarios:**
- CEO Fraud: Attacker impersonates CEO, emails finance to urgently wire money
- Vendor Impersonation: Fake vendor email asking to update payment account details
- Employee Impersonation: HR email requesting W-2s or payroll redirection

**Why it's devastating:** No malware involved. Just manipulation. Hard to detect technically.

---

### 8. Vishing (Voice Phishing)

Phone-based attacks using social engineering.

**Example attack script:**
```
"Hello, this is Alex from Microsoft. We've detected a virus 
on your computer. I need you to install this tool so we 
can help you remotely."
```

**Common targets:**
- Elderly people (tech support scams)
- Employees (pretending to be IT, HR, executives)
- Banks (impersonating fraud departments)

---

### 9. The Attack Lifecycle (Social Engineering Kill Chain)

```
1. Reconnaissance  → Research the target (LinkedIn, website, social media)
2. Target Selection → Choose vulnerable individuals
3. Pretext Creation → Build convincing backstory
4. Execution       → Make contact and deliver the attack
5. Exploitation    → Victim complies — steal credentials, install malware, transfer money
6. Exit            → Disengage before victim suspects anything
```

---

### 10. OSINT in Social Engineering

Attackers use Open Source Intelligence to make attacks more convincing:
- LinkedIn → Org structure, job titles, project names, employee names
- Company website → Technology stack, partners, email format
- Social media → Personal details, relationships, recent events
- Data breaches → Old passwords, personal info for credential stuffing

---

## 🛡️ Defense and Awareness

### Technical Controls
- **Email filtering** — Block spoofed domains, scan attachments
- **SPF/DKIM/DMARC** — Email authentication standards
- **MFA everywhere** — Even if credentials are stolen, attacker can't log in
- **Zero trust** — Verify every request, every time
- **URL filtering** — Block known phishing domains

### Human Controls
- **Security awareness training** — Regular, scenario-based education
- **Phishing simulations** — Test employees, not to punish but to train
- **Clear verification procedures** — "Always call back on a known number before acting"
- **Report culture** — Make it easy and safe to report suspicious activity
- **No blame policy** — Victims of SE shouldn't fear punishment — encourages reporting

---

## 📚 Key Terms Glossary

| Term              | Meaning                                                          |
|-------------------|------------------------------------------------------------------|
| Pretext           | Fabricated scenario used to manipulate                          |
| Spear phishing    | Targeted phishing with personalized content                      |
| Whaling           | Phishing targeting executives                                    |
| BEC               | Business Email Compromise                                        |
| Vishing           | Voice phishing                                                   |
| Smishing          | SMS phishing                                                     |
| Tailgating        | Unauthorized physical entry by following authorized personnel    |
| Pretexting        | Impersonation using a fake identity/story                        |
| OSINT             | Open Source Intelligence gathering                               |

---

## 🔗 Resources

- [Social Engineering: The Art of Human Hacking (book)](https://www.wiley.com/en-gb/Social+Engineering%3A+The+Art+of+Human+Hacking-p-9780470639535)
- [The Social Engineering Framework](https://www.social-engineer.org/)
- [KnowBe4 Blog](https://blog.knowbe4.com/) — Security awareness content
- [Phishtool](https://www.phishtool.com/) — Phishing email analysis
- [Gophish](https://getgophish.com/) — Open-source phishing simulation framework

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*

