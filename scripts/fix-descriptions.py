#!/usr/bin/env python3
"""Fix duplicative skill descriptions and regenerate AGENTS.md catalogs.

Walks all 10 plugin dirs, finds every SKILL.md with the bad "Name — frameworks"
description pattern, and replaces it with a unique, actionable description from
a comprehensive dictionary. Then regenerates each plugin's AGENTS.md catalog.

Usage:
    python3 scripts/fix-descriptions.py              # Apply changes
    python3 scripts/fix-descriptions.py --dry-run     # Preview changes only
    python3 scripts/fix-descriptions.py --regen-only   # Only regenerate AGENTS.md
"""

import argparse
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLUGINS = ["ai", "code", "data", "design", "infra", "ops", "product", "research", "tools", "write"]

# ─────────────────────────────────────────────────────────────────────────────
# Comprehensive description dictionary: skill-name -> new description
# Each description starts with an action verb and describes what the skill does.
# Keyed by "plugin/skill-name" to handle name collisions across plugins.
# ─────────────────────────────────────────────────────────────────────────────

SKILL_DESCRIPTIONS = {
    # ── ai plugin ────────────────────────────────────────────────────────────
    "ai/agent-designer": "Design autonomous AI agent architectures, define tool-use patterns, plan multi-step reasoning chains, and orchestrate agent collaboration",
    "ai/audio-analyzer": "Analyze audio files for transcription, speaker identification, sentiment detection, and acoustic feature extraction",
    "ai/chain-designer": "Design LLM prompt chains, build sequential reasoning pipelines, and compose multi-step AI workflows with structured outputs",
    "ai/context-manager": "Optimize context window usage, implement retrieval strategies, manage token budgets, and design context-aware prompt systems",
    "ai/cost-optimizer": "Reduce AI inference costs through model selection, prompt optimization, caching strategies, and batch processing techniques",
    "ai/diagram-explainer": "Interpret and explain diagrams, flowcharts, architecture drawings, and visual documentation using vision models",
    "ai/document-scanner": "Extract structured data from scanned documents, forms, and handwritten text using OCR and vision models",
    "ai/embedding-specialist": "Build embedding pipelines, select embedding models, optimize vector representations, and design similarity search systems",
    "ai/error-handler": "Design error handling strategies for AI systems, manage hallucination detection, implement fallback chains, and build retry logic",
    "ai/fine-tuning-expert": "Fine-tune language models with custom datasets, configure training parameters, evaluate model performance, and manage training pipelines",
    "ai/image-analyzer": "Analyze images for object detection, classification, scene understanding, and visual question answering using vision models",
    "ai/llm-evaluation-expert": "Evaluate LLM outputs for quality, accuracy, and safety using automated benchmarks, human evaluation frameworks, and statistical analysis",
    "ai/llm-optimizer": "Optimize LLM inference speed and quality through quantization, distillation, prompt engineering, and serving configuration",
    "ai/memory-architect": "Design persistent memory systems for AI agents, implement conversation history management, and build knowledge graph integrations",
    "ai/monitoring-expert": "Monitor AI system performance, track model drift, set up alerting for quality degradation, and build observability dashboards",
    "ai/multi-agent-orchestrator": "Orchestrate multi-agent systems, design agent communication protocols, manage task delegation, and coordinate parallel agent execution",
    "ai/pdf-extractor": "Extract text, tables, images, and structured data from PDF documents using parsing libraries and vision models",
    "ai/prompt-engineer": "Craft effective prompts, design prompt templates, implement few-shot examples, and optimize prompt performance across LLM providers",
    "ai/prompt-template-designer": "Design reusable prompt templates with variable interpolation, conditional logic, and output format specifications",
    "ai/rag-system-architect": "Build retrieval-augmented generation systems, design document ingestion pipelines, implement hybrid search, and optimize retrieval quality",
    "ai/receipt-reader": "Extract line items, totals, dates, and vendor information from receipt images and scanned documents",
    "ai/routing-expert": "Design intelligent request routing for AI systems, implement model selection logic, and build load balancing for inference endpoints",
    "ai/safety-specialist": "Implement AI safety guardrails, content filtering, bias detection, output validation, and responsible AI practices",
    "ai/screenshot-reader": "Extract UI elements, text, layout structure, and interactive components from screenshot images",
    "ai/testing-specialist": "Test AI systems with evaluation suites, regression tests, adversarial inputs, and automated quality benchmarks",
    "ai/tool-builder": "Build function-calling tools for LLM agents, design tool schemas, implement tool execution logic, and manage tool registries",
    "ai/video-analyzer": "Analyze video content for scene detection, object tracking, temporal understanding, and frame-by-frame visual analysis",
    "ai/workflow-designer": "Design end-to-end AI workflows combining data ingestion, processing, inference, and output delivery with error handling",

    # ── code plugin ──────────────────────────────────────────────────────────
    "code/accessibility-expert": "Audit and fix mobile app accessibility for VoiceOver, TalkBack, dynamic type, and screen reader compatibility",
    "code/accessibility-specialist": "Implement WCAG-compliant web accessibility with ARIA attributes, keyboard navigation, focus management, and screen reader support",
    "code/accessibility-tester": "Write automated accessibility tests, audit WCAG compliance, and build CI checks for accessibility regressions",
    "code/ai-engineer": "Integrate AI models into production applications, build inference pipelines, manage model serving, and implement MLOps workflows",
    "code/analytics-expert": "Implement mobile analytics tracking, event instrumentation, user flow analysis, and crash reporting integration",
    "code/android-expert": "Build Android apps with Kotlin, Jetpack Compose, Material Design, lifecycle management, and Play Store deployment",
    "code/angular-architect": "Design Angular application architecture with modules, services, routing, RxJS state management, and lazy loading strategies",
    "code/animation-expert": "Build web animations with CSS transitions, Framer Motion, GSAP, requestAnimationFrame, and GPU-accelerated transforms",
    "code/api-architect": "Design RESTful and GraphQL API architectures, define resource models, plan versioning strategies, and implement authentication flows",
    "code/api-designer": "Design API contracts, write OpenAPI specifications, define request/response schemas, and establish API design standards",
    "code/api-designer-agent": "Collaboratively design API contracts through iterative refinement, generating OpenAPI specs and schema validation rules",
    "code/api-gateway-designer": "Design API gateway routing, rate limiting, authentication middleware, request transformation, and service mesh integration",
    "code/api-security-specialist": "Secure APIs with OAuth 2.0, JWT validation, rate limiting, input sanitization, and OWASP API security best practices",
    "code/api-testing-specialist": "Write API integration tests, contract tests, load tests, and automated regression suites for REST and GraphQL endpoints",
    "code/api-versioning-strategist": "Plan API versioning strategies, manage breaking changes, design deprecation policies, and implement backward compatibility",
    "code/app-store-expert": "Optimize App Store and Play Store listings, manage app review processes, handle release management, and improve store rankings",
    "code/architect": "Design software system architecture, evaluate trade-offs, create component diagrams, and plan scalable distributed systems",
    "code/architect-reviewer": "Review architecture decisions, critique design proposals, identify structural risks, and suggest architectural improvements",
    "code/auditor": "Audit codebases for security vulnerabilities, compliance violations, code quality issues, and technical debt",
    "code/authentication-architect": "Design authentication systems with OAuth 2.0, OIDC, SAML, multi-factor auth, session management, and token refresh flows",
    "code/auto-scaling-expert": "Configure auto-scaling policies, design capacity planning, implement horizontal pod autoscaling, and optimize resource utilization",
    "code/azure-infra-engineer": "Build Azure infrastructure with ARM templates, Azure DevOps pipelines, managed services, and hybrid cloud configurations",
    "code/backend-developer": "Build server-side applications with APIs, database integrations, authentication, background jobs, and error handling",
    "code/backend-performance-engineer": "Optimize backend performance through query tuning, caching, connection pooling, async processing, and profiling",
    "code/backend-security-expert": "Secure backend services against injection attacks, implement input validation, manage secrets, and enforce least-privilege access",
    "code/backend-testing-expert": "Write backend test suites including unit tests, integration tests, database tests, and API contract tests",
    "code/backup-architect": "Design backup and recovery strategies, implement point-in-time recovery, plan disaster recovery, and automate backup schedules",
    "code/blockchain-developer": "Build blockchain applications with Solidity smart contracts, Web3 integration, DeFi protocols, and on-chain data interaction",
    "code/bug-fixer": "Diagnose and fix bugs through systematic debugging, root cause analysis, log analysis, and targeted patch creation",
    "code/build-engineer": "Configure build systems, optimize CI/CD pipelines, manage build artifacts, and reduce build times across projects",
    "code/build-tool-expert": "Configure and optimize build tools like Webpack, Vite, esbuild, Rollup, and Turbopack for frontend projects",
    "code/bundler-expert": "Optimize JavaScript bundle sizes, configure code splitting, tree shaking, lazy loading, and module federation",
    "code/cache-strategist": "Design caching layers with Redis, Memcached, CDN caching, HTTP cache headers, and cache invalidation strategies",
    "code/caching-strategist": "Implement frontend caching with service workers, IndexedDB, localStorage, SWR/React Query, and offline-first patterns",
    "code/cdn-strategist": "Configure CDN distribution, edge caching, origin shielding, cache purging, and multi-region content delivery",
    "code/chaos-engineer": "Design chaos experiments, implement fault injection, test system resilience, and build automated recovery validation",
    "code/ci-testing-expert": "Set up CI test pipelines, parallelize test execution, manage flaky tests, and optimize test feedback loops",
    "code/cicd-architect": "Design CI/CD pipeline architectures, implement deployment strategies, configure build stages, and automate release workflows",
    "code/cli-developer": "Build command-line tools with argument parsing, interactive prompts, progress indicators, and cross-platform compatibility",
    "code/cloud-architect": "Design cloud-native architectures, select managed services, plan multi-region deployments, and optimize cloud costs",
    "code/cloud-security-expert": "Secure cloud infrastructure with IAM policies, network segmentation, encryption, compliance controls, and security monitoring",
    "code/code-explainer": "Explain complex code logic, trace execution flow, document algorithms, and create educational breakdowns of codebases",
    "code/code-reviewer": "Review code for correctness, performance, security, readability, and adherence to project conventions",
    "code/code-reviewer-agent": "Perform automated code reviews with structured feedback on style, logic, performance, and security concerns",
    "code/compliance-advisor": "Guide regulatory compliance for software systems including GDPR, HIPAA, SOC 2, PCI-DSS, and accessibility standards",
    "code/component-library-designer": "Design reusable component libraries with consistent APIs, theming support, accessibility, and documentation",
    "code/cpp-pro": "Write high-performance C++ code with modern standards (C++17/20/23), template metaprogramming, and memory-safe patterns",
    "code/cross-browser-tester": "Test and fix cross-browser compatibility issues across Chrome, Firefox, Safari, and Edge with polyfills and feature detection",
    "code/cross-platform-mobile-architect": "Design cross-platform mobile architectures with shared business logic, platform-specific UIs, and native module bridges",
    "code/csharp-developer": "Build C# applications with .NET, LINQ, Entity Framework, ASP.NET Core, and modern C# language features",
    "code/css-in-js-expert": "Implement CSS-in-JS solutions with styled-components, Emotion, Tailwind CSS, and optimize runtime styling performance",
    "code/css-specialist": "Write maintainable CSS with modern layout (Grid, Flexbox), custom properties, container queries, and responsive design",
    "code/csv": "Parse, transform, validate, and generate CSV data with proper escaping, encoding handling, and schema validation",
    "code/data-engineer": "Build data pipelines, design ETL workflows, implement data validation, and manage data warehouse schemas",
    "code/data-migration-specialist": "Plan and execute data migrations with schema transformations, rollback strategies, and data integrity validation",
    "code/database-administrator": "Manage database operations including backup, replication, user permissions, performance tuning, and capacity planning",
    "code/database-designer": "Design database schemas, normalize data models, plan indexing strategies, and define relationships and constraints",
    "code/database-optimizer": "Optimize database performance with query analysis, index tuning, execution plan review, and connection pool configuration",
    "code/database-replication-architect": "Design database replication topologies, configure read replicas, implement failover strategies, and manage data consistency",
    "code/debugger": "Debug application issues with breakpoint strategies, log analysis, memory profiling, and systematic issue isolation",
    "code/deployment-engineer": "Automate deployments with blue-green, canary, and rolling strategies using container orchestration and infrastructure as code",
    "code/devops-engineer": "Build DevOps infrastructure with CI/CD pipelines, container orchestration, monitoring, and infrastructure as code",
    "code/devops-incident-responder": "Handle production incidents with runbooks, root cause analysis, post-mortem documentation, and prevention measures",
    "code/disaster-recovery-planner": "Design disaster recovery plans with RPO/RTO targets, failover procedures, backup verification, and recovery testing",
    "code/django-developer": "Build Django applications with models, views, templates, REST framework, admin customization, and ORM optimization",
    "code/dns-expert": "Configure DNS records, troubleshoot resolution issues, plan DNS migration, and implement DNS-based load balancing",
    "code/docker-specialist": "Write Dockerfiles, configure multi-stage builds, optimize image sizes, manage Docker Compose, and troubleshoot containers",
    "code/documentation-writer": "Write clear technical documentation including API docs, architecture guides, runbooks, and onboarding materials",
    "code/documentation": "Generate and maintain code documentation with JSDoc, docstrings, README files, and inline comments",
    "code/dotnet-core-expert": "Build .NET Core applications with dependency injection, middleware pipelines, Entity Framework Core, and cross-platform deployment",
    "code/dotnet-framework-expert": "Maintain and modernize .NET Framework applications with WCF, WPF, ASP.NET WebForms, and migration planning to .NET Core",
    "code/dx-optimizer": "Improve developer experience with better tooling, faster feedback loops, clearer error messages, and streamlined workflows",
    "code/e2e-testing-specialist": "Write end-to-end tests with Playwright, Cypress, or Selenium covering user flows, visual regression, and cross-browser scenarios",
    "code/electron-pro": "Build cross-platform desktop apps with Electron, manage main/renderer processes, implement IPC, and optimize performance",
    "code/embedded-systems": "Program embedded systems with C/C++, configure peripherals, manage real-time constraints, and implement hardware interfaces",
    "code/encryption-specialist": "Implement encryption with AES, RSA, TLS configuration, key management, hashing, and secure data storage patterns",
    "code/error-detective": "Trace error origins through stack traces, logs, and system interactions to find root causes of production failures",
    "code/error-handling-expert": "Design error handling strategies with custom exceptions, retry policies, circuit breakers, and graceful degradation",
    "code/exploratory-tester": "Perform exploratory testing to discover edge cases, usability issues, and unexpected behaviors beyond scripted test cases",
    "code/fintech-engineer": "Build financial technology systems with payment processing, ledger management, regulatory compliance, and transaction safety",
    "code/flutter-expert": "Build Flutter apps with Dart, widget composition, state management (Riverpod/Bloc), platform channels, and responsive layouts",
    "code/forms-expert": "Build complex forms with validation, multi-step flows, dynamic fields, file uploads, and accessible error handling",
    "code/frontend-developer": "Build frontend applications with React, Vue, or vanilla JS, implement responsive layouts, and manage client-side state",
    "code/frontend-performance-expert": "Optimize frontend performance with code splitting, lazy loading, image optimization, Core Web Vitals, and rendering strategies",
    "code/frontend-security-expert": "Secure frontend applications against XSS, CSRF, clickjacking, and implement Content Security Policy and input sanitization",
    "code/frontend-testing-expert": "Write frontend tests with React Testing Library, Jest, Vitest, component snapshots, and interaction testing",
    "code/fullstack-developer": "Build full-stack applications connecting frontend UIs to backend APIs, databases, and authentication systems",
    "code/game-developer": "Build games with game loops, physics engines, sprite management, input handling, and cross-platform game frameworks",
    "code/gdpr-specialist": "Implement GDPR compliance with data subject rights, consent management, data processing agreements, and privacy by design",
    "code/gitops-specialist": "Implement GitOps workflows with Flux or ArgoCD, manage declarative infrastructure, and automate reconciliation loops",
    "code/golang-pro": "Write Go applications with goroutines, channels, interfaces, error handling patterns, and idiomatic Go project structure",
    "code/graphql-architect": "Design GraphQL schemas, implement resolvers, configure federation, manage subscriptions, and optimize query performance",
    "code/grpc-specialist": "Build gRPC services with Protocol Buffers, streaming RPCs, interceptors, load balancing, and cross-language client generation",
    "code/i18n-expert": "Implement internationalization with locale management, pluralization rules, RTL support, date/number formatting, and translation workflows",
    "code/identity-access-expert": "Design identity and access management with RBAC, ABAC, SCIM provisioning, directory integration, and SSO federation",
    "code/incident-responder": "Respond to production incidents with structured triage, communication templates, mitigation steps, and post-incident reviews",
    "code/infrastructure-compliance-expert": "Ensure infrastructure compliance with CIS benchmarks, SOC 2 controls, audit logging, and automated policy enforcement",
    "code/infrastructure-security-expert": "Secure infrastructure with network segmentation, firewall rules, bastion hosts, VPN configuration, and intrusion detection",
    "code/infrastructure-testing-expert": "Test infrastructure with Terratest, InSpec, ServerSpec, and automated compliance verification for IaC deployments",
    "code/ios-architect": "Design iOS app architectures with Swift, SwiftUI/UIKit, MVVM/TCA patterns, modularization, and dependency injection",
    "code/iot-engineer": "Build IoT systems with device protocols (MQTT, CoAP), edge computing, sensor data pipelines, and device management",
    "code/java-architect": "Design Java application architectures with Spring Boot, microservices patterns, JPA, messaging, and performance tuning",
    "code/javascript-pro": "Write modern JavaScript with ES2024+ features, async patterns, module systems, and browser/Node.js runtime optimization",
    "code/json": "Parse, transform, validate, and generate JSON data with schema validation, JQ-style queries, and format conversion",
    "code/kotlin-specialist": "Build Kotlin applications with coroutines, sealed classes, DSL builders, multiplatform projects, and Jetpack integration",
    "code/kubernetes-expert": "Deploy and manage Kubernetes clusters with Helm charts, operators, networking policies, and resource management",
    "code/kubernetes-specialist": "Configure Kubernetes workloads, debug pod issues, manage ConfigMaps/Secrets, and implement health checks and probes",
    "code/laravel-specialist": "Build Laravel applications with Eloquent ORM, Blade templates, queues, event broadcasting, and API resource controllers",
    "code/legacy-modernizer": "Plan and execute legacy code modernization with strangler fig patterns, incremental rewrites, and dependency upgrades",
    "code/llm-architect": "Design LLM-powered application architectures, plan inference infrastructure, implement caching, and manage model lifecycle",
    "code/load-balancer": "Configure load balancers with health checks, session affinity, SSL termination, and traffic distribution algorithms",
    "code/load-testing-expert": "Design and run load tests with k6, Locust, or JMeter to identify bottlenecks and validate performance requirements",
    "code/log-management-expert": "Design structured logging, configure log aggregation, build log-based alerting, and implement log retention policies",
    "code/m365-admin": "Manage Microsoft 365 administration with Exchange, SharePoint, Teams, Entra ID, and PowerShell automation",
    "code/machine-learning-engineer": "Build ML pipelines with feature engineering, model training, hyperparameter tuning, and production model serving",
    "code/mcp-developer": "Build Model Context Protocol servers and tools, implement resource providers, and integrate external services with LLM agents",
    "code/message-queue-architect": "Design message queue systems with RabbitMQ, Kafka, or SQS for event-driven architectures, pub/sub, and dead letter handling",
    "code/micro-frontend-architect": "Design micro-frontend architectures with module federation, shared dependencies, independent deployment, and routing strategies",
    "code/microservices-architect": "Design microservices architectures with service boundaries, inter-service communication, data consistency, and observability",
    "code/microservices-expert": "Build microservices with API gateways, service discovery, circuit breakers, distributed tracing, and contract testing",
    "code/mobile-app-developer": "Build native mobile apps for iOS and Android with platform-specific UI patterns, navigation, and device APIs",
    "code/mobile-developer": "Develop cross-platform mobile applications with shared codebases, native bridges, and platform-adaptive UI components",
    "code/mobile-devops-engineer": "Set up mobile CI/CD with automated builds, code signing, beta distribution, app store deployment, and crash monitoring",
    "code/mobile-performance-expert": "Optimize mobile app performance with memory profiling, startup time reduction, battery optimization, and network efficiency",
    "code/mobile-testing-expert": "Test mobile apps with XCTest, Espresso, Detox, or Appium covering device compatibility, gestures, and offline scenarios",
    "code/mobile-ui-designer": "Build mobile UI with native components, gesture interactions, adaptive layouts, and platform design guidelines (HIG/Material)",
    "code/monitoring-architect": "Design observability systems with metrics, traces, and logs using Prometheus, Grafana, Datadog, or OpenTelemetry",
    "code/monitoring-expert": "Implement application monitoring with custom metrics, SLI/SLO tracking, alerting rules, and performance dashboards",
    "code/monitoring-specialist": "Configure infrastructure monitoring with uptime checks, resource utilization alerts, and capacity trend analysis",
    "code/network-architect": "Design network architectures with VPCs, subnets, routing tables, peering, and hybrid connectivity solutions",
    "code/network-engineer": "Configure network infrastructure including firewalls, VPNs, DNS, load balancers, and troubleshoot connectivity issues",
    "code/nextjs-developer": "Build Next.js applications with App Router, Server Components, API routes, ISR, middleware, and deployment optimization",
    "code/nlp-engineer": "Build NLP pipelines with text classification, named entity recognition, sentiment analysis, and language model integration",
    "code/nosql-architect": "Design NoSQL data models for MongoDB, DynamoDB, Cassandra, or Redis with access patterns, indexing, and consistency trade-offs",
    "code/offline-expert": "Implement offline-first web apps with service workers, IndexedDB, background sync, and conflict resolution strategies",
    "code/orm-expert": "Configure and optimize ORMs like Prisma, SQLAlchemy, TypeORM, or Sequelize with migrations, relations, and query optimization",
    "code/payment-integration": "Integrate payment processors (Stripe, PayPal, Square), handle webhooks, manage subscriptions, and ensure PCI compliance",
    "code/penetration-tester": "Conduct authorized penetration testing, identify vulnerabilities, write exploit reports, and recommend remediation steps",
    "code/performance-engineer": "Profile and optimize application performance through benchmarking, bottleneck analysis, caching, and resource tuning",
    "code/performance-tester": "Design performance test suites, establish baselines, identify regressions, and validate throughput and latency requirements",
    "code/php-pro": "Write modern PHP with type safety, PSR standards, Composer packages, and framework-agnostic best practices",
    "code/platform-engineer": "Build internal developer platforms with self-service infrastructure, golden paths, and standardized deployment workflows",
    "code/postgres-pro": "Optimize PostgreSQL with advanced queries, partitioning, JSONB operations, extensions, replication, and performance tuning",
    "code/powershell-5-expert": "Write PowerShell 5.1 scripts for Windows automation, Active Directory management, and legacy system administration",
    "code/powershell-7-expert": "Build PowerShell 7 cross-platform scripts with modern cmdlets, parallel execution, and .NET interop capabilities",
    "code/powershell-module-architect": "Design PowerShell modules with proper manifests, exported functions, pipeline support, and Pester test suites",
    "code/powershell-ui-architect": "Build PowerShell-based UIs with WPF, Windows Forms, or terminal UI frameworks for admin tools and dashboards",
    "code/push-notification-expert": "Implement push notifications with APNs, FCM, web push, notification channels, and delivery tracking",
    "code/pwa-developer": "Build Progressive Web Apps with service workers, web manifests, offline caching, installability, and push notifications",
    "code/python-pro": "Write Pythonic code with type hints, async/await, virtual environments, packaging, and performance optimization",
    "code/qa-automation-expert": "Build QA automation frameworks with page objects, data-driven tests, parallel execution, and CI/CD integration",
    "code/qa-expert": "Design QA strategies with test plans, risk-based testing, defect triage, and quality metrics tracking",
    "code/rails-expert": "Build Ruby on Rails applications with ActiveRecord, ActionCable, Hotwire, background jobs, and RESTful conventions",
    "code/rate-limiting-expert": "Implement rate limiting with token buckets, sliding windows, distributed rate limiting, and client-specific throttling",
    "code/react-architect": "Design React application architectures with component patterns, state management, data fetching, and rendering optimization",
    "code/react-native-specialist": "Build React Native apps with native modules, navigation, platform-specific code, and bridge optimization",
    "code/react-specialist": "Build React components with hooks, context, suspense, server components, and modern React patterns",
    "code/readme": "Generate clear, comprehensive README files with setup instructions, API documentation, and usage examples",
    "code/refactor-assistant": "Refactor code for improved readability, reduced complexity, better naming, and cleaner architecture without changing behavior",
    "code/refactoring-expert": "Plan and execute large-scale refactoring with safe incremental steps, test coverage verification, and rollback strategies",
    "code/refactoring-specialist": "Apply refactoring patterns like extract method, replace conditional with polymorphism, and introduce parameter objects",
    "code/responsive-design-specialist": "Build responsive layouts with CSS Grid, Flexbox, media queries, container queries, and mobile-first design strategies",
    "code/router-designer": "Design client-side routing with nested routes, lazy loading, route guards, URL parameters, and navigation state management",
    "code/rust-engineer": "Write Rust applications with ownership, lifetimes, traits, async runtime, error handling, and zero-cost abstractions",
    "code/schema": "Design data schemas for databases, APIs, and config files with validation rules, versioning, and migration support",
    "code/search": "Implement search functionality with full-text search, faceted filtering, autocomplete, relevance tuning, and search analytics",
    "code/secrets-management-expert": "Manage secrets with HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault including rotation, access policies, and encryption",
    "code/security-code-reviewer": "Review code specifically for security vulnerabilities including injection, authentication flaws, and insecure data handling",
    "code/security-engineer": "Build secure applications with threat modeling, secure coding practices, dependency scanning, and security testing automation",
    "code/security-incident-responder": "Handle security incidents with forensic analysis, containment procedures, evidence preservation, and breach notification",
    "code/security-specialist": "Implement application security controls including input validation, output encoding, CSRF protection, and secure headers",
    "code/security-tester": "Write security tests for authentication bypasses, authorization flaws, injection vectors, and data exposure vulnerabilities",
    "code/seo-specialist": "Optimize web applications for search engines with meta tags, structured data, sitemap generation, and Core Web Vitals",
    "code/service-mesh-expert": "Configure service meshes with Istio or Linkerd for traffic management, mTLS, observability, and canary deployments",
    "code/software-developer": "Write clean, maintainable application code with SOLID principles, design patterns, and comprehensive test coverage",
    "code/spring-boot-engineer": "Build Spring Boot applications with dependency injection, data JPA, security, REST controllers, and actuator monitoring",
    "code/sql-optimization-specialist": "Optimize SQL queries with execution plan analysis, index strategy, query rewriting, and database-specific tuning",
    "code/sql-pro": "Write advanced SQL with window functions, CTEs, recursive queries, JSON operations, and cross-database compatibility",
    "code/sre-engineer": "Implement site reliability engineering with SLOs, error budgets, toil reduction, capacity planning, and incident management",
    "code/sre-specialist": "Build SRE tooling for automated remediation, runbook automation, chaos testing, and production readiness reviews",
    "code/state-management-architect": "Design frontend state management with Redux, Zustand, Jotai, or XState including normalized stores and side effect handling",
    "code/swift-expert": "Write Swift code with protocols, generics, concurrency (async/await), property wrappers, and SwiftUI/UIKit integration",
    "code/terraform-engineer": "Build Terraform infrastructure with modules, state management, workspace configuration, and multi-provider deployments",
    "code/terraform-expert": "Design Terraform architectures with remote backends, module composition, policy enforcement, and CI/CD pipeline integration",
    "code/test-architect": "Design test architectures with test pyramids, fixture strategies, test isolation, and cross-layer testing approaches",
    "code/test-automator": "Automate test execution with framework configuration, parallel runners, reporting, and CI/CD pipeline integration",
    "code/test-coverage-analyst": "Analyze test coverage gaps, identify critical untested paths, and design targeted tests to improve coverage quality",
    "code/test-data-manager": "Generate and manage test data with factories, fixtures, database seeders, and synthetic data generation",
    "code/test-writer": "Write unit tests, integration tests, and snapshot tests with proper assertions, mocking, and test organization",
    "code/testing-architect": "Design comprehensive testing strategies spanning unit, integration, end-to-end, and performance testing across the stack",
    "code/threat-modeling-expert": "Conduct threat modeling with STRIDE, attack trees, data flow diagrams, and security control recommendations",
    "code/tooling-engineer": "Build developer tools, code generators, linters, formatters, and IDE extensions to improve team productivity",
    "code/typescript-expert": "Design TypeScript type systems with generics, conditional types, mapped types, discriminated unions, and type inference",
    "code/typescript-pro": "Write TypeScript with strict mode, utility types, module declarations, and framework-specific type patterns",
    "code/ui-designer": "Build user interfaces with component design, layout systems, theming, responsive breakpoints, and design token integration",
    "code/visual-regression-tester": "Set up visual regression testing with screenshot comparison, pixel-diff thresholds, and cross-browser visual validation",
    "code/vue-expert": "Build Vue.js applications with Composition API, Pinia state management, Vue Router, and component design patterns",
    "code/vuejs-expert": "Design Vue.js architectures with Options/Composition API, Vuex/Pinia, SSR with Nuxt, and component library patterns",
    "code/vulnerability-management-expert": "Manage vulnerability lifecycle from scanning and triage to patching, with CVE tracking and remediation prioritization",
    "code/web-vitals-expert": "Optimize Core Web Vitals (LCP, FID, CLS) with performance budgets, measurement tools, and targeted improvements",
    "code/webgl-specialist": "Build WebGL/WebGPU graphics with shaders, 3D rendering, texture management, and performance optimization",
    "code/webhook-designer": "Design webhook systems with event schemas, delivery guarantees, retry logic, signature verification, and payload management",
    "code/websocket-engineer": "Build WebSocket services with connection management, heartbeat protocols, message framing, and scaling strategies",
    "code/windows-infra-admin": "Manage Windows Server infrastructure with Active Directory, Group Policy, WSUS, IIS, and PowerShell automation",
    "code/wordpress-master": "Build and customize WordPress sites with themes, plugins, custom post types, Gutenberg blocks, and WP-CLI management",
    "code/zero-trust-architect": "Design zero-trust security architectures with identity verification, micro-segmentation, continuous authentication, and least-privilege access",

    # ── data plugin ──────────────────────────────────────────────────────────
    "data/ab-testing-specialist": "Design and analyze A/B tests, calculate statistical significance, determine sample sizes, and interpret experiment results",
    "data/analyst": "Analyze datasets with statistical methods, identify patterns and trends, create visualizations, and deliver actionable insights",
    "data/analyst-agent": "Perform interactive data analysis with iterative exploration, hypothesis testing, and automated insight generation",
    "data/anomaly-detection-expert": "Build anomaly detection systems with statistical methods, isolation forests, autoencoders, and real-time alerting",
    "data/automl-specialist": "Configure AutoML pipelines for automated feature selection, model comparison, hyperparameter optimization, and ensemble creation",
    "data/causal-inference-analyst": "Conduct causal inference analysis with difference-in-differences, instrumental variables, propensity score matching, and regression discontinuity",
    "data/competitive-analyst-agent": "Analyze competitive landscapes with market positioning, feature comparison, pricing analysis, and strategic recommendations",
    "data/computer-vision-expert": "Build computer vision systems with image classification, object detection, segmentation, and video analysis pipelines",
    "data/deep-learning-expert": "Design deep learning architectures with CNNs, transformers, attention mechanisms, and training optimization techniques",
    "data/etl-pipeline-engineer": "Build ETL/ELT pipelines with data extraction, transformation logic, loading strategies, and pipeline orchestration",
    "data/feature-engineer": "Create predictive features through data transformation, aggregation, encoding, and automated feature selection techniques",
    "data/formatter": "Format and transform data between CSV, JSON, Parquet, and other formats with schema mapping and type conversion",
    "data/ml-engineer": "Build end-to-end machine learning systems from data preparation through model training, evaluation, and deployment",
    "data/ml-model-evaluation-expert": "Evaluate ML models with cross-validation, confusion matrices, ROC curves, bias analysis, and fairness metrics",
    "data/mlops-engineer": "Build MLOps infrastructure with model registries, experiment tracking, automated retraining, and deployment pipelines",
    "data/model-deployment-expert": "Deploy ML models with containerization, serving frameworks (TorchServe, TFServing), A/B testing, and canary rollouts",
    "data/model-interpretability-expert": "Explain ML model predictions with SHAP values, LIME, feature importance, partial dependence plots, and attention visualization",
    "data/nlp-specialist": "Build NLP systems for text classification, entity extraction, summarization, translation, and language understanding",
    "data/pipeline-architect": "Design data pipeline architectures with batch/streaming processing, data quality checks, and fault tolerance",
    "data/privacy-expert": "Implement data privacy with anonymization, differential privacy, data masking, consent management, and regulatory compliance",
    "data/quality-expert": "Build data quality frameworks with validation rules, profiling, anomaly detection, and automated data quality monitoring",
    "data/quant-analyst": "Perform quantitative analysis with financial modeling, risk metrics, portfolio optimization, and time series forecasting",
    "data/recommendation-system-expert": "Build recommendation engines with collaborative filtering, content-based methods, hybrid approaches, and cold-start handling",
    "data/reinforcement-learning-expert": "Build reinforcement learning agents with reward functions, policy gradient methods, Q-learning, and environment simulation",
    "data/research-analyst": "Conduct quantitative research with hypothesis formulation, data collection, statistical analysis, and findings presentation",
    "data/researcher": "Perform systematic data research with literature review, methodology design, data collection, and reproducible analysis",
    "data/scientist": "Apply data science methodology with exploratory analysis, feature engineering, model selection, and results communication",
    "data/statistical-analyst": "Perform statistical analysis with hypothesis testing, regression modeling, ANOVA, Bayesian methods, and confidence intervals",
    "data/synthetic-data-generator": "Generate synthetic datasets preserving statistical properties, privacy constraints, and domain-specific distributions",
    "data/time-series-analyst": "Analyze time series data with trend decomposition, seasonality detection, forecasting models (ARIMA, Prophet), and anomaly detection",
    "data/trend-analyst": "Identify and forecast data trends with moving averages, exponential smoothing, change point detection, and growth modeling",
    "data/visualization-expert": "Create data visualizations with chart selection, color theory, interactive dashboards, and storytelling through data",
    "data/viz-attribution-analyst": "Build marketing attribution models with multi-touch analysis, conversion path mapping, and channel effectiveness measurement",
    "data/viz-business-intelligence-designer": "Design BI dashboards with KPI selection, drill-down navigation, self-service analytics, and executive reporting views",
    "data/viz-churn-analyst": "Analyze customer churn with cohort analysis, survival curves, churn prediction models, and retention driver identification",
    "data/viz-cohort-analyst": "Perform cohort analysis with user segmentation, retention curves, lifecycle metrics, and behavioral pattern identification",
    "data/viz-dashboard-designer": "Design interactive dashboards with layout best practices, widget selection, filtering systems, and real-time data updates",
    "data/viz-data-storyteller": "Create data narratives with visualization sequencing, annotation, context framing, and audience-appropriate presentation",
    "data/viz-funnel-analyst": "Analyze conversion funnels with drop-off identification, segmented funnel views, and optimization recommendations",
    "data/viz-kpi-designer": "Design KPI frameworks with metric hierarchies, target setting, tracking dashboards, and performance alerting systems",
    "data/viz-metrics-analyst": "Define and analyze product metrics with engagement tracking, growth accounting, and metric decomposition frameworks",
    "data/viz-real-time-analytics-expert": "Build real-time analytics systems with streaming aggregation, live dashboards, event processing, and low-latency visualization",
    "data/viz-report-builder": "Generate automated reports with data aggregation, chart generation, narrative summaries, and scheduled distribution",
    "data/viz-retention-analyst": "Analyze user retention with day-N retention curves, engagement scoring, reactivation analysis, and lifecycle stage mapping",
    "data/viz-revenue-analyst": "Analyze revenue metrics with MRR/ARR tracking, unit economics, revenue cohorts, and financial forecasting models",
    "data/viz-user-behavior-analyst": "Analyze user behavior with event tracking, session analysis, user flow mapping, and behavioral segmentation",
    "data/viz-visualization-expert": "Build advanced data visualizations with D3.js, Plotly, or Vega-Lite for interactive, publication-quality charts",
    "data/warehouse-architect": "Design data warehouse architectures with dimensional modeling, slowly changing dimensions, and query optimization strategies",

    # ── design plugin ────────────────────────────────────────────────────────
    "design/accessibility-designer": "Design accessible interfaces with inclusive design patterns, WCAG guidelines, assistive technology support, and cognitive accessibility",
    "design/design-critique-facilitator": "Facilitate structured design critiques with feedback frameworks, constructive analysis, and actionable improvement suggestions",
    "design/design-handoff-specialist": "Prepare design-to-development handoffs with specifications, component inventories, interaction annotations, and asset export",
    "design/design-metrics-analyst": "Measure design effectiveness with usability metrics, task completion rates, satisfaction scores, and design system adoption tracking",
    "design/design-researcher": "Conduct design research with user interviews, surveys, competitive analysis, and synthesis into actionable design insights",
    "design/design-sprint-facilitator": "Facilitate design sprints with problem framing, ideation exercises, rapid prototyping, and user testing within a week",
    "design/design-storyteller": "Craft design narratives that communicate vision, rationale, and user impact for stakeholder presentations and case studies",
    "design/design-system-architect": "Design and maintain design systems with tokens, components, documentation, versioning, and cross-platform consistency",
    "design/design-system-governance-expert": "Establish design system governance with contribution guidelines, review processes, deprecation policies, and adoption metrics",
    "design/information-architect": "Design information architectures with content organization, taxonomy, navigation systems, and findability optimization",
    "design/interaction-designer": "Design interaction patterns with micro-interactions, transitions, gesture systems, and responsive behavior specifications",
    "design/mobile-ux-designer": "Design mobile user experiences with touch interactions, navigation patterns, gesture shortcuts, and platform-appropriate conventions",
    "design/persona-creator": "Create evidence-based user personas with demographic data, behavioral patterns, goals, pain points, and usage scenarios",
    "design/prototyping-expert": "Build interactive prototypes with clickable wireframes, animation sequences, and user flow simulations for validation testing",
    "design/usability-tester": "Plan and conduct usability tests with task scenarios, participant recruitment, observation protocols, and findings reports",
    "design/user-journey-mapper": "Map user journey flows with touchpoints, emotions, pain points, and opportunity identification across service channels",
    "design/ux-researcher": "Conduct UX research with qualitative and quantitative methods, synthesis frameworks, and evidence-based design recommendations",
    "design/visual-designer": "Create visual designs with typography, color systems, iconography, illustration styles, and brand-consistent UI elements",
    "design/voice-ui-designer": "Design voice user interfaces with conversation flows, intent mapping, error recovery, and multi-modal interaction patterns",
    "design/wireframe-designer": "Create wireframes with layout structure, content hierarchy, component placement, and responsive breakpoint planning",

    # ── infra plugin ─────────────────────────────────────────────────────────
    "infra/api-gateway-designer": "Design infrastructure-level API gateways with traffic routing, SSL termination, caching policies, and multi-service ingress",
    "infra/assistant": "Provide general infrastructure guidance for cloud setup, server configuration, and deployment architecture decisions",
    "infra/aws-specialist": "Design and manage AWS infrastructure with EC2, S3, Lambda, RDS, CloudFormation, and cost optimization strategies",
    "infra/azure-expert": "Build Azure infrastructure with Resource Manager, App Services, AKS, Cosmos DB, and Azure networking configurations",
    "infra/backup-strategist": "Design backup strategies with 3-2-1 rules, incremental backups, retention policies, and cross-region disaster recovery",
    "infra/compliance-expert": "Implement infrastructure compliance with CIS benchmarks, SOC 2 controls, HIPAA safeguards, and automated audit trails",
    "infra/cost-optimizer": "Optimize cloud costs with reserved instances, spot pricing, right-sizing, resource scheduling, and usage analysis",
    "infra/gcp-architect": "Design Google Cloud architectures with GKE, Cloud Run, BigQuery, Spanner, and GCP networking configurations",
    "infra/migration-specialist": "Plan and execute infrastructure migrations between cloud providers, on-premises to cloud, and version upgrades",
    "infra/monitoring-architect": "Design infrastructure monitoring with alerting hierarchies, SLO dashboards, capacity planning, and incident response automation",
    "infra/multi-cloud-architect": "Design multi-cloud architectures with workload distribution, data synchronization, and vendor-neutral infrastructure patterns",
    "infra/networking-specialist": "Configure network infrastructure with VPCs, subnets, security groups, transit gateways, and hybrid connectivity",
    "infra/premium": "Provide premium infrastructure consulting for enterprise-scale architecture, capacity planning, and high-availability design",
    "infra/security-architect": "Design infrastructure security architectures with defense-in-depth, network segmentation, and zero-trust principles",
    "infra/serverless-architect": "Design serverless architectures with Lambda/Cloud Functions, event-driven patterns, cold start optimization, and cost modeling",
    "infra/solutions-architect": "Design end-to-end technical solutions matching business requirements to cloud services, databases, and integration patterns",
    "infra/storage-expert": "Design storage solutions with block, object, and file storage, tiering policies, replication, and performance optimization",

    # ── ops plugin ───────────────────────────────────────────────────────────
    "ops/analytics-expert": "Define business analytics strategies with metric frameworks, data collection plans, and dashboard requirements",
    "ops/announcement-writer": "Write clear product announcements, release communications, and stakeholder updates with appropriate tone and detail",
    "ops/backlog-manager": "Manage product backlogs with prioritization frameworks, story refinement, sprint planning, and technical debt tracking",
    "ops/beta-program-manager": "Design and manage beta programs with participant recruitment, feedback collection, issue tracking, and launch readiness criteria",
    "ops/board-presentation": "Create board-level presentations with strategic metrics, financial summaries, competitive positioning, and governance updates",
    "ops/business-analyst": "Analyze business processes, gather requirements, model workflows, and translate business needs into technical specifications",
    "ops/business-case-writer": "Write business cases with cost-benefit analysis, ROI projections, risk assessment, and strategic alignment justification",
    "ops/business-intelligence-analyst": "Build BI reports with data modeling, KPI tracking, trend analysis, and self-service analytics for business stakeholders",
    "ops/business-metrics-designer": "Design business metric systems with leading/lagging indicators, metric trees, and measurement instrumentation plans",
    "ops/business-model-designer": "Design business models with revenue streams, cost structures, value propositions, and go-to-market channel strategies",
    "ops/business-plan": "Write comprehensive business plans with market analysis, financial projections, competitive positioning, and growth strategies",
    "ops/business-process-designer": "Design and optimize business processes with workflow mapping, bottleneck analysis, and automation opportunities",
    "ops/change-management-expert": "Plan organizational change with stakeholder impact analysis, communication plans, training programs, and adoption metrics",
    "ops/competitive-analyst": "Conduct competitive analysis with market positioning, feature comparisons, SWOT analysis, and strategic recommendations",
    "ops/conflict-resolver": "Mediate team conflicts with structured dialogue frameworks, root cause identification, and resolution agreements",
    "ops/consultant": "Provide management consulting with problem structuring, data-driven analysis, recommendation synthesis, and stakeholder alignment",
    "ops/context-manager": "Manage project context with documentation strategies, knowledge transfer plans, and institutional memory preservation",
    "ops/cross-cultural-communicator": "Navigate cross-cultural business communication with cultural awareness, localized messaging, and inclusive collaboration practices",
    "ops/customer-research-expert": "Conduct customer research with interview design, survey methodology, persona development, and journey mapping",
    "ops/customer-success-manager": "Manage customer success with onboarding playbooks, health scoring, expansion strategies, and churn prevention tactics",
    "ops/dependency-manager": "Track and manage project dependencies with risk assessment, mitigation plans, and cross-team coordination",
    "ops/documentation-writer": "Write operational documentation with process guides, standard operating procedures, and knowledge base articles",
    "ops/email-writer": "Compose professional emails with appropriate tone, clear structure, and effective calls to action for business contexts",
    "ops/executive-communicator": "Craft executive communications with strategic framing, data-backed narratives, and board-ready presentation materials",
    "ops/executive-summary-writer": "Write concise executive summaries that distill complex information into clear, actionable briefs for senior leadership",
    "ops/executive-summary": "Create structured executive summaries with situation analysis, key findings, recommendations, and next steps",
    "ops/experimentation-expert": "Design business experiments with hypothesis formation, test design, success metrics, and results interpretation",
    "ops/feature-prioritization-expert": "Prioritize features with RICE scoring, Jobs-to-be-Done analysis, OKR alignment, and stakeholder impact assessment",
    "ops/feedback-provider": "Deliver constructive feedback with specific observations, behavioral impact framing, and growth-oriented suggestions",
    "ops/financial-analyst": "Perform financial analysis with modeling, forecasting, variance analysis, and investment evaluation frameworks",
    "ops/git-workflow-manager": "Design git branching strategies, code review workflows, merge policies, and release branch management",
    "ops/go-to-market-strategist": "Plan go-to-market strategies with market segmentation, positioning, channel selection, and launch timeline coordination",
    "ops/growth-strategist": "Develop growth strategies with acquisition funnels, retention loops, viral mechanics, and growth experiment design",
    "ops/interview-prep": "Prepare for job interviews with behavioral question practice, technical topic review, and company research strategies",
    "ops/interview-preparer": "Design interview processes with question banks, evaluation rubrics, candidate assessment frameworks, and debrief templates",
    "ops/investor-pitch": "Create investor pitch decks with market opportunity, traction metrics, team credentials, and financial projections",
    "ops/launch-specialist": "Coordinate product launches with timeline management, checklist execution, stakeholder alignment, and launch day operations",
    "ops/market-fit-analyst": "Assess product-market fit with Sean Ellis tests, NPS analysis, retention metrics, and qualitative user feedback synthesis",
    "ops/market-researcher": "Conduct market research with industry analysis, TAM/SAM/SOM sizing, customer segmentation, and trend identification",
    "ops/meeting-facilitator": "Facilitate effective meetings with agenda design, time management, decision-making frameworks, and action item tracking",
    "ops/metrics-analyst": "Define and analyze operational metrics with baseline establishment, trend analysis, anomaly investigation, and reporting cadence",
    "ops/negotiation-coach": "Coach negotiation skills with BATNA analysis, value creation tactics, anchoring strategies, and deal structuring techniques",
    "ops/okr-designer": "Design OKR frameworks with objective setting, key result measurement, alignment cascading, and progress tracking systems",
    "ops/operations-strategist": "Optimize operations with process analysis, efficiency improvements, resource allocation, and operational excellence frameworks",
    "ops/partnership-strategist": "Develop partnership strategies with partner identification, deal structuring, value alignment, and relationship management",
    "ops/presentation-coach": "Coach presentation delivery with slide design, storytelling structure, audience engagement, and speaking confidence techniques",
    "ops/pricing-strategist": "Design pricing strategies with value-based pricing, competitive analysis, price elasticity modeling, and packaging optimization",
    "ops/product-manager-agent": "Provide product management guidance with feature scoping, user story writing, sprint planning, and stakeholder communication",
    "ops/product-manager": "Manage product lifecycle with roadmap planning, requirement definition, cross-functional coordination, and delivery tracking",
    "ops/project-manager": "Manage projects with work breakdown structures, milestone tracking, risk management, and resource coordination",
    "ops/requirements-analyst": "Gather and document requirements with stakeholder interviews, use case modeling, acceptance criteria, and traceability matrices",
    "ops/risk-analyst": "Assess business risks with probability-impact matrices, mitigation strategies, risk registers, and contingency planning",
    "ops/risk-manager": "Manage enterprise risk with risk frameworks, control assessments, reporting dashboards, and compliance monitoring",
    "ops/roadmap-planner": "Build product roadmaps with theme-based planning, dependency mapping, capacity allocation, and stakeholder communication",
    "ops/roi-calculator": "Calculate return on investment with cost modeling, benefit quantification, payback period analysis, and sensitivity testing",
    "ops/sales-engineer": "Support sales with technical demonstrations, proof of concept builds, solution architecture, and RFP responses",
    "ops/slack-message-optimizer": "Craft effective Slack messages with clear formatting, appropriate channel selection, and actionable communication patterns",
    "ops/stakeholder-analyst": "Map stakeholders with influence-interest analysis, engagement strategies, and communication frequency planning",
    "ops/stakeholder-communicator": "Communicate with stakeholders using tailored messaging, progress updates, and escalation management",
    "ops/stakeholder-report": "Create stakeholder reports with project status, milestone progress, risk summaries, and decision requests",
    "ops/status-report-writer": "Write status reports with progress summaries, blockers, upcoming milestones, and resource utilization updates",
    "ops/strategic-planning-expert": "Conduct strategic planning with vision setting, strategic analysis, initiative prioritization, and execution roadmaps",
    "ops/strategist": "Develop organizational strategies with competitive positioning, capability assessment, and strategic initiative planning",
    "ops/team-communication-optimizer": "Optimize team communication with channel design, meeting cadence, async workflows, and information architecture",
    "ops/team-retrospective-facilitator": "Facilitate team retrospectives with structured reflection, root cause analysis, and improvement action item generation",
    "ops/technical-explainer": "Explain technical concepts to non-technical audiences with analogies, visual aids, and progressive complexity layering",
    "ops/user-story-writer": "Write user stories with acceptance criteria, persona-driven narratives, edge case coverage, and testable requirements",
    "ops/value-proposition-designer": "Design value propositions with customer job analysis, pain/gain mapping, and competitive differentiation positioning",
    "ops/vendor-analyst": "Evaluate vendors with scoring matrices, capability assessments, pricing analysis, and contract term recommendations",
    "ops/vision-creator": "Craft product and organizational visions with aspirational narratives, strategic pillars, and alignment frameworks",

    # ── product plugin ───────────────────────────────────────────────────────
    "product/brainstorm-partner": "Guide collaborative brainstorming sessions with structured ideation techniques, idea evaluation, and concept refinement",
    "product/concept": "Develop product concepts from initial ideas through validation, specification, and development-ready documentation",
    "product/ideation": "Generate and evaluate product ideas with structured ideation frameworks, feasibility assessment, and opportunity scoring",

    # ── research plugin ──────────────────────────────────────────────────────
    "research/agent-organizer": "Organize multi-agent research workflows with task delegation, output synthesis, and knowledge consolidation",
    "research/budget-planner": "Create detailed project budgets with cost estimation, resource allocation, contingency planning, and tracking templates",
    "research/compliance-auditor": "Audit regulatory compliance with checklist-based assessments, gap analysis, remediation tracking, and evidence documentation",
    "research/decision-advisor": "Provide structured decision support with options analysis, criteria weighting, risk assessment, and recommendation synthesis",
    "research/electrician": "Provide electrical engineering guidance for residential and commercial wiring, code compliance, and circuit design",
    "research/error-coordinator": "Coordinate error investigation across systems with root cause analysis, impact assessment, and resolution tracking",
    "research/fact-check": "Verify claims and statements with source identification, evidence evaluation, and accuracy assessment",
    "research/feature-spec": "Write detailed feature specifications with requirements, acceptance criteria, edge cases, and implementation guidance",
    "research/forecast-modeler": "Build forecast models with trend analysis, scenario planning, sensitivity analysis, and confidence interval estimation",
    "research/knowledge-synthesizer": "Synthesize information from multiple sources into coherent summaries, frameworks, and actionable recommendations",
    "research/legal-advisor": "Provide legal analysis for contracts, terms of service, intellectual property, regulatory compliance, and risk assessment",
    "research/literature-reviewer": "Conduct systematic literature reviews with source evaluation, thematic analysis, and research gap identification",
    "research/manufacturing-planner": "Plan manufacturing processes with production scheduling, capacity analysis, quality control, and supply chain coordination",
    "research/market-researcher-agent": "Conduct automated market research with data collection, competitor tracking, and trend analysis across sources",
    "research/medical-diagnosis": "Analyze medical symptoms and conditions with differential diagnosis frameworks, evidence-based guidelines, and referral recommendations",
    "research/multi-agent-coordinator": "Coordinate multiple research agents with task distribution, progress tracking, and output aggregation strategies",
    "research/performance-monitor": "Monitor system performance with metric collection, baseline comparison, alerting thresholds, and trend reporting",
    "research/problem-solver": "Apply structured problem-solving with root cause analysis, hypothesis testing, and solution evaluation frameworks",
    "research/product-designer": "Design physical and digital products with user needs analysis, concept development, and prototyping recommendations",
    "research/risk-assessor": "Assess project and operational risks with probability analysis, impact evaluation, and mitigation strategy development",
    "research/scrum-master": "Facilitate Scrum ceremonies, remove impediments, coach agile practices, and track sprint velocity and burndown",
    "research/system-architect": "Design system architectures with component identification, interface definition, scalability planning, and technology selection",
    "research/task-distributor": "Distribute tasks across team members or agents with load balancing, skill matching, and dependency management",
    "research/therapist": "Provide mental health support guidance with active listening frameworks, coping strategies, and self-care recommendations",
    "research/tradeoff-analyzer": "Analyze trade-offs between options with multi-criteria decision analysis, weighted scoring, and sensitivity assessment",
    "research/trend-spotter": "Identify emerging trends with signal detection, pattern recognition, and forward-looking analysis across domains",
    "research/unit-economics": "Calculate unit economics with customer acquisition cost, lifetime value, contribution margins, and payback period analysis",
    "research/workflow-orchestrator": "Design and manage complex workflows with task sequencing, parallel execution, error handling, and progress monitoring",

    # ── tools plugin ─────────────────────────────────────────────────────────
    "tools/action-items": "Extract and organize action items from meeting notes, conversations, and documents with assignee and deadline tracking",
    "tools/assistant": "Provide general-purpose task assistance with structured responses, step-by-step guidance, and contextual recommendations",
    "tools/default": "Handle general requests with adaptive responses, task decomposition, and appropriate tool selection",
    "tools/general": "Provide versatile assistance for miscellaneous tasks with clear explanations and structured output",
    "tools/helper": "Assist with quick tasks, answer questions, and provide concise guidance on a variety of topics",
    "tools/meeting-summary": "Summarize meetings with key decisions, discussion points, action items, and follow-up deadlines",
    "tools/mobile-testing": "Test mobile apps on simulators and devices with automated UI interaction, screenshot capture, and accessibility checks",
    "tools/quick-answer": "Provide fast, concise answers to straightforward questions with relevant context and source references",

    # ── write plugin ─────────────────────────────────────────────────────────
    "write/api-documenter": "Write API documentation with endpoint descriptions, request/response examples, authentication guides, and error reference tables",
    "write/blog-writer": "Write blog posts with SEO optimization, engaging introductions, structured sections, and audience-targeted content",
    "write/changelog-writer": "Write changelogs with categorized changes, migration guides, breaking change alerts, and version comparison notes",
    "write/code-comment-reviewer": "Review code comments for accuracy, clarity, staleness, and alignment with the actual code behavior",
    "write/content-marketer": "Create marketing content with brand voice consistency, conversion-focused copy, and multi-channel campaign messaging",
    "write/content-writer": "Write web copy, landing pages, and articles with clear messaging, audience awareness, and call-to-action optimization",
    "write/diagram-creator": "Create technical diagrams with Mermaid, PlantUML, or draw.io for architecture, flow, sequence, and entity relationships",
    "write/documentation-tester": "Test documentation for accuracy by following instructions, verifying code samples, and identifying gaps or inconsistencies",
    "write/documentation-writer": "Write technical documentation with user guides, installation instructions, troubleshooting sections, and reference materials",
    "write/email": "Compose emails with appropriate tone, clear structure, professional formatting, and effective subject lines",
    "write/explainer": "Write clear explanations of complex topics with progressive disclosure, analogies, and structured learning paths",
    "write/feedback": "Write constructive feedback with specific examples, behavioral observations, and actionable improvement suggestions",
    "write/french-translator": "Translate text to and from French with natural phrasing, cultural context, and domain-appropriate terminology",
    "write/german-translator": "Translate text to and from German with proper grammar, compound word handling, and formal/informal register",
    "write/grant-writer": "Write grant proposals with compelling narratives, budget justifications, methodology descriptions, and impact statements",
    "write/japanese-translator": "Translate text to and from Japanese with appropriate politeness levels, kanji usage, and cultural context",
    "write/knowledge-base-architect": "Design knowledge base structures with taxonomy, article templates, search optimization, and content governance policies",
    "write/language-translator": "Translate text between languages with context preservation, idiomatic expressions, and domain-specific terminology",
    "write/naming": "Generate effective names for products, features, variables, and projects with criteria-based evaluation and domain awareness",
    "write/newsletter-writer": "Write engaging newsletters with compelling subject lines, scannable formatting, and subscriber retention strategies",
    "write/pitch-deck-writer": "Write pitch deck content with problem-solution framing, market sizing, traction metrics, and investor-focused narratives",
    "write/proofread": "Proofread text for grammar, spelling, punctuation, consistency, and style guide adherence with tracked corrections",
    "write/proposal-writer": "Write business proposals with executive summaries, scope definitions, pricing structures, and timeline commitments",
    "write/readme-writer": "Write README files with project overview, installation steps, usage examples, configuration options, and contribution guidelines",
    "write/release-notes-writer": "Write release notes with user-facing change summaries, upgrade instructions, and known issue documentation",
    "write/script-writer": "Write scripts for videos, podcasts, and presentations with dialogue, stage directions, and timing annotations",
    "write/sdk-documentation-expert": "Write SDK documentation with quickstart guides, API references, code examples, and migration guides for developers",
    "write/social-media-writer": "Write social media content with platform-specific formatting, hashtag strategies, and engagement-optimized copy",
    "write/spanish-translator": "Translate text to and from Spanish with regional dialect awareness, formal/informal register, and cultural nuance",
    "write/story-writer": "Write creative stories with character development, plot structure, dialogue, and narrative voice consistency",
    "write/style-guide-creator": "Create writing style guides with tone definitions, terminology standards, formatting rules, and usage examples",
    "write/tagline": "Generate memorable taglines and slogans with brand alignment, emotional resonance, and competitive differentiation",
    "write/technical-blog-writer": "Write technical blog posts with code examples, architecture explanations, and developer-audience-appropriate depth",
    "write/technical-editor": "Edit technical content for accuracy, clarity, consistency, and audience appropriateness with tracked changes",
    "write/technical-presentation-designer": "Design technical presentation structures with slide content, speaker notes, and visual hierarchy recommendations",
    "write/technical-writer-agent": "Generate technical documentation through iterative drafting with outline review, content generation, and revision cycles",
    "write/technical-writer": "Write technical documents with clear structure, precise language, consistent terminology, and audience-appropriate detail",
    "write/translator": "Translate text between any language pair with context awareness, terminology consistency, and natural target language flow",
    "write/tutorial-creator": "Create step-by-step tutorials with progressive complexity, code examples, exercises, and troubleshooting sections",
    "write/video-script-writer": "Write video scripts with visual cues, narration text, timing marks, and B-roll suggestions for educational or marketing content",
}


