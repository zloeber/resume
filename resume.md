# Zachary Loeber
Infrastructure Automation Engineer

zloeber@gmail.com | 630.730.1764 | https://blog.zacharyloeber.com
McFarland, Wisconsin, US

## Summary
Cloud Architect, DevOps Expert, Infrastructure Engineer, and AI Specialist experienced in automating, securing, and supporting business-critical systems

## Profiles
- X (Twitter) (zloeber): https://twitter.com/zloeber
- LinkedIn (zloeber): https://linkedin.com/in/zloeber
- GitHub (zloeber): https://github.com/zloeber

## Experience
### Principal Cloud Consultant, Delivery Team - SPR
Feb 2018 - Present
Cloud consultant architect responsible for automating and supporting cloud infrastructure and DevOps solutions for clients.
- Act as a technical lead for the delivery team.
- Thought leader for the team on cloud infrastructure, DevOps, and automation topics.
- Architect, automate, and support business critical solutions for clients.
- Provide in depth technical candidate interviews for hundreds of potential new hires.
- Author of numerous blogs across a wide range of technologies for the organization.

### Global Cloud and DevOps Engineer - SPR (Current Client)
Mar 2025 - Aug 2026
AWS Organizations, Control Tower, and Landing Zone architect and engineer. Design and implement a multi-account AWS environment for a global organization with over 20 accounts. Implement guardrails, security baselines, and account structure to support the organization's cloud strategy.
- Architected and built a full AI agent operations cockpit (the 'IT Operations Agent') — a metagit-based atlas, orchestration spine, and Taskfile-driven verb layer — giving both human operators and autonomous agents a shared, auditable interface into ~90 repos across ~40 AWS accounts.
- Designed a dual-mode agent access model (Operator vs. Sentinel) with a deterministic capability-probing preflight check, ensuring autonomous AI agents downgrade any risky write to a reviewable GitLab MR or queued approval rather than acting directly — closing the human-in-the-loop gap for unattended AI operations.
- Built an org-wide, read-only AWS query layer using Steampipe/Powerpipe fronted by a per-account read only role StackSet, letting a single SQL query fan out across the entire AWS organization for compliance benchmarking and fleet audits without granting any data-plane access (secrets, KMS, S3 object content excluded by policy).
- Implemented a GitOps-driven account lifecycle system (workload onboarding, permission-set authoring/assignment, patch policies, cross-account IAM, budget management) — each a discrete, agent- and human-usable skill/task that lands as a Terraform MR rather than a manual console change.
- Established an agent isolation doctrine for concurrent human/AI collaboration on the same GitLab project — dedicated agent-owned clones, one persistent per-day working branch, MR-on-signal (not auto-merge) — eliminating the recurring merge-conflict class caused by agents editing a human's live working tree.
- Stood up a CI/CD validation gate (secret scanning, lint, skill-schema, atlas, script index, task-naming convention checks) enforced on every merge request, catching both human and AI agent contributions before they land on main.
- Delegated infrastructure-as-code implementation work to Claude Code subagents with automatic routing based on target-repo agent-readiness (AGENTS.md/CLAUDE.md, local skills, MCP servers), improving delegated MR success rates over generic subagents lacking repo-local context.
- Used AI agents to run and document real cost/security audits — including an org-wide Fargate platform retirement exposure sweep and an AWS Savings Plan renewal assessment — publishing findings through automated docs pipelines (MkDocs + GitLab Pages).
- Built a knowledge ingestion and institutional-knowledge pipeline pulling Confluence spaces into a git-tracked, searchable knowledge base to ground AI agent responses in authoritative internal documentation rather than hallucinated context.
- Authored and maintain 30+ reusable operational skills (playbooks) for AI agents covering AWS account governance, Terraform authoring conventions, GitLab MR workflows, secrets handling (SecretZero), and DevOps task automation — turning tribal knowledge into executable, versioned procedure.
- Extended cross-account IAM automation with scoped, least-privilege assume-role patterns (explicit actions/ARNs, never wildcard) reused across DNS sync, backup, and audit use cases via a shared, locally-patched Terraform module.
- Introduced a compliance risk-tiering model (low/medium/high/critical) governing which AI-agent actions can proceed autonomously vs. require explicit human approval, formalizing safe autonomy boundaries for infrastructure automation.
- Designed and implemented a multi-account AWS environment using AWS Control Tower and Organizations to support the organization's global cloud strategy.
- Implemented guardrails and security baselines to ensure compliance with industry standards and best practices.
- Automated account provisioning and management using Infrastructure as Code (IaC) principles.
- Collaborated with cross-functional teams to ensure seamless integration of cloud services with existing on-premises infrastructure.
- Built SES email sending solution for the organization to support various business units' email needs.
- Provided training and documentation to internal teams on AWS best practices and governance.
- Authored terraform modules and shared GitLab CICD component libraries to support the organization's cloud infrastructure as code strategy.
- Developed GitOps approach for managing AWS account access and permissions using AWS SSO and IAM Identity Center.
- Developed several Python scripts to generate AWS documentation for internal teams.
- Implemented organizational logging and monitoring using AWS CloudTrail, Config, and CloudWatch to ensure visibility and compliance across all accounts.
- Created terraform provisioning process for various team's AWS workloads that automated the GitLab integrated CICD pipelines to deploy and manage resources in a consistent and repeatable manner.
- Employed AI to assist in the generation of terraform code and documentation to speed up the delivery of infrastructure as code solutions.
- Deployed FortiGate firewalls in AWS using terraform for the organization's secure network architecture and SDWAN initiative.
- Technical support for deployed EKS cluster issues and workloads.
- Implemented AWS Backup and DR strategies for critical workloads in the AWS environment.
- Commvault backup implementation and deployment in AWS using terraform to support the organization's data protection strategy for critical workloads.

