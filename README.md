# Cybersecurity Lab

My hands-on cybersecurity and computer science learning lab, focused on practical experiments, security analysis, and system fundamentals.

## Topics

- **Linux:** Command-line tools, file permissions, users, and groups
- **Networking:** Network fundamentals and communication protocols
- **C++:** Programming fundamentals, memory, pointers, and data structures
- **Computer Memory:** Memory management and program execution
- **Cybersecurity Fundamentals:** Authentication, access control, log analysis, and threat detection

## Projects

### Lab 01 — SSH Login Investigation

A hands-on project that analyzes SSH authentication logs to identify suspicious login activity.

**Features**
- Extracts failed login attempts using Linux commands and Python.
- Counts failed login attempts by IP address.
- Detects repeated failures within a five-minute time window.
- Generates alerts when a configurable threshold is reached.

**Technologies**
- Python
- Linux command-line tools
- Regular expressions
- `pathlib`, `datetime`, and `collections`
- Docker

**Current detection rule:** Alert when an IP address reaches three or more failed login attempts within five minutes.

See the `labs/lab01-login-investigation/` directory for the scripts, sample logs, and investigation report.

## Development Environment

- macOS
- Docker with Ubuntu
- Visual Studio Code
- Git and GitHub

## Learning Approach

I focus on understanding how systems work by building small projects, testing security assumptions, analyzing results, and improving my implementations.

## Roadmap

- Strengthen Linux and networking fundamentals.
- Improve log analysis and detection logic.
- Practice security testing in controlled environments.
- Explore the intersection of cybersecurity and Agentic AI.

## Repository

[View this repository on GitHub](https://github.com/ryo-ji3636/cybersecurity_lab1)