def parse_skill_md(filepath):
    """Parse SKILL.md frontmatter and return (name, description, full_content)."""
    with open(filepath, "r") as f:
        content = f.read()

    # Match YAML frontmatter
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return None, None, content

    frontmatter = match.group(1)
    name = None
    description = None
    for line in frontmatter.split("\n"):
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip()
        elif line.startswith("description:"):
            description = line.split(":", 1)[1].strip()
            # Handle quoted descriptions
            if description.startswith('"') and description.endswith('"'):
                description = description[1:-1]

    return name, description, content


def has_bad_description(description):
    """Check if a description follows the bad 'Name — frameworks' pattern."""
    if not description:
        return False
    return " — " in description


def fix_description(filepath, plugin, skill_name, dry_run=False):
    """Fix a single SKILL.md description. Returns (old_desc, new_desc) or None."""
    name, description, content = parse_skill_md(filepath)
    if not description:
        return None

    if not has_bad_description(description):
        return None  # Already has a good description

    key = f"{plugin}/{skill_name}"
    if key not in SKILL_DESCRIPTIONS:
        print(f"  WARNING: No replacement description for {key}", file=sys.stderr)
        return None

    new_desc = SKILL_DESCRIPTIONS[key]

    if not dry_run:
        # Replace the description line in the file
        # Handle both quoted and unquoted descriptions
        old_line = f"description: {description}"
        # Also try with quotes
        old_line_quoted = f'description: "{description}"'

        if old_line_quoted in content:
            new_content = content.replace(old_line_quoted, f"description: {new_desc}", 1)
        elif old_line in content:
            new_content = content.replace(old_line, f"description: {new_desc}", 1)
        else:
            print(f"  WARNING: Could not find description line in {filepath}", file=sys.stderr)
            return None

        with open(filepath, "w") as f:
            f.write(new_content)

    return (description, new_desc)


