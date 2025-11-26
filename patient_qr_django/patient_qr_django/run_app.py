import os
import sys
import subprocess
import webbrowser
import threading
import time

def open_browser():
    """Wait for server to start then open browser"""
    print("⏳ Waiting for server to start...")
    time.sleep(2)  # Give server a moment to start
    url = "http://127.0.0.1:8000/"
    print(f"🚀 Opening browser at {url}")
    webbrowser.open(url)

def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    
    print("="*50)
    print("🏥 Starting Hospital Management System...")
    print("="*50)

    # 1. Run Migrations (to ensure DB is ready)
    print("\n📦 Checking database...")
    try:
        subprocess.run([sys.executable, "manage.py", "migrate"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error running migrations. Please check your setup.")
        input("Press Enter to exit...")
        sys.exit(1)

    # 2. Start Browser in a separate thread
    threading.Thread(target=open_browser, daemon=True).start()

    # 3. Start Django Server
    print("\n⚡ Starting server...")
    print("❌ Press Ctrl+C to stop the server")
    try:
        subprocess.run([sys.executable, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
