#!/usr/bin/env python3
"""
API Weaver - HTTP Thread Spinner (Standard Library version)
Weaving network requests into usable data tapestries...
Uses urllib (standard library) since external modules unavailable
"""

import urllib.request
import json
import ssl

class APIResponse:
    """A woven response object from an API call"""
    
    def __init__(self, status_code, headers, body):
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.successful = status_code < 400
    
    def to_dict(self):
        """Convert response to dictionary representation"""
        return {
            'status': self.status_code,
            'successful': self.successful,
            'content_length': len(self.body) if isinstance(self.body, (str, bytes)) else getattr(self.body, '__len__', lambda: 0),
            'headers_dict': dict(self.headers) if hasattr(self.headers, 'items') else {}
        }
    
    def to_json(self):
        """Convert response to JSON"""
        return json.dumps(self.to_dict(), indent=2)

class ThreadSpinner:
    """Main class for spinning HTTP threads using standard urllib"""
    
    def __init__(self, timeout=10):
        self.timeout = timeout
        
    def weave_thread(self, url, method='GET', headers=None, params=None):
        """Spin a single HTTP thread and weave the response using urllib"""
        
        try:
            # Create SSL context (avoiding certificate verification for simplicity)
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            
            # Prepare headers
            request_headers = {k.strip(): v.strip() for k, v in (headers or {}).items()}
            
            # Make the request using GET method
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Weaver-HTTP/1.0')
            if request_headers:
                for key, value in request_headers.items():
                    req.add_header(key, value)
            
            # Set timeout on the opener
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context))
            response = opener.open(req, timeout=self.timeout)
            
            status_code = response.getcode()
            body_bytes = response.read()  # Read once and store as bytes
            body_text = body_bytes.decode('utf-8')[:1024] if len(body_bytes) > 1024 else body_bytes.decode('utf-8')
            
            # Create woven response object
            api_response = APIResponse(status_code, {}, body_text)
            
            return {'status': 'success', 'response': api_response}
            
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def weave_multiple(self, urls):
        """Spin multiple threads sequentially"""
        
        results = []
        for url in urls:
            result = self.weave_thread(url)
            results.append(result)
        
        return results

def main():
    """Demonstrate API weaving capabilities using standard library urllib"""
    
    spinner = ThreadSpinner(timeout=15)
    
    print("API Weaver - HTTP Thread Spinner (urllib Standard Library)")
    print("=" * 50)
    print("\nWeaving test threads to public APIs...")
    print("(Using urllib standard library since external modules unavailable)")
    
    # Test URLs (public APIs we can use for demonstration)
    test_urls = [
        'https://httpbin.org/get',  # Simple echo service
        'https://jsonplaceholder.typicode.com/posts/1',  # JSON placeholder
        'https://api.github.com/repos/python/cpython',  # GitHub repo info
    ]
    
    results = spinner.weave_multiple(test_urls)
    
    for i, result in enumerate(results):
        if result['status'] == 'success':
            response = result['response']
            print(f"\nThread {i+1} Status: {response.status_code}")
            content_preview = str(response.body)[:200] if response.body else 'Empty'
            print(f"Content Preview (first 200 chars): {content_preview}...")
        else:
            print(f"\nThread {i+1} Error: {result['message']}")
    
    print("\n=== Weaving complete ===")

if __name__ == '__main__':
    main()