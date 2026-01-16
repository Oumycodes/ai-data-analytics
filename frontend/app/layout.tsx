import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'InsightForge - AI-Powered Data Analytics',
  description: 'Transform raw data into actionable insights with AI-powered analytics',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