def regenerate_agents_md(plugin):
    """Regenerate a plugin's AGENTS.md from its skill files."""
    skills_dir = os.path.join(REPO_ROOT, plugin, "skills")
    if not os.path.isdir(skills_dir):
        return

    rows = []
    for skill_name in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
        if not os.path.isfile(skill_path):
            continue

        name, description, _ = parse_skill_md(skill_path)
        if not description:
            continue

        # Clean up description for table display
        desc = description.strip()
        if desc.startswith('"') and desc.endswith('"'):
            desc = desc[1:-1]

        rows.append((skill_name, desc))

    agents_md_path = os.path.join(REPO_ROOT, plugin, "AGENTS.md")
    with open(agents_md_path, "w") as f:
        f.write(f"# {plugin} — Agent Skills\n\n")
        f.write("| Skill | Description |\n")
        f.write("|-------|-------------|\n")
        for skill_name, desc in rows:
            # Use plain skill name with file path instead of /plugin:skill invocation
            f.write(f"| `{skill_name}` | {desc} |\n")
        f.write(f"\n**Path:** `~/Projects/agent-skills/{plugin}/skills/<skill-name>/SKILL.md`\n")
        f.write(f"\nTo use a skill, read its SKILL.md file for full instructions.\n")

    return len(rows)