### Principal Security Engineer, Privilege Access Management team - SPR (Northwestern Mutual)
Apr 2021 - Jan 2025
Design and deliver HashiCorp Vault platform as a service for internal development teams in the organization. Additionally automated identity and access management operational tasks and integrations. Designed and developed APIs to fulfill business requirements, and performed DevOps engineering for the privlege access management team.
- Spearheaded unified Vault platform as a service using an innovative 'Vault Unified Manifest' configuration as code based GitOps pipeline delivery architecture. This solution provides a centrally managed project for teams to easily deploy complex Vault requirements across 4 environments each containing several purpose driven provisioning pipelines. This versatile manifest consolidates up to 32 different touch points for developers into a single merge request driven system that services hundreds of teams and automatically generates then provisions thousands of terraform manifests.
- Developed multi-threaded Python application required to process Vault unified manifests and transform them into required terraform manifests using Jinja templates, jsonschema, click, and more.
- Constructed multiple Vault and AWS terraform modules for the Vault infrastructure and configuration as code pipelines.
- Introduced CI/CD pipelines for existing terraform modules to automatically lint, document, and publish new versions for use in the organization.
- Designed and implemented DynamoDB NoSQL schema for Vault state management used in API integrations with the platform.
- Programmed, automated, and delivered a containerized FastAPI REST API application with several dozen endpoints using schema driven development, OpenAPI, and DynamoDB (including all relevant CI/CD pipelines and Docker images)
- Collaborated with teams to architect automated integrations for Vault + Kubernetes + CSI driver used in several dozen on-premise and cloud based Kubernetes clusters via customized Helm charts and terraform pipelines.
- Worked on the design and delivery of secrets as a service via HashiCorp Vault in the organization including; Key/Value, AppRole, PKI, AWS, Azure AD, Gitlab, EC2 SSH, and Aurora database integrations.
- Authored Gitlab pipelines for Python, NodeJS, Terraform, Golang, Docker images, and Powershell modules.
- Worked with team to create PowerShell modules, supporting scripts, and CICD pipelines to unify the processing of inbound self service requests for Cyberark vaulted Active Directory based generic IDs.
- Authored Python application to centralize Slack notifications behind all Cyberark self service automation workflows.
- Authored first ServiceNow API integrated automation tasks for the team via a custom Python application that automates the daily application id integration synchronization process with on premise Domino database.
- Revamped the ReactJS application used for CyberArk self-service automation forms and added CI/CD pipelines to automate the build and delivery of the forms as a Gitlab identity integrated web application.
- Created infrastructure as code examples in Python and TypeScript using AWS CDK to further support the AWS Vault Lambda extension integration
- Developed AWS EC2 Vault Role integration with Vault for secrets for both Windows and Linux via automated Vault Agent service installations and dynamic configuration file generation.
- Redesign support portal to deliver a platform agnostic path of choices for the privilege access management team.

