import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { 
  TrendingUp, TrendingDown, Users, DollarSign, 
  BarChart3, PieChart, LineChart, Activity,
  Download, Share2, Settings, Bell, Search
} from 'lucide-react'

export default function Dashboard() {
  const metrics = [
    { label: 'Total Revenue', value: '$124,563', change: '+12.5%', trend: 'up', icon: DollarSign },
    { label: 'Active Users', value: '8,423', change: '+8.2%', trend: 'up', icon: Users },
    { label: 'Conversion Rate', value: '3.24%', change: '-2.1%', trend: 'down', icon: TrendingUp },
    { label: 'Avg. Session', value: '4m 32s', change: '+5.3%', trend: 'up', icon: Activity },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      {/* Dashboard Header */}
      <div className="bg-white border-b border-gray-200 pt-24 pb-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 mb-2">Dashboard</h1>
              <p className="text-gray-600">Welcome back! Here's what's happening with your data today.</p>
            </div>
            <div className="flex gap-3 mt-4 sm:mt-0">
              <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors">
                <Download className="h-4 w-4 mr-2" />
                Export
              </button>
              <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors">
                <Share2 className="h-4 w-4 mr-2" />
                Share
              </button>
              <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors">
                <Settings className="h-4 w-4 mr-2" />
                Settings
              </button>
            </div>
          </div>

          {/* Search Bar */}
          <div className="relative max-w-md">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
            <input
              type="text"
              placeholder="Search dashboards, reports..."
              className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            />
          </div>
        </div>
      </div>

      {/* Main Dashboard Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Metrics Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          {metrics.map((metric, index) => {
            const Icon = metric.icon
            return (
              <div key={index} className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
                <div className="flex items-center justify-between mb-4">
                  <div className="p-2 bg-primary-100 rounded-lg">
                    <Icon className="h-5 w-5 text-primary-600" />
                  </div>
                  <span className={`text-sm font-medium flex items-center ${
                    metric.trend === 'up' ? 'text-green-600' : 'text-red-600'
                  }`}>
                    {metric.trend === 'up' ? (
                      <TrendingUp className="h-4 w-4 mr-1" />
                    ) : (
                      <TrendingDown className="h-4 w-4 mr-1" />
                    )}
                    {metric.change}
                  </span>
                </div>
                <div className="text-2xl font-bold text-gray-900 mb-1">{metric.value}</div>
                <div className="text-sm text-gray-600">{metric.label}</div>
              </div>
            )
          })}
        </div>

        {/* Charts Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
          {/* Revenue Chart */}
          <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-gray-900">Revenue Overview</h3>
              <select className="text-sm border border-gray-300 rounded-lg px-3 py-1">
                <option>Last 7 days</option>
                <option>Last 30 days</option>
                <option>Last 90 days</option>
              </select>
            </div>
            <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center">
              <LineChart className="h-16 w-16 text-gray-400" />
              <span className="ml-4 text-gray-500">Chart visualization placeholder</span>
            </div>
          </div>

          {/* User Growth Chart */}
          <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-gray-900">User Growth</h3>
              <select className="text-sm border border-gray-300 rounded-lg px-3 py-1">
                <option>Last 7 days</option>
                <option>Last 30 days</option>
                <option>Last 90 days</option>
              </select>
            </div>
            <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center">
              <BarChart3 className="h-16 w-16 text-gray-400" />
              <span className="ml-4 text-gray-500">Chart visualization placeholder</span>
            </div>
          </div>
        </div>

        {/* Bottom Row */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Distribution Chart */}
          <div className="lg:col-span-2 bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-gray-900">Traffic Sources</h3>
              <button className="text-sm text-primary-600 hover:text-primary-700">View all</button>
            </div>
            <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center">
              <PieChart className="h-16 w-16 text-gray-400" />
              <span className="ml-4 text-gray-500">Chart visualization placeholder</span>
            </div>
          </div>

          {/* Recent Activity */}
          <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
            <div className="flex justify-between items-center mb-6">
              <h3 className="text-lg font-semibold text-gray-900">Recent Activity</h3>
              <Bell className="h-5 w-5 text-gray-400" />
            </div>
            <div className="space-y-4">
              {[
                { action: 'New report generated', time: '2 min ago', type: 'report' },
                { action: 'Dashboard shared', time: '15 min ago', type: 'share' },
                { action: 'Data source updated', time: '1 hour ago', type: 'update' },
                { action: 'Alert triggered', time: '2 hours ago', type: 'alert' },
              ].map((activity, index) => (
                <div key={index} className="flex items-start">
                  <div className="w-2 h-2 bg-primary-600 rounded-full mt-2 mr-3"></div>
                  <div className="flex-1">
                    <p className="text-sm text-gray-900">{activity.action}</p>
                    <p className="text-xs text-gray-500">{activity.time}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      <Footer />
    </div>
  )
}
