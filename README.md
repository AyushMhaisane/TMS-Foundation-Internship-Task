# TMS Foundation: Web Development Assessment
**Candidate:** [Your Name]  
**Submission Date:** January 7, 2026

---

## Task 1: Strategic Analysis & Audit

### 1. Decoupled Architecture (React + Django)
For a non-profit like TMS Foundation, a decoupled architecture is about **longevity and flexibility**.
* **Scalability:** By using Django as a REST API and React as the frontend, we ensure the backend can eventually power a mobile app without rewriting code.
* **Performance:** React allows for a fast, "app-like" experience for donors, while Django provides industry-standard security for sensitive data.

### 2. UI/UX Audit: dev.bharatyuva.org
* **Mobile UX:** The navigation menu is not fully optimized for touch, leading to potential misclicks on smaller screens.
* **Accessibility:** Higher contrast is needed for call-to-action buttons to ensure the site is usable for everyone, including those with visual impairments.
* **Stability:** Implementing fixed dimensions for media will prevent "Layout Shifts," making the site feel more professional and polished.

### 3. Redesign Vision: Live Impact Tracker
I suggest an **Interactive Impact Dashboard**. Using React, we can create live data visualizations (like progress bars for fundraising goals) that build immediate trust with donors.

---

## Task 2: Technical Proficiency

### 1. API Integration (CORS)
To enable secure communication between React and Django, I implement `django-cors-headers`. This ensures only our trusted frontend can access the database.
*(See `implementation/django_cors_setup.py`)*

### 2. State Management (Context API)
I use the **React Context API** for global data like user authentication. This prevents "prop drilling" and ensures a seamless experience as a user moves through different sections of the portal.
*(See `implementation/AuthContext.js`)*

---

## Practical Implementation
I have included a folder titled `/implementation` containing documented code snippets for the technical tasks mentioned above.