### Senior Consultant, DevOps & Cloud Team - SPR (HAVI)
Jan 2019 - Mar 2021
Devops engineer responsible for automating micro-services and cloud infrastructure deployments for the NextGen Spark driven streaming engine.
- Authored Terraform code to accommodate 7 different environments across 4 teams with varied requirements including; AKS multi-nodepool clusters, container registries, webapps, Azure networking, storage and more.
- Evaluated, absorbed, modified, or custom crafted dozens of helm charts to form several pillar technologies that comprised the foundation of the project engine. This includes; Elasticsearch/FluentBit/Kibana, Prometheus/Gafana/AlertManager, Confluent Kafka, Cassandra, Cert-manager, ingress, and more.
- Fortified existing pipelines by converting all classic release pipelines into pipeline as code and centralizing into version control.
- Rewrote Python deployment code for submitting Spark streaming jobs to Kubernetes to include logging, dry run, local launch scripts, a Makefile, and a requirements file.
- Constructed end to end CI/CD pipeline as code libraries in Azure Devops for new and existing project repositories.
- Administered Azure Devops project's pipelines, service connections, variable groups, and repositories.
- Created and added branch policies and PR code review gates to align with the development team’s chosen git branch methodology.
- Provided Azure support across multiple tenants for access, security, and resource deployments.
- Constructed a reusable project helm chart for use across several micro-service Kubernetes deployment pipelines.
- Updated all existing pipelines to source secrets from Azure Key Vault instead of plain text environment variables.
- Saved costs by eliminating several unused or unrealized PaaS and IaaS services and implementing services directly on Kubernetes
- Introduced per team Kubernetes clusters for deployments to eliminate reduce resource contention issues.
- Designed and applied multiple workload targeting (aka: multi-tenancy) of Kubernetes deployments across all key services to allow for side-by-side fan-out deployment of workloads to multiple environments across the same clusters.
- Acted as a technical escalation point and liaison for multiple offshore development teams.
- Improved observability, security, and stability in the Nextgen engine by maintaining detailed workbooks, diagrams, and continually introducing various technologies such as; Weavscope, Polaris, Kured, several Prometheus exporters, Alertmanager, MS Teams integration, and more.
- Introduced, configured, and deployed project critical technologies for horizontal pod autoscaling, nodepool workload steering, automatic keyvault secrets injection, and more.
- Eliminated outside dependencies by creating Dockerfiles and pipelines for base container images used in most project critical components.

### Senior Consultant, DevOps & Cloud Team - SPR (Nielsen)
Feb 2018 - Jan 2019
Design, implement, and support cloud based big data pipeline devops solutions. Automate and improve cloud deployments and workflows for financial and operational efficiency.
- Developed a Python solution for bridging and automating AWS elastic map reduce cluster deployments through Ansible Tower from an existing orchestration platform. Solution utilized jinja based email notifications, is entirely self-contained as a pip module, and vastly simplifies the process for several teams within the client organization.
- Took over and optimized the deployment pipeline for Cloudera Hadoop cluster deployments to AWS by eliminating complexities and refactoring most of the custom Python deployment code.
- Created a custom smoke test framework using bash and makefiles that reduced developer code deployment testing for spark jobs from 24 hours down to 90 minutes.
- Designed and developed Python solution for monitoring AWS instances and alerting on threshold limitations set on a per-environment/per-team basis.
- Optimized and automated the container image build process for a legacy Python/Cython application.
- Led multiple teams in mapping out and moving forward with CI/CD strategies for their applications.
- Analyzed existing cloud resource utilization for financial optimization opportunities and constructed strategies that saved upwards of 15k a month in average spend.
- Constructed a self-updating Jenkins deployment using declarative pipeline code that builds containers to automate consistent artifact bundling from multiple dependent project sources.
- Constructed and deployed Jenkins pipelines for Maven build workflows.
- Automated bootstrap of local maven encrypted credentials both on Windows (with PowerShell) and on Linux/Mac (with makefiles and bash).
- Automated Kubernetes cluster deployments to local workstations and AWS for automated micro-services application deployment testing.

