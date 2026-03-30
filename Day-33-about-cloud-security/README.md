# ☁️ Cloud Security

> **Domain:** Cloud Security  
> **Difficulty:** Intermediate → Advanced  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is Cloud Security?

Cloud Security is the set of practices, policies, and technologies that protect cloud-based systems, data, and infrastructure. As organizations move from on-premises to the cloud (AWS, Azure, GCP), the attack surface changes dramatically. Misconfigurations — not sophisticated exploits — are the #1 cause of cloud breaches.

---

## 🧱 Core Concepts

### 1. The Shared Responsibility Model

One of the most important concepts in cloud security. The cloud provider and customer *share* responsibility — but the split differs by service type.

```
                    Customer Responsibility ←───────────────────────────────
 ──────────────────────────────────────────────────────────────────────────
 IaaS (EC2/VMs)     OS, Runtime, App, Data, Identity, Network config
 PaaS (Lambda/App)  App, Data, Identity
 SaaS (Office365)   Data, Identity, Access management
 ──────────────────────────────────────────────────────────────────────────
                    ──────────────────────→ Provider Responsibility
```

**Bottom line:** The cloud provider secures *the cloud*. You secure *what's in the cloud*.

---

### 2. Cloud Service Models

| Model | Examples              | You manage                       |
|-------|-----------------------|----------------------------------|
| IaaS  | EC2, Azure VM, GCE    | OS, runtime, apps, data          |
| PaaS  | Heroku, App Engine    | Apps and data only               |
| SaaS  | Gmail, Salesforce     | Data and user access only        |
| FaaS  | Lambda, Cloud Functions | Code and triggers only          |

---

### 3. Common Cloud Misconfigurations

This is where most real-world cloud breaches come from.

| Misconfiguration              | Impact                                           |
|-------------------------------|--------------------------------------------------|
| Public S3 bucket              | Anyone can read/download all stored files        |
| Overly permissive IAM roles   | Attacker can escalate privileges across services |
| Exposed metadata endpoint     | EC2 metadata reveals IAM credentials             |
| Open security group (0.0.0.0) | All internet traffic can reach the instance      |
| No MFA on root/admin accounts | Single stolen password = full account takeover   |
| Unencrypted storage/databases | Data at rest is readable if accessed             |
| Publicly exposed Kubernetes dashboard | Full cluster takeover               |
| Hardcoded cloud keys in code  | Keys pushed to GitHub = immediate compromise     |

---

### 4. Identity and Access Management (IAM)

IAM is the core of cloud security. Getting it wrong is catastrophic.

**Principle of Least Privilege:** Give only the permissions needed — nothing more.

```json
// Bad - wildcard permissions
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}

// Good - specific permissions only
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::my-specific-bucket/*"
}
```

**Key IAM concepts:**

| Concept        | Description                                              |
|----------------|----------------------------------------------------------|
| User           | Individual identity with credentials                     |
| Role           | Assumed identity for services/applications               |
| Group          | Collection of users sharing policies                     |
| Policy         | JSON document defining permissions                       |
| MFA            | Multi-factor authentication — critical for all accounts  |
| SCP            | Service Control Policy — org-wide guardrails (AWS)       |

---

### 5. AWS-Specific Security Concepts

#### IMDS — Instance Metadata Service
EC2 instances can query their own metadata, including temporary IAM credentials.

```bash
# Accessible from inside the instance
curl http://169.254.169.254/latest/meta-data/

# Can return IAM credentials if role attached!
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

**Attack:** If SSRF exists in a web app running on EC2, attacker can steal IAM credentials.

**Defense:** Use IMDSv2 (requires token) — blocks SSRF-based metadata theft.

#### Key AWS Security Services

| Service        | Purpose                                                  |
|----------------|----------------------------------------------------------|
| IAM            | Identity and access management                           |
| CloudTrail     | Logs all API calls — your audit trail                    |
| GuardDuty      | Threat detection (anomaly + signature-based)             |
| Security Hub   | Unified security findings dashboard                      |
| Macie          | Data classification and PII detection in S3              |
| Config         | Tracks resource configuration changes                    |
| KMS            | Key Management Service — manage encryption keys          |
| WAF            | Web Application Firewall for CloudFront/ALB              |
| Inspector      | Vulnerability scanning for EC2 and containers            |
| Secrets Manager| Store and rotate credentials securely                    |

---

### 6. Container Security

Containers (Docker/Kubernetes) introduce new attack surfaces.

**Docker security basics:**
- Don't run containers as root
- Use official/verified base images
- Scan images for CVEs (Trivy, Snyk)
- Don't store secrets in Dockerfiles or ENV
- Use read-only filesystems where possible

```dockerfile
# Bad
FROM ubuntu:latest
RUN apt install everything
USER root

