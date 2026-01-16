import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { 
  Zap, BarChart3, Shield, TrendingUp, Users, CheckCircle, 
  Database, Lock, Globe, Code, FileText, Bell 
} from 'lucide-react'

export default function Features() {
  const features = [
    {
      icon: Zap,
      title: 'AI-Powered Analysis',
      description: 'Automatically discover patterns, anomalies, and insights using advanced machine learning algorithms.',
      details: [
        'Natural language queries',
        'Automated pattern detection',
        'Anomaly identification',
        'Predictive modeling'
      ]
    },
    {
      icon: BarChart3,
      title: 'Interactive Dashboards',
      description: 'Create beautiful, customizable dashboards with drag-and-drop functionality and real-time updates.',
      details: [
        'Drag-and-drop builder',
        'Real-time data sync',
        'Custom visualizations',
        'Export to PDF/PNG'
      ]
    },
    {
      icon: Shield,
      title: 'Enterprise Security',
      description: 'Bank-level encryption, SSO, and compliance with SOC 2, GDPR, and HIPAA standards.',
      details: [
        'End-to-end encryption',
        'Single Sign-On (SSO)',
        'Role-based access control',
        'Audit logs'
      ]
    },
    {
      icon: TrendingUp,
      title: 'Predictive Analytics',
      description: 'Forecast future trends and make data-driven predictions with machine learning models.',
      details: [
        'Time series forecasting',
        'Regression analysis',
        'Classification models',
        'Custom ML pipelines'
      ]
    },
    {
      icon: Database,
      title: 'Data Integration',
      description: 'Connect to 100+ data sources including databases, APIs, cloud storage, and more.',
      details: [
        'SQL databases',
        'REST APIs',
        'Cloud storage (S3, GCS)',
        'Data warehouses'
      ]
    },
    {
      icon: Users,
      title: 'Team Collaboration',
      description: 'Share insights, collaborate on reports, and work together seamlessly with your team.',
      details: [
        'Shared workspaces',
        'Comment threads',
        'Version control',
        'Team permissions'
      ]
    },
    {
      icon: Code,
      title: 'Custom Scripts',
      description: 'Write custom Python or SQL scripts to extend functionality and automate workflows.',
      details: [
        'Python support',
        'SQL queries',
        'Scheduled jobs',
        'API webhooks'
      ]
    },
    {
      icon: FileText,
      title: 'Automated Reports',
      description: 'Generate and schedule automated reports delivered to your inbox or shared with stakeholders.',
      details: [
        'Scheduled reports',
        'Email delivery',
        'PDF generation',
        'Custom templates'
      ]
    },
    {
      icon: Bell,
      title: 'Smart Alerts',
      description: 'Set up intelligent alerts that notify you when important metrics change or thresholds are met.',
      details: [
        'Threshold alerts',
        'Anomaly detection',
        'Multi-channel notifications',
        'Alert rules engine'
      ]
    },
    {
      icon: Globe,
      title: 'Public Dashboards',
      description: 'Share insights publicly with customizable, embeddable dashboards for your website or blog.',
      details: [
        'Public URLs',
        'Embeddable widgets',
        'Custom branding',
        'Access controls'
      ]
    },
    {
      icon: Lock,
      title: 'Data Governance',
      description: 'Manage data access, quality, and compliance with comprehensive governance tools.',
      details: [
        'Data catalog',
        'Lineage tracking',
        'Quality monitoring',
        'Compliance reporting'
      ]
    },
    {
      icon: CheckCircle,
      title: 'Easy Setup',
      description: 'Get started in minutes with our intuitive interface and comprehensive documentation.',
      details: [
        'Quick start guide',
        'Video tutorials',
        'Sample datasets',
        '24/7 support'
      ]
    }
  ]

  return (
    <div className="min-h-screen bg-white">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-50 to-white">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            Powerful Features for
            <span className="text-primary-600 block">Modern Analytics</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Everything you need to analyze data, build dashboards, and make better decisions
          </p>
        </div>
      </section>

      {/* Features Grid */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => {
              const Icon = feature.icon
              return (
                <div
                  key={index}
                  className="p-8 rounded-xl border border-gray-200 hover:shadow-xl transition-all hover:border-primary-200"
                >
                  <div className="w-14 h-14 bg-primary-100 rounded-lg flex items-center justify-center mb-6">
                    <Icon className="h-7 w-7 text-primary-600" />
                  </div>
                  <h3 className="text-xl font-semibold text-gray-900 mb-3">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600 mb-4">
                    {feature.description}
                  </p>
                  <ul className="space-y-2">
                    {feature.details.map((detail, idx) => (
                      <li key={idx} className="flex items-start text-sm text-gray-600">
                        <CheckCircle className="h-4 w-4 text-primary-600 mr-2 mt-0.5 flex-shrink-0" />
                        {detail}
                      </li>
                    ))}
                  </ul>
                </div>
              )
            })}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-primary-600">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Ready to explore all features?
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            Start your free trial and see how InsightForge can transform your data analytics.
          </p>
          <a
            href="/app"
            className="inline-flex items-center justify-center px-8 py-3 bg-white text-primary-600 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
          >
            Start Free Trial
          </a>
        </div>
      </section>

      <Footer />
    </div>
  )
}