### Senior Infrastructure and Cloud Manager (Promotion) - ISACA
Oct 2016 - Feb 2018
Technical leader for the IT organization. Manager for infrastructure, security, and service desk teams. Lead, design and implement cloud-based solutions for Office 365, Azure, and SaaS integrations. Optimize IT in the organization for operational excellence.
- Lead architect and technical implementation engineer for a data-center migration for all critical organization infrastructure into a collocation facility resulting in reduction of operational overhead from 7 down to 1 rack of equipment.
- Deployed and configured Azure advanced threat analytic services, multi-factor authentication, and workspace join capabilities among other things.
- Eliminated all 2003 servers by migrating or consolidating legacy services to new 2012 R2 servers or cloud based services.
- Migrated key business SQL clusters to supported shared back-end SAN storage.
- Implemented Jenkins for enterprise task scheduling and other scheduled automation tasks.
- Automated ADP user profile sync with Active Directory, Office 365, and third-party SaaS providers.
- Authored PowerShell scripts to integrate several external vendors with internal systems.
- Designed and deployed entire test, QA, and Stage environments for a major web project initiative.
- Spearheaded, planned, and delivered a cloud-based consolidated CDN solution for all online organization assets. The forward designed solution provides guaranteed DDOS protection, flexible web application firewall capability, eliminates network complexity, saves approximately 60K a year, and provides a framework for future cloud efforts.
- Acted as a primary architect and engineer for infrastructure in the deployment of a major line of business cross premise e-commerce solution including isolated testing, staging, and production environments.
- Migrated outdated and unsupported on-premise PBX to Office 365 Cloud PBX with Skype for Business Online.
- Acted as a lead database administrator for business-critical SQL servers implementing backup and maintenance jobs, tightening security by roles, and enabling the database team to proactively monitor/manage systems with least privilege access.
- Upgraded entire organization from Windows 7 and Office 2010 to Windows 10 and Office 2016.
- Rapidly configured and brought online an office addition to facilitate an entirely new customer experience center.
- Setup, tested, and made available BitLocker drive encryption for the organization's sensitive laptops.
- Upgraded and rectified Veeam backups to an upgraded Dell EqualLogic storage array for backups.
- Ran regular cross-training sessions to increase operational awareness and knowledge between different IT departments.
- Provided leadership and mentoring to direct reports with transparent goals and regular open discussions to foster teamwork and collaborative spirit within the department.

### Senior Solutions Engineer - PSC Group
Dec 2013 - Dec 2015
Senior technical resource and advocate for Microsoft infrastructure technologies including Exchange, Lync, ADFS, Hyper-V, and Active Directory
- Assess, plan, design, and deploy Lync and Exchange 2013 through all phases of the project to replace existing aging telephony solutions.
- Assess and resolve existing Lync federation and deployment issues.
- Collaborate with AT&T and other PSTN providers to gather information required for Lync 2013 PBX replacement projects.
- Configure and deploy Sonus/Audiocodes PSTN gateways with SIP trunk providers or PSTN providers for highly available Lync 2013 voice deployments.
- Configure and deploy Audiocodes Mediant PSTN gateways with Lync SBA
- Perform Active Directory, Lync, and Exchange health assessments to provide tangible reports and next step solutions for issue remediation.
- Perform ADFS design and deployments for both hybrid cloud integration and for publishing content to federated external partners.
- Assessed and resolved Hyper-V 2012 R2 farm and cluster issues to stabilize infrastructure for Lync 2013 voice deployment.
- Provided direct impact to the business bottom line by bringing in new clients or solidifying relationships with new clients.
- Led open forum technical presentations at company meetings detailing prior successful Lync deployments
- Mentored new employees to the department to ease the on-boarding process and increase retention.
- Provided a plethora of technical interviews for both my group and for clients as required.
- Create PowerShell utilities, Excel checklists, and Word admin guide templates to assist in all phases of client engagements.

