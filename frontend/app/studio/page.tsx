import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { 
  Plus, Folder, FileText, BarChart3, Settings, 
  Search, Filter, Download, Share2, MoreVertical 
} from 'lucide-react'

export default function Studio() {
  const projects = [
    { name: 'Sales Analytics Q4', type: 'Dashboard', updated: '2 hours ago', color: 'bg-blue-500' },
    { name: 'Customer Segmentation', type: 'Analysis', updated: '1 day ago', color: 'bg-green-500' },
    { name: 'Marketing ROI Report', type: 'Report', updated: '3 days ago', color: 'bg-purple-500' },
    { name: 'Revenue Forecast', type: 'Model', updated: '1 week ago', color: 'bg-orange-500' },
    { name: 'User Behavior Analysis', type: 'Dashboard', updated: '2 weeks ago', color: 'bg-pink-500' },
    { name: 'Product Performance', type: 'Analysis', updated: '2 weeks ago', color: 'bg-indigo-500' },
  ]

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      {/* Header */}
      <div className="bg-white border-b border-gray-200 pt-24 pb-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 mb-2">Studio</h1>
              <p className="text-gray-600">Create, manage, and collaborate on your analytics projects</p>
            </div>
            <div className="flex gap-3 mt-4 sm:mt-0">
              <a
                href="/app"
                className="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-lg font-medium hover:bg-primary-700 transition-colors"
              >
                Launch Analytics
              </a>
              <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors">
                <Plus className="h-5 w-5 mr-2" />
                New Project
              </button>
            </div>
          </div>

          {/* Search and Filter */}
          <div className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1 relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input
                type="text"
                placeholder="Search projects..."
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              />
            </div>
            <button className="inline-flex items-center px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors">
              <Filter className="h-5 w-5 mr-2" />
              Filter
            </button>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Quick Stats */}
        <div className="grid grid-cols-1 sm:grid-cols-4 gap-4 mb-8">
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Total Projects</div>
            <div className="text-2xl font-bold text-gray-900">24</div>
          </div>
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Active Dashboards</div>
            <div className="text-2xl font-bold text-gray-900">12</div>
          </div>
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Shared Reports</div>
            <div className="text-2xl font-bold text-gray-900">8</div>
          </div>
          <div className="bg-white p-4 rounded-lg border border-gray-200">
            <div className="text-sm text-gray-600 mb-1">Team Members</div>
            <div className="text-2xl font-bold text-gray-900">6</div>
          </div>
        </div>

        {/* Projects Grid */}
        <div>
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-semibold text-gray-900">Recent Projects</h2>
            <div className="flex gap-2">
              <button className="p-2 border border-gray-300 rounded-lg hover:bg-gray-50">
                <Folder className="h-5 w-5 text-gray-600" />
              </button>
              <button className="p-2 border border-gray-300 rounded-lg hover:bg-gray-50">
                <BarChart3 className="h-5 w-5 text-gray-600" />
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {projects.map((project, index) => (
              <div
                key={index}
                className="bg-white rounded-xl border border-gray-200 hover:shadow-lg transition-all cursor-pointer group"
              >
                <div className={`h-32 ${project.color} rounded-t-xl`}></div>
                <div className="p-5">
                  <div className="flex justify-between items-start mb-2">
                    <div>
                      <h3 className="font-semibold text-gray-900 mb-1">{project.name}</h3>
                      <p className="text-sm text-gray-600">{project.type}</p>
                    </div>
                    <button className="opacity-0 group-hover:opacity-100 p-1 hover:bg-gray-100 rounded transition-opacity">
                      <MoreVertical className="h-5 w-5 text-gray-600" />
                    </button>
                  </div>
                  <p className="text-xs text-gray-500 mb-4">Updated {project.updated}</p>
                  <div className="flex gap-2">
                    <button className="flex-1 inline-flex items-center justify-center px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-50 transition-colors">
                      <Share2 className="h-4 w-4 mr-1" />
                      Share
                    </button>
                    <button className="flex-1 inline-flex items-center justify-center px-3 py-2 border border-gray-300 rounded-lg text-sm text-gray-700 hover:bg-gray-50 transition-colors">
                      <Download className="h-4 w-4 mr-1" />
                      Export
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Sidebar Placeholder for Workspace Tools */}
        <div className="mt-12 bg-white rounded-xl border border-gray-200 p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Workspace Tools</h3>
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <button className="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <FileText className="h-8 w-8 text-primary-600 mb-2" />
              <span className="text-sm text-gray-700">Reports</span>
            </button>
            <button className="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <BarChart3 className="h-8 w-8 text-primary-600 mb-2" />
              <span className="text-sm text-gray-700">Dashboards</span>
            </button>
            <button className="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <Settings className="h-8 w-8 text-primary-600 mb-2" />
              <span className="text-sm text-gray-700">Settings</span>
            </button>
            <button className="flex flex-col items-center p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
              <Folder className="h-8 w-8 text-primary-600 mb-2" />
              <span className="text-sm text-gray-700">Folders</span>
            </button>
          </div>
        </div>
      </div>

      <Footer />
    </div>
  )
}
