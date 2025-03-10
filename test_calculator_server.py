#!/usr/bin/env python3
"""
Test suite for the MCP Calculator Server

This script runs all doctests in the calculator_server.py file
and provides feedback on whether the tests passed or failed.
"""

import doctest
import sys
from calculator_server import app

def run_doctests():
    """
    Run doctests for all functions in calculator_server.py
    """
    # Find all available functions/tools in the app
    tools = [tool.func for tool in app.tools]
    
    # Count tests and results
    total_tests = 0
    total_failures = 0
    
    print("Running doctests for MCP Calculator Server...")
    print("=" * 50)
    
    # Test each function individually
    for tool in tools:
        result = doctest.testmod(
            sys.modules[tool.__module__],
            name=tool.__name__,
            globs={tool.__name__: tool}
        )
        
        status = "✓ PASSED" if result.failed == 0 else "✗ FAILED"
        print(f"{status}: {tool.__name__} ({result.attempted} tests, {result.failed} failures)")
        
        total_tests += result.attempted
        total_failures += result.failed
    
    # Print summary
    print("\nSUMMARY")
    print("=" * 50)
    print(f"Total tests: {total_tests}")
    print(f"Failed: {total_failures}")
    print(f"Success: {total_tests - total_failures}")
    print("=" * 50)
    print("RESULT: " + ("SUCCESS" if total_failures == 0 else "FAILURE"))
    
    return total_failures == 0

if __name__ == "__main__":
    success = run_doctests()
    sys.exit(0 if success else 1)