### Infrastructure Technical Engineer - Dyson
Dec 2012 - Dec 2013
Perform in a lead technical role for the infrastructure design, troubleshooting, and deployment for all company offices in North America.

### Senior Consultant - Peters & Associates
Oct 2011 - Dec 2012
Act as technical expert for Cisco, VMware, Active Directory, Lync, and Exchange infrastructure issues, upgrades, and deployments. Assess current IT environments for performance, security, and best practices. Lead engineer in forklift upgrades of Cisco/Microsoft environments.

### System Engineer/Architect/Administrator - Acxiom
May 2011 - Sep 2011
Scope out, architect, and build Exchange 2010 infrastructures for Exchange 2003 migrations both internally and for multiple clients. Install, configure, and support Exchange 2003/2010, Lync 2010, OCS, TMG, and Compliance servers with high availability in mind. Provide level three support for organization as needed.

### Network Infrastructure/Security Analyst II - Cision
Oct 2008 - Apr 2011
Optimize, build, secure, and maintain the North America infrastructure and server environments. Ensure maximum uptime of all production systems and sites. Research, architect, and deploy new infrastructure environments to increase productivity and cohesiveness across all departments. Upgrade existing environments to add high availability and reduce downtime. Automate and organize internal business processes and systems monitoring to optimize infrastructure operations. Act as a lead technical expert for helpdesk and other IT departments as required.

### System Administrator - Kone Elevator
Apr 2008 - Oct 2008
Act as primary point of support for the local and international VIP corporate users of the company at a new main corporate headquarters.

### Sr. Network and System Administrator - Healthcare Associates Credit Union
Jul 2006 - Apr 2008
Upgrade, maintain, and monitor network infrastructure and company servers. Ensure maximum uptime of all systems and the reliability of end user workstations. Implement security software and practices to guard company assets.

### Senior Technical Analyst - Adesso Solutions
Jul 2005 - Jul 2006
Provided database and high-level technical support for both clients and internal staff. Assisted in the hand-holding and implementation of new clients to the Adesso hosted trade and asset management solution. Provided maintenance and support for the production-hosting environment.

### Tier 2 Network/Application Analyst - Thomson NETg
Jul 2004 - Jul 2005
Performed in a pivotal position to prevent further escalation to on site engineers for client critical issues. Assisted management and first level support with advanced technical issues.

### Product Support Specialist - Visibillity
Jun 2003 - Jul 2004
Provided phone and e-mail support for a collaborative and interactive online system for more than 1000 law firms and several insurance companies.

### Tier 1 Technical Analyst - Robert Half Technology
Jul 2002 - Jun 2003
Provided phone and e-mail support for over 12 unique computer learning products including, but not limited to, java-based Internet browser playable courses. Supported over 600 unique businesses and universities.

### Senior Lab Coordinator - OnIT Consulting
Dec 2000 - Apr 2002
Managed the operation and system administration of technical training facilities within three cities. Designed and instructed A+, Network+, and MCSE 2000 courses. Provided network support for remote clients of the company engineering department.

### Account Support Representative/Programmer - Xerox Business Services
Dec 1999 - Dec 2000
Learn and support the roles of employees at all remote sites to fulfill customer SLAs when filling in for staff when they are absent from work. Program C++ solutions to meet client needs.

## Education
### College of DuPage | Associate - General Studies
Jan 2000 - Jan 2018
https://www.cod.edu/