def main():
    parser = argparse.ArgumentParser(description="Fix duplicative skill descriptions")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--regen-only", action="store_true", help="Only regenerate AGENTS.md files")
    args = parser.parse_args()

    if not args.regen_only:
        print("=" * 60)
        print("Fixing skill descriptions")
        print("=" * 60)

        total_fixed = 0
        total_skipped = 0
        total_warnings = 0

        for plugin in PLUGINS:
            skills_dir = os.path.join(REPO_ROOT, plugin, "skills")
            if not os.path.isdir(skills_dir):
                continue

            plugin_fixed = 0
            for skill_name in sorted(os.listdir(skills_dir)):
                skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
                if not os.path.isfile(skill_path):
                    continue

                result = fix_description(skill_path, plugin, skill_name, dry_run=args.dry_run)
                if result is None:
                    total_skipped += 1
                else:
                    old_desc, new_desc = result
                    plugin_fixed += 1
                    if args.dry_run:
                        print(f"  {plugin}/{skill_name}:")
                        print(f"    OLD: {old_desc}")
                        print(f"    NEW: {new_desc}")

            total_fixed += plugin_fixed
            print(f"  {plugin}: {plugin_fixed} descriptions {'would be ' if args.dry_run else ''}fixed")

        print(f"\nTotal: {total_fixed} fixed, {total_skipped} skipped (already good)")

        if args.dry_run:
            print("\n(Dry run — no files were modified)")
            return

    # Regenerate AGENTS.md catalogs
    print("\n" + "=" * 60)
    print("Regenerating AGENTS.md catalogs")
    print("=" * 60)

    for plugin in PLUGINS:
        count = regenerate_agents_md(plugin)
        if count:
            print(f"  {plugin}/AGENTS.md: {count} skills")

    print("\nDone!")


if __name__ == "__main__":
    main()
