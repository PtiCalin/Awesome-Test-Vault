---
title: "Intro to IT Architecture"
created: 2025-04-30
type: note
tags: [note, "IT Architecture"]
parent: "IT Strategy"
children: []
---

# Intro to IT Architecture

This note explores the foundations of **IT Architecture** and how it guides technology direction within organisations.

## Role of IT Architecture

| Aspect | Purpose |
| --- | --- |
| Strategic alignment | Ensures technology capabilities map to business goals. |
| Decision support | Provides reference models that guide make‑or‑buy, cloud vs. on‑prem, and integration choices. |
| Risk management | Surfaces technical debt, security posture, and compliance gaps early. |
| Communication bridge | Gives execs a high‑level blueprint while offering engineers standards and patterns. |
| Governance | Establishes principles, guardrails, and review boards that keep projects consistent. |

**IT Architect roles** include Enterprise Architect (EA), Solution Architect (SA), Domain/Platform Architect, and Cloud/DevOps Architect. Each operates at a different zoom level but shares common modelling skills.

## Traditional vs Modern Architectures

| Dimension | Traditional (Pre‑cloud) | Modern (Cloud‑native) |
| --- | --- | --- |
| Hosting model | Monolithic apps on dedicated servers or VMs | Microservices, containers, serverless on public/private cloud |
| Delivery cadence | Quarterly/annual releases | Continuous delivery (CI/CD) |
| Scaling | Vertical (bigger hardware) | Horizontal (auto‑scale groups, Kubernetes) |
| Resilience | HA clusters, DR sites | Chaos engineering, multi‑AZ/region deployment |
| Security mindset | Perimeter (firewall, VPN) | Zero‑Trust, identity‑centric |
| Org size impact | Small orgs: ad‑hoc IT; Large: heavyweight governance | Small: pay‑as‑you‑go cloud; Large: hybrid/multi‑cloud, platform teams |

## Key Frameworks & Methodologies

| Framework | What it provides | Common use‑case |
| --- | --- | --- |
| TOGAF (The Open Group Architecture Framework) | ADM cycle, viewpoints, deliverables | Enterprise‑wide architecture practice |
| Zachman Framework | 6×6 matrix of perspectives (Who, What, How…) | Taxonomy / documentation checklist |
| Gartner Enterprise Architecture | Focus on business outcomes & pace‑layered approach | Align EA to digital‑business value |
| SAFe (Scaled Agile) Architecture | Architectural runway, enabler epics | Agile enterprises scaling DevOps |
| AWS Well‑Architected / Azure CAF / Google CAF | Cloud‑native pillars & best practices | Reviewing workloads on specific clouds |
| Domain‑Driven Design (DDD) | Bounded contexts, ubiquitous language | Microservice boundaries & data modelling |

Methodologies continue to evolve: **Waterfall ➜ Agile ➜ DevOps ➜ FinOps ➜ Platform Engineering**. Architects now embed themselves in cross‑functional product teams instead of producing ivory‑tower diagrams.

## Reducing Complexity

- **Standardisation** – Shared API contracts, coding conventions, container base images.
- **Consolidation** – Reduce duplicate services (e.g., one logging stack for all apps).
- **Reference architectures & templates** – Terraform modules, Helm charts, reusable CI pipelines.
- **Tech‑radar & rationalisation cycles** – Adopt/Trial/Assess/Hold categories to phase out legacy tech.
- **Automation & Infrastructure‑as‑Code** – Repeatable, audit‑friendly environment builds (Terraform, Pulumi, Bicep).

## Advances & Trends

| Trend | Architectural Impact |
| --- | --- |
| Hybrid & Multi‑Cloud | Workload portability; need for abstraction layers (K8s, service mesh). |
| Edge Computing | Push computation near data sources; patterns like IoT gateways, 5G MEC. |
| Microservices | Decompose monoliths, enable team autonomy; requires observability & service discovery. |
| Serverless | Event‑driven, pay‑per‑invoke; reduces ops overhead but adds cold‑start latency concerns. |
| Zero Trust Security | Identity‑aware proxies, micro‑segmentation, least‑privilege IAM. |
| AI/ML Integration | MLOps pipelines, feature stores, GPU scheduling, responsible‑AI guardrails. |
| Event Streaming (Kafka/Pulsar) | Async decoupling, real‑time analytics. |
| Platform Engineering | Internal Developer Platforms (IDPs) that productise infrastructure. |
| Sustainability/GreenOps | Carbon‑aware workload scheduling, right‑sizing resources. |

### Quick Reference Cheat‑Sheet

- **Architect levels**: Strategy (EA) → Portfolio (Domain) → Solution → Implementation
- **4+1 Views**: Logical • Development • Process • Physical • Scenarios
- **Cloud‑design tenets**: Resilience • Scalability • Observability • Security • Cost
- **Decision log**: ADR (Architecture Decision Record) for each significant choice
- **Tooling**: ArchiMate, C4 Model, PlantUML, draw.io, Lucidchart, Structurizr

### Learning Path Suggestions

- TOGAF® Essentials – free Open Group study materials.
- Hands‑on: Design a reference architecture for a simple e‑commerce stack using AWS services; map it to Well‑Architected lenses.
- Compare: Pick a legacy monolith and sketch an incremental migration to microservices with DDD.
- Practise ADRs: Log every major decision in your personal projects.
- Follow thought leaders: Gregor Hohpe (Architecture Elevator), Neal Ford (Evolutionary Arch).

---

Created for the Awesome Test Vault – bridges IT architecture principles with data‑research & analysis initiatives.