## Skills
- **Cloud Infrastructure (Expert)**
  Azure, AWS, Terraform, Ansible, DynamoDB, EC2, Python, AKS, Docker, Azure Key Vault, boto3
- **Identity & Access Management (Expert)**
  HashiCorp Vault, CyberArk, AWS IAM, Azure AD, AppRole, PKI, SSO, MFA
- **Security (Expert)**
  Azure Security, AWS Security, HashiCorp Vault, CyberArk
- **Software Development & Scripting (Intermediate)**
  Python, PowerShell, dotnet, JavaScript, NodeJS, Jinja, bash, Makefile
- **DevOps (Expert)**
  CICD, GitHub, Azure Devops, Jenkins, GitLab, SemVer, git, Docker, workflow automation
- **Development (Intermediate)**
  HTML, CSS, JavaScript, React, NodeJS, ExpressJS, FastAPI, OpenAPI, Vite, AI
- **Automation**
  Powershell, Python, Terraform, Ansible, Third Party API Integration, CI/CD Pipelines, GitOps

## Certificates
- Certified AI Practitioner - AWS (Mar 2025)
  https://www.credly.com/badges/14230421-69a8-41b2-98f1-e538ee926379/public_url
- CCNA Routing and Switching - Cisco (Jan 2008)
  https://www.credly.com/badges/82f377c6-d4b4-42e5-8ac4-7d4092d81d0c/public_url
- Certified Kubernetes Administrator - The Linux Foundation (May 2023)
  https://www.credly.com/badges/3793ece1-4fde-4d32-a1b6-5538e507581d/public_url
- Certified Cloud Practitioner - AWS (Mar 2024)
  https://www.credly.com/badges/7a3c7a3c-0689-4d0e-8d4e-d5e4f8f8441b/public_url
- Vault Associate - HashiCorp (Sep 2023)
  https://www.credly.com/badges/255e6ebe-b920-4f53-8698-a995228525d6/public_url
- Terraform Associate - HashiCorp (May 2020)
  https://www.credly.com/badges/21434533-4064-44c7-85b3-e2b68827497c/public_url
- Gold MSDN and TechNet Galleries contributor - Microsoft (Jan 2024)
  https://learn.microsoft.com/api/achievements/share/en-us/zloeber/ZP3L4TM2?sharingId=E718E81B956EDD5B
- Certified Professional - Microsoft (May 2014)
- Solutions Associate: Windows Server 2008 - Microsoft (Apr 2012)
- A+ - CompTIA (Jan 2000)
- Network+ - CompTIA (Jan 2000)
- I-Net+ - CompTIA (Jan 2000)
- A+ - CompTIA (Jan 2000)
- MCSE NT 4.0 - Microsoft (Jan 2000)
- MCSE 2000 - Microsoft (Jan 2001)

## Projects
- **Prepper Guides**
  Planning for disasters based on your location and threat profile.
  https://www.prepper-guides.com
- **Terraform-Ingest**
  A terraform module ingestion CLI tool and MCP server that can read terraform code and supercharge your infrastructure as code efforts with AI assistance.
  https://github.com/zloeber/terraform-ingest
- **Metagit**
  A situational awareness for your git projects. Metagit makes sprawling multi-repo projects feel like monorepos and provides concise information on the software stacks, generated artifacts, dependencies, and more.
  https://github.com/metagit-ai/metagit-cli
- **Public PowerShell Collection**
  A large collection of PowerShell scripts and modules for public use. This collection is used by quite a few people it seems.
  https://github.com/zloeber/Powershell
- **PSAD Module**
  PowerShell AD Module for managing Active Directory via ADSI
  https://github.com/zloeber/PSAD

## Languages
- English - Native speaker

## Interests
- **AI**
  CoPilot, ChatGPT, Ollama, CrewAI, Agentic AI
- **Home Automation**
  Home Assistant, k3s, Frigate
- **Mischellaneous**
  PC Gaming, Rogue-likes, Blogging, Yo-yo, Tabletop Gaming

## References
- Provided: upon request
