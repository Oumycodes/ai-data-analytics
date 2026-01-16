'use client'

import { useEffect, useState } from 'react'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { ExternalLink, Loader2, AlertCircle, Play } from 'lucide-react'

export default function StreamlitApp() {
  const [isLoading, setIsLoading] = useState(true)
  const [streamlitAvailable, setStreamlitAvailable] = useState(false)
  const [showDirectLink, setShowDirectLink] = useState(false)
  const streamlitUrl = 'http://localhost:8501'

  useEffect(() => {
    // Check if Streamlit is running
    const checkStreamlit = async () => {
      try {
        const response = await fetch(streamlitUrl, { 
          mode: 'no-cors',
          method: 'HEAD'
        })
        setStreamlitAvailable(true)
        setIsLoading(false)
      } catch (error) {
        // Try to load iframe anyway - might work even if fetch fails
        setStreamlitAvailable(false)
        setIsLoading(false)
        setShowDirectLink(true)
      }
    }
    
    // Check immediately
    checkStreamlit()
    
    // Also check after a delay
    const timer = setTimeout(() => {
      if (isLoading) {
        setIsLoading(false)
        setShowDirectLink(true)
      }
    }, 3000)
    
    return () => clearTimeout(timer)
  }, [])

  const handleDirectAccess = () => {
    window.location.href = streamlitUrl
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />

      {/* Header */}
      <div className="bg-white border-b border-gray-200 pt-24 pb-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 mb-2">InsightForge Analytics</h1>
              <p className="text-gray-600">Upload data, ask questions, and get AI-powered insights</p>
            </div>
            <div className="flex gap-3 mt-4 sm:mt-0">
              <button
                onClick={handleDirectAccess}
                className="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-lg font-medium hover:bg-primary-700 transition-colors"
              >
                <Play className="h-4 w-4 mr-2" />
                Open Analytics App
              </button>
              <a
                href={streamlitUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-4 py-2 border border-gray-300 text-gray-700 rounded-lg font-medium hover:bg-gray-50 transition-colors"
              >
                <ExternalLink className="h-4 w-4 mr-2" />
                New Tab
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* Streamlit App Embed */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {showDirectLink && !streamlitAvailable ? (
          <div className="bg-white rounded-xl border-2 border-red-200 p-12 flex flex-col items-center justify-center min-h-[600px]">
            <AlertCircle className="h-16 w-16 text-red-500 mb-4" />
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Streamlit App Not Running</h2>
            <p className="text-gray-600 mb-6 text-center max-w-md">
              The analytics app needs to be started first. Click the button below to open it directly, 
              or start Streamlit in your terminal.
            </p>
            <button
              onClick={handleDirectAccess}
              className="inline-flex items-center px-6 py-3 bg-primary-600 text-white rounded-lg font-semibold hover:bg-primary-700 transition-colors mb-6"
            >
              <Play className="h-5 w-5 mr-2" />
              Open Analytics App
            </button>
            <div className="bg-blue-50 border border-blue-200 rounded-xl p-6 w-full max-w-2xl">
              <h3 className="text-lg font-semibold text-blue-900 mb-3">How to Start:</h3>
              <ol className="list-decimal list-inside space-y-2 text-blue-800">
                <li className="mb-2">
                  Open a terminal and navigate to: 
                  <code className="bg-blue-100 px-2 py-1 rounded ml-2">/Users/oumyb/Desktop/ai-data-analytics</code>
                </li>
                <li className="mb-2">
                  Run: <code className="bg-blue-100 px-2 py-1 rounded">streamlit run app.py</code>
                </li>
                <li className="mb-2">
                  Wait for: <code className="bg-blue-100 px-2 py-1 rounded">Local URL: http://localhost:8501</code>
                </li>
                <li>
                  Then refresh this page or click "Open Analytics App" above
                </li>
              </ol>
            </div>
          </div>
        ) : (
          <>
            <div className="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden mb-6">
              <iframe
                src={streamlitUrl}
                className="w-full h-[calc(100vh-250px)] min-h-[800px] border-0"
                title="InsightForge Analytics"
                allow="clipboard-read; clipboard-write"
                onLoad={() => {
                  setIsLoading(false)
                  setStreamlitAvailable(true)
                }}
                onError={() => {
                  setIsLoading(false)
                  setShowDirectLink(true)
                }}
              />
            </div>
            
            {isLoading && (
              <div className="bg-white rounded-xl border border-gray-200 p-8 flex items-center justify-center">
                <Loader2 className="h-8 w-8 text-primary-600 animate-spin mr-4" />
                <p className="text-gray-600">Loading analytics app...</p>
              </div>
            )}

            {/* Quick Help */}
            <div className="bg-blue-50 border border-blue-200 rounded-xl p-6">
              <h3 className="text-lg font-semibold text-blue-900 mb-2">💡 What You Can Do Here:</h3>
              <ul className="list-disc list-inside space-y-2 text-blue-800">
                <li><strong>Upload CSV files</strong> - Click "Upload New Dataset" to analyze your data</li>
                <li><strong>Ask questions</strong> - Type questions like "What is the average revenue by month?"</li>
                <li><strong>Get insights</strong> - Click "Generate Insights" for automatic analysis</li>
                <li><strong>Create visualizations</strong> - AI automatically creates charts based on your questions</li>
                <li><strong>Generate summaries</strong> - Create executive summaries with one click</li>
              </ul>
              <p className="mt-4 text-sm text-blue-700">
                <strong>Note:</strong> For AI-powered features, enter your Claude API key in the sidebar. 
                Get one at <a href="https://console.anthropic.com" target="_blank" rel="noopener noreferrer" className="underline">console.anthropic.com</a>
              </p>
            </div>
          </>
        )}
      </div>

      <Footer />
    </div>
  )
}
