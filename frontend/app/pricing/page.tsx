import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { Check, ArrowRight } from 'lucide-react'
import Link from 'next/link'

export default function Pricing() {
  const plans = [
    {
      name: 'Starter',
      price: '$29',
      period: '/month',
      description: 'Perfect for individuals and small teams getting started',
      features: [
        'Up to 5 projects',
        '10GB data storage',
        'Basic dashboards',
        'Email support',
        '5 team members',
        'Basic integrations',
        'Export to PDF/PNG'
      ],
      cta: 'Start Free Trial',
      popular: false
    },
    {
      name: 'Professional',
      price: '$99',
      period: '/month',
      description: 'For growing teams that need advanced analytics',
      features: [
        'Unlimited projects',
        '100GB data storage',
        'Advanced dashboards',
        'Priority support',
        'Unlimited team members',
        'All integrations',
        'Custom visualizations',
        'AI-powered insights',
        'Scheduled reports',
        'API access'
      ],
      cta: 'Start Free Trial',
      popular: true
    },
    {
      name: 'Enterprise',
      price: 'Custom',
      period: '',
      description: 'For large organizations with custom requirements',
      features: [
        'Everything in Professional',
        'Unlimited data storage',
        'Dedicated support',
        'Custom integrations',
        'SSO & SAML',
        'Advanced security',
        'Custom SLA',
        'On-premise deployment',
        'Training & onboarding',
        'Dedicated account manager'
      ],
      cta: 'Contact Sales',
      popular: false
    }
  ]

  return (
    <div className="min-h-screen bg-white">
      <Navbar />

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-b from-gray-50 to-white">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold text-gray-900 mb-6">
            Simple, Transparent
            <span className="text-primary-600 block">Pricing</span>
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Choose the plan that's right for you. All plans include a 14-day free trial.
          </p>
        </div>
      </section>

      {/* Pricing Cards */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-white">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {plans.map((plan, index) => (
              <div
                key={index}
                className={`relative rounded-2xl border-2 p-8 ${
                  plan.popular
                    ? 'border-primary-500 shadow-xl scale-105'
                    : 'border-gray-200 hover:border-gray-300'
                } transition-all`}
              >
                {plan.popular && (
                  <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
                    <span className="bg-primary-600 text-white px-4 py-1 rounded-full text-sm font-semibold">
                      Most Popular
                    </span>
                  </div>
                )}

                <div className="text-center mb-8">
                  <h3 className="text-2xl font-bold text-gray-900 mb-2">{plan.name}</h3>
                  <div className="flex items-baseline justify-center mb-4">
                    <span className="text-5xl font-bold text-gray-900">{plan.price}</span>
                    {plan.period && (
                      <span className="text-xl text-gray-600 ml-2">{plan.period}</span>
                    )}
                  </div>
                  <p className="text-gray-600">{plan.description}</p>
                </div>

                <ul className="space-y-4 mb-8">
                  {plan.features.map((feature, idx) => (
                    <li key={idx} className="flex items-start">
                      <Check className="h-5 w-5 text-primary-600 mr-3 flex-shrink-0 mt-0.5" />
                      <span className="text-gray-700">{feature}</span>
                    </li>
                  ))}
                </ul>

                <Link
                  href={plan.name === 'Enterprise' ? '/contact' : '/app'}
                  className={`block w-full text-center py-3 rounded-lg font-semibold transition-colors ${
                    plan.popular
                      ? 'bg-primary-600 text-white hover:bg-primary-700'
                      : 'bg-gray-100 text-gray-900 hover:bg-gray-200'
                  }`}
                >
                  {plan.cta}
                  {plan.name !== 'Enterprise' && (
                    <ArrowRight className="inline-block ml-2 h-4 w-4" />
                  )}
                </Link>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-gray-900 text-center mb-12">
            Frequently Asked Questions
          </h2>
          <div className="space-y-6">
            {[
              {
                q: 'Can I change plans later?',
                a: 'Yes, you can upgrade or downgrade your plan at any time. Changes take effect immediately, and we\'ll prorate the billing.'
              },
              {
                q: 'What payment methods do you accept?',
                a: 'We accept all major credit cards, PayPal, and wire transfers for Enterprise plans.'
              },
              {
                q: 'Is there a free trial?',
                a: 'Yes, all plans include a 14-day free trial. No credit card required to start.'
              },
              {
                q: 'What happens to my data if I cancel?',
                a: 'You can export all your data before canceling. We\'ll keep your data for 30 days after cancellation in case you want to reactivate.'
              }
            ].map((faq, index) => (
              <div key={index} className="bg-white p-6 rounded-lg border border-gray-200">
                <h3 className="font-semibold text-gray-900 mb-2">{faq.q}</h3>
                <p className="text-gray-600">{faq.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 bg-primary-600">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl sm:text-4xl font-bold text-white mb-4">
            Still have questions?
          </h2>
          <p className="text-xl text-primary-100 mb-8">
            Our team is here to help you choose the right plan for your needs.
          </p>
          <Link
            href="/contact"
            className="inline-flex items-center justify-center px-8 py-3 bg-white text-primary-600 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
          >
            Contact Sales
            <ArrowRight className="ml-2 h-5 w-5" />
          </Link>
        </div>
      </section>

      <Footer />
    </div>
  )
}
