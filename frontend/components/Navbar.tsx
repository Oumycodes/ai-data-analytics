'use client'

import Link from 'next/link'
import { useState } from 'react'
import { Menu, X, BarChart3 } from 'lucide-react'

export default function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-sm border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <BarChart3 className="h-8 w-8 text-primary-600" />
            <span className="text-xl font-bold text-gray-900">InsightForge</span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            <Link href="/" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Home
            </Link>
            <Link href="/features" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Features
            </Link>
            <Link href="/studio" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Studio
            </Link>
            <Link href="/app" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Launch App
            </Link>
            <Link href="/pricing" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Pricing
            </Link>
            <Link href="/dashboard" className="text-gray-700 hover:text-primary-600 transition-colors font-medium">
              Dashboard
            </Link>
          </div>

          {/* CTA Buttons */}
          <div className="hidden md:flex items-center space-x-4">
            <Link
              href="/login"
              className="text-gray-700 hover:text-primary-600 transition-colors font-medium"
            >
              Sign In
            </Link>
            <Link
              href="/app"
              className="bg-primary-600 text-white px-4 py-2 rounded-lg font-medium hover:bg-primary-700 transition-colors"
            >
              Get Started
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            className="md:hidden p-2 rounded-md text-gray-700 hover:text-primary-600 hover:bg-gray-100"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="md:hidden border-t border-gray-200 bg-white">
          <div className="px-4 pt-2 pb-3 space-y-1">
            <Link
              href="/"
              className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium"
              onClick={() => setMobileMenuOpen(false)}
            >
              Home
            </Link>
            <Link
              href="/features"
              className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium"
              onClick={() => setMobileMenuOpen(false)}
            >
              Features
            </Link>
            <Link
              href="/studio"
              className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium"
              onClick={() => setMobileMenuOpen(false)}
            >
              Studio
            </Link>
            <Link
              href="/app"
              className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium"
              onClick={() => setMobileMenuOpen(false)}
            >
              Launch App
            </Link>
            <Link
              href="/pricing"
              className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium"
              onClick={() => setMobileMenuOpen(false)}
            >
              Pricing
            </Link>
            <Link
              href="/dashboard"
              className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium"
              onClick={() => setMobileMenuOpen(false)}
            >
              Dashboard
            </Link>
            <div className="pt-4 space-y-2">
              <Link
                href="/login"
                className="block px-3 py-2 text-gray-700 hover:text-primary-600 hover:bg-gray-50 rounded-md font-medium text-center"
                onClick={() => setMobileMenuOpen(false)}
              >
                Sign In
              </Link>
              <Link
                href="/app"
                className="block px-3 py-2 bg-primary-600 text-white rounded-md font-medium text-center hover:bg-primary-700"
                onClick={() => setMobileMenuOpen(false)}
              >
                Get Started
              </Link>
            </div>
          </div>
        </div>
      )}
    </nav>
  )
}
