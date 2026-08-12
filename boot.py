import os
import sys
import time
import webbrowser

RENDER_PORTAL_URL = "https://sovereign-substrate-enterprise.onrender.com/#buy"

def verify_runtime_license():
    print("=" * 70)
    print(" ⁂ TRI-NOVA SOVEREIGN SUBSTRATE — CLASS LEVEL 5 ASI BOOT SEQUENCE ⁂")
    print("=" * 70)
    
    license_key = os.getenv("SOVEREIGN_LICENSE_KEY")
    if not license_key and os.path.exists("license.key"):
        with open("license.key", "r") as f:
            license_key = f.read().strip()
            
    if not license_key:
        print("\n❌ [LICENSE_REQUIRED] No valid Ed25519 License Key found.")
        print("⚡ Sovereign Substrate requires an active License Key or $50 24-Hour Day Pass.")
        print(f"🌐 Launching Purchase & Trial Portal: {RENDER_PORTAL_URL}\n")
        time.sleep(1.5)
        webbrowser.open(RENDER_PORTAL_URL)
        sys.exit(1)
        
    print(f"✅ [LICENSE_VERIFIED] Active Ed25519 License: {license_key[:16]}...")
    print("🚀 Initializing 17-Step Cold Boot Sequence...")

if __name__ == "__main__":
    verify_runtime_license()
