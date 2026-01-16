import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { ArrowRight, Zap, Shield, BarChart3, TrendingUp, Users, CheckCircle } from 'lucide-react'
import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen bg-white">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-24 pb-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-50 to-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center">
            <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold text-gray-900 mb-6">
              Transform Data Into
              <span className="text-primary-600 block">Actionable Insights</span>
            </h1>
            <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
              AI-powered analytics platform that helps you make data-driven decisions faster. 
              Connect, analyze, and visualize your data with ease.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link
                href="/app"
                className="inline-flex items-center justify-center px-8 py-3 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition-colors"
              >
                Launch InsightForge
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
              <Link
                href="/features"
                className="inline-flex items-center justify-center px-8 py-3 border-2 border-gray-300 text-gray-700 rounded-lg font-semibold hover:border-gray-400 transition-colors"
              >
                Explore Features
              </Link>
            </div>
          </div>

          {/* Hero Image/Dashboard Preview */}
          <div className="mt-16 rounded-xl shadow-2xl overflow-hidden border border-gray-200">
            <div className="bg-gray-900 p-4">
              <div className="flex space-x-2">
                <div className="w-3 h-3 rounded-full bg-red-500"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                <div className="w-3 h-3 rounded-full bg-green-500"></div>
              </div>
            </div>
            <div className="bg-gradient-to-br from-gray-50 to-gray-100 h-96 flex items-center justify-center">
              <div className="text-center">
                <BarChart3 className="h-24 w-24 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500">Dashboard Preview</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
              Everything you need to analyze data
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Powerful features designed to help you understand your data better
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <Zap className="h-6 w-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">AI-Powered Analysis</h3>
              <p className="text-gray-600">
                Leverage advanced AI to automatically discover patterns, trends, and insights in your data.
              </p>
            </div>

            {/* Feature 2 */}
            <div className="p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-accent-100 rounded-lg flex items-center justify-center mb-4">
                <BarChart3 className="h-6 w-6 text-accent-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Real-time Dashboards</h3>
              <p className="text-gray-600">
                Create beautiful, interactive dashboards that update in real-time as your data changes.
              </p>
            </div>

            {/* Feature 3 */}
            <div className="p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <Shield className="h-6 w-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Enterprise Security</h3>
              <p className="text-gray-600">
                Bank-level encryption and compliance with industry standards to keep your data safe.
              </p>
            </div>

            {/* Feature 4 */}
            <div className="p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-accent-100 rounded-lg flex items-center justify-center mb-4">
                <TrendingUp className="h-6 w-6 text-accent-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Predictive Analytics</h3>
              <p className="text-gray-600">
                Forecast future trends and make proactive decisions with machine learning models.
              </p>
            </div>

            {/* Feature 5 */}
            <div className="p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-primary-100 rounded-lg flex items-center justify-center mb-4">
                <Users className="h-6 w-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Team Collaboration</h3>
              <p className="text-gray-600">
                Share insights, collaborate on reports, and work together seamlessly with your team.
              </p>
            </div>

            {/* Feature 6 */}
            <div className="p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-shadow">
              <div className="w-12 h-12 bg-accent-100 rounded-lg flex items-center justify-center mb-4">
                <CheckCircle className="h-6 w-6 text-accent-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">Easy Integration</h3>
              <p className="text-gray-600">
                Connect with 100+ data sources including databases, APIs, and cloud storage.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">
              Trusted by data teams worldwide
            </h2>
            <p className="text-xl text-gray-600">
              See what our customers are saying
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Testimonial 1 */}
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-200">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mr-4">
                  <span className="text-primary-600 font-semibold">JD</span>
                </div>
                <div>
                  <h4 className="font-semibold text-gray-900">John Doe</h4>
                  <p className="text-sm text-gray-600">Data Analyst, TechCorp</p>
                </div>
              </div>
              <p className="text-gray-700">
                "InsightForge has transformed how we analyze data. The AI insights are incredibly accurate and save us hours of manual work."
              </p>
            </div>

            {/* Testimonial 2 */}
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-200">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-accent-100 rounded-full flex items-center justify-center mr-4">
                  <span className="text-accent-600 font-semibold">SM</span>
                </div>
                <div>
                  <h4 className="font-semibold text-gray-900">Sarah Miller</h4>
                  <p className="text-sm text-gray-600">Head of Analytics, DataCo</p>
                </div>
              </div>
              <p className="text-gray-700">
                "The real-time dashboards are a game-changer. Our team can now make decisions based on live data, not yesterday's reports."
              </p>
            </div>

            {/* Testimonial 3 */}
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-200">
              <div className="flex items-center mb-4">
                <div className="w-12 h-12 bg-primary-100 rounded-full flex items-center justify-center mr-4">
                  <span className="text-primary-600 font-semibold">MJ</span>
                </div>
                <div>
                  <h4 className="font-semibold text-gray-900">Michael Johnson</h4>
                  <p className="text-sm text-gray-600">CTO, StartupXYZ</p>
                </div>
              </div>
              <p className="text-gray-700">
                "Easy to set up, powerful features, and excellent support. InsightForge is exactly what we needed for our analytics stack."
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-primary-600">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Ready to get started?
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            Join thousands of teams using InsightForge to make better data-driven decisions.
          </p>
          <Link
            href="/app"
            className="inline-flex items-center justify-center px-8 py-3 bg-white text-primary-600 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
          >
            Start Free Trial
            <ArrowRight className="ml-2 h-5 w-5" />
          </Link>
        </div>
      </section>

      <Footer />
    </div>
  )
}
