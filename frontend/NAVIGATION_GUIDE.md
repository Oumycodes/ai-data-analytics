# 🧭 Navigation Guide - InsightForge

This guide shows you how to navigate between all pages in the InsightForge website.

## 🚀 Starting the App

First, make sure both services are running:

```bash
# Terminal 1 - Streamlit
cd /Users/oumyb/Desktop/ai-data-analytics
streamlit run app.py

# Terminal 2 - Next.js
cd /Users/oumyb/Desktop/ai-data-analytics/frontend
npm run dev
```

Then open: **http://localhost:3000**

## 📍 Navigation Bar (Top Menu)

The navigation bar is at the top of every page. It includes:

### Desktop Navigation:
- **Home** → Landing page (`/`)
- **Features** → Features page (`/features`)
- **Studio** → Studio/Workspace page (`/studio`)
- **Launch App** → Analytics app (`/app`) ⭐ **This is where the work happens!**
- **Pricing** → Pricing page (`/pricing`)
- **Dashboard** → Dashboard UI (`/dashboard`)
- **Sign In** → Login page (placeholder)
- **Get Started** → Analytics app (`/app`) ⭐

### Mobile Navigation:
Click the hamburger menu (☰) in the top right to see all pages on mobile.

## 🗺️ All Available Pages

### 1. **Landing Page** (`/`)
**URL:** http://localhost:3000

**What's here:**
- Hero section with main message
- Features overview
- Testimonials
- Call-to-action buttons

**How to navigate:**
- Click "Launch InsightForge" → Goes to `/app`
- Click "Explore Features" → Goes to `/features`
- Use the top navigation bar to go anywhere

---

### 2. **Features Page** (`/features`)
**URL:** http://localhost:3000/features

**What's here:**
- Detailed list of all 12 features
- Feature descriptions with icons
- Benefits and use cases

**How to navigate:**
- Click "Start Free Trial" at bottom → Goes to `/app`
- Use navigation bar to go to other pages

---

### 3. **Studio Page** (`/studio`)
**URL:** http://localhost:3000/studio

**What's here:**
- Project management interface
- Project cards grid
- Quick stats
- Workspace tools

**How to navigate:**
- Click "Launch Analytics" button → Goes to `/app`
- Use navigation bar to go to other pages

---

### 4. **Analytics App** (`/app`) ⭐ **MAIN WORK PAGE**
**URL:** http://localhost:3000/app

**What's here:**
- **This is where you do the actual analytics work!**
- Upload CSV files
- Ask AI-powered questions
- Generate insights
- Create visualizations
- Generate executive summaries

**How to navigate:**
- Click "Open Analytics App" → Opens Streamlit directly at http://localhost:8501
- Use navigation bar to go to other pages

**Note:** Make sure Streamlit is running (`streamlit run app.py`) for this page to work!

---

### 5. **Pricing Page** (`/pricing`)
**URL:** http://localhost:3000/pricing

**What's here:**
- Three pricing tiers (Starter, Professional, Enterprise)
- Feature comparison
- FAQ section

**How to navigate:**
- Click "Start Free Trial" on any plan → Goes to `/app`
- Use navigation bar to go to other pages

---

### 6. **Dashboard Page** (`/dashboard`)
**URL:** http://localhost:3000/dashboard

**What's here:**
- Dashboard UI layout
- Metrics cards
- Chart placeholders
- Recent activity feed

**How to navigate:**
- Use navigation bar to go to other pages

---

## 🎯 Quick Navigation Paths

### From Landing Page to Analytics:
1. Click **"Launch InsightForge"** button (hero section)
2. OR click **"Get Started"** button (top right)
3. OR click **"Launch App"** in navigation bar

### From Any Page to Analytics:
- Click **"Launch App"** in navigation bar
- OR click **"Get Started"** button (top right)
- OR go directly to: http://localhost:3000/app

### Direct URLs:
- Landing: http://localhost:3000
- Features: http://localhost:3000/features
- Studio: http://localhost:3000/studio
- **Analytics (Main):** http://localhost:3000/app ⭐
- Pricing: http://localhost:3000/pricing
- Dashboard: http://localhost:3000/dashboard

## 🔗 Navigation Flow Diagram

```
Landing Page (/)
    │
    ├─→ "Launch InsightForge" → Analytics App (/app) ⭐
    ├─→ "Explore Features" → Features Page (/features)
    ├─→ Navigation Bar → Any Page
    │
    └─→ Footer Links → Various Pages

Analytics App (/app) ⭐
    │
    ├─→ "Open Analytics App" → Direct Streamlit (http://localhost:8501)
    ├─→ Navigation Bar → Any Page
    │
    └─→ This is where you:
        • Upload CSV files
        • Ask questions
        • Get insights
        • Create visualizations
```

## 💡 Tips

1. **The Logo** (top left) always takes you back to the landing page
2. **Navigation bar** is visible on all pages for easy access
3. **"Get Started"** and **"Launch App"** both go to the analytics page
4. **Mobile users**: Use the hamburger menu (☰) to see all pages
5. **Analytics page** requires Streamlit to be running

## 🎨 Visual Navigation Guide

```
┌─────────────────────────────────────────────────┐
│  [Logo]  Home | Features | Studio | Launch App │
│          Pricing | Dashboard    [Sign In] [Get Started] │
└─────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
     Landing        Features        Studio
        │               │               │
        └───────────────┼───────────────┘
                        │
                   Analytics ⭐
                   (Main Work)
                        │
                   ┌────┴────┐
                   │         │
              Pricing    Dashboard
```

## 🚨 Important Notes

- **Analytics App (`/app`)** is the main functional page where you do actual work
- All other pages are informational/marketing pages
- Make sure **Streamlit is running** for the analytics app to work
- You can access Streamlit directly at: http://localhost:8501

---

**Happy Navigating! 🎉**