# Better  
FROM ubuntu:22.04@sha256:<digest>  # Pin version
USER 1000:1000                      # Non-root user
```

**Kubernetes security concerns:**
- Exposed dashboard (publicly accessible = full cluster access)
- Privileged pods (can escape to host)
- Secrets stored in plaintext in etcd
- No network policies (all pods can talk to all pods)
- Overly permissive RBAC

---

### 7. Data Security in the Cloud

| Control              | Description                                         |
|----------------------|-----------------------------------------------------|
| Encryption at rest   | Encrypt S3 objects, EBS volumes, RDS databases      |
| Encryption in transit| TLS for all data moving between services            |
| DLP                  | Data Loss Prevention — detect/prevent data exfil    |
| Backups              | Automated, tested, stored in separate account/region|
| Data classification  | Tag data by sensitivity (public, internal, secret)  |

---

### 8. Cloud Attack Techniques (MITRE ATT&CK Cloud)

| Technique                     | Description                                              |
|-------------------------------|----------------------------------------------------------|
| T1552.005 - Cloud Instance Metadata | Steal creds via metadata endpoint (SSRF)          |
| T1098.001 - Add Cloud Credentials | Attacker adds their own access keys to persist    |
| T1530 - Data from Cloud Storage | Exfiltrate data from S3, GCS, Azure Blob           |
| T1537 - Transfer to Cloud Account | Move data to attacker-controlled cloud account    |
| T1578 - Modify Cloud Compute Infrastructure | Spin up crypto miners, etc.            |

---

### 9. Cloud Security Best Practices

```
✅ Enable MFA on all accounts, especially root/admin
✅ Never use root account for day-to-day operations
✅ Apply least privilege to all IAM roles and users
✅ Enable CloudTrail / audit logging in all regions
✅ Encrypt all storage (S3, RDS, EBS) at rest
✅ Use IMDSv2 to block SSRF metadata attacks
✅ No public S3 buckets unless explicitly intended
✅ Rotate access keys regularly (or use roles instead)
✅ Never hardcode secrets in code or Dockerfiles
✅ Enable GuardDuty / Defender for Cloud
✅ Use VPCs with private subnets for sensitive resources
✅ Monitor for anomalous API calls and logins
```

---

## 🛠️ Tools to Know

| Tool           | Purpose                                              |
|----------------|------------------------------------------------------|
| ScoutSuite     | Multi-cloud security auditing                        |
| Prowler        | AWS security best practices auditor                  |
| Pacu           | AWS exploitation framework (like Metasploit for AWS) |
| CloudMapper    | AWS network visualization and auditing               |
| Trivy          | Container/image vulnerability scanner                |
| Checkov        | IaC security scanner (Terraform, CloudFormation)     |
| CloudTrail     | AWS native audit logging                             |
| Falco          | Runtime security for containers/Kubernetes           |

---

## 📚 Key Terms Glossary

| Term         | Meaning                                                       |
|--------------|---------------------------------------------------------------|
| Tenant       | An isolated customer environment in a cloud platform          |
| VPC          | Virtual Private Cloud — isolated network in AWS               |
| Security Group | Virtual firewall for cloud instances                       |
| NACL         | Network ACL — stateless subnet-level firewall in AWS          |
| Blob Storage | Azure's equivalent of S3                                      |
| CSPM         | Cloud Security Posture Management — detect misconfigs         |
| CWPP         | Cloud Workload Protection Platform                            |
| IaC          | Infrastructure as Code (Terraform, CloudFormation)            |

---

## 🔗 Resources

- [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) — Vulnerable AWS environment to practice on
- [flaws.cloud](http://flaws.cloud/) — AWS security challenges
- [flaws2.cloud](http://flaws2.cloud/) — Defender-perspective AWS challenges
- [AWS Security Docs](https://docs.aws.amazon.com/security/)
- [MITRE ATT&CK for Cloud](https://attack.mitre.org/matrices/enterprise/cloud/)
- [Cloud Security Alliance](https://cloudsecurityalliance.org/)

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*
