# InsightForge Frontend

A professional SaaS frontend for InsightForge, built with Next.js, React, and Tailwind CSS, inspired by DataFa.st design patterns.

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm/yarn/pnpm

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
# or
yarn install
# or
pnpm install
```

3. Run the development server:
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 📁 Project Structure

```
frontend/
├── app/
│   ├── dashboard/      # Dashboard page (UI only)
│   ├── features/       # Features page
│   ├── pricing/        # Pricing page
│   ├── studio/         # Studio/Workspace page
│   ├── globals.css     # Global styles
│   ├── layout.tsx      # Root layout
│   └── page.tsx        # Landing page
├── components/
│   ├── Navbar.tsx      # Navigation component
│   └── Footer.tsx      # Footer component
├── package.json
├── tailwind.config.js  # Tailwind configuration
└── tsconfig.json       # TypeScript configuration
```

## 🎨 Pages

### Landing Page (`/`)
- Hero section with CTA buttons
- Features grid
- Testimonials section
- Final CTA section

### Features Page (`/features`)
- Detailed feature cards with icons
- Feature descriptions and benefits
- CTA section

### Studio Page (`/studio`)
- Project management interface
- Project cards grid
- Quick stats
- Workspace tools

### Pricing Page (`/pricing`)
- Three pricing tiers (Starter, Professional, Enterprise)
- Feature comparison
- FAQ section
- Contact CTA

### Dashboard Page (`/dashboard`)
- Metrics cards
- Chart placeholders
- Recent activity feed
- Search and filter options

## 🎨 Design System

### Colors
- **Primary**: Blue shades (`primary-50` to `primary-900`)
- **Accent**: Teal shades (`accent-50` to `accent-900`)
- **Neutrals**: Gray scale for text and backgrounds

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: Bold, large sizes
- **Body**: Regular weight, readable sizes

### Components
- Responsive navigation bar
- Footer with links
- Card-based layouts
- Button styles (primary, secondary)
- Form inputs

## 🛠️ Tech Stack

- **Next.js 14** - React framework
- **React 18** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Lucide React** - Icons

## 📱 Responsive Design

All pages are fully responsive and optimized for:
- Mobile devices (320px+)
- Tablets (768px+)
- Desktop (1024px+)
- Large screens (1280px+)

## 🚀 Build for Production

```bash
npm run build
npm start
```

## 📝 Notes

- This is a UI-only frontend with no backend integration
- All links and buttons are placeholders
- Chart visualizations are placeholders (replace with actual chart libraries like Chart.js, Recharts, or similar)
- Authentication and data fetching logic should be added separately

## 🔧 Customization

### Colors
Edit `tailwind.config.js` to customize the color palette.

### Fonts
Update `app/globals.css` to change the font family.

### Components
Modify components in the `components/` directory to customize layout and styling.

## 📄 License

This project is a frontend template for InsightForge.
