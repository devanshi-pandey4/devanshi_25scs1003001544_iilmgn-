"""
Galaxy Classification AI - Main Runner

This is the main entry point for the Galaxy Classification AI project.

"""

import os
import sys
import subprocess

def print_banner():
    """Print the project banner."""
    print("🌌" * 25)
    print("🌌 GALAXY CLASSIFICATION AI 🌌")
    print("🌌" * 25)
    print("Welcome to the Galaxy Classification AI project!")
    print("=" * 50)

def print_menu():
    """Print the main menu."""
    print("\n📋 MAIN MENU")
    print("-" * 20)
    print("1. 🚀 Run Complete Demo")
    print("2. 🤖 Train AI Models")
    print("3. 🖥️  Open GUI Interface")
    print("4. 🧪 Run Tests")
    print("5. 📊 View Project Info")
    print("6. ❓ Help & Instructions")
    print("7. 🚪 Exit")
    print("-" * 20)

def run_demo():
    """Run the complete demonstration."""
    print("\n🚀 Running Complete Demo...")
    print("This will show you everything the project can do!")
    print("-" * 30)
    
    try:
        subprocess.run([sys.executable, "demo.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Demo failed: {e}")
    except FileNotFoundError:
        print("❌ demo.py not found!")

def train_models():
    """Train the AI models."""
    print("\n🤖 Training AI Models...")
    print("This will train multiple machine learning models.")
    print("-" * 30)
    
    try:
        subprocess.run([sys.executable, "src/train.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Training failed: {e}")
    except FileNotFoundError:
        print("❌ src/train.py not found!")

def open_gui():
    """Open the GUI interface."""
    print("\n🖥️  Opening GUI Interface...")
    print("This will open the interactive galaxy classification interface.")
    print("-" * 30)
    
    try:
        subprocess.run([sys.executable, "src/gui.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ GUI failed: {e}")
    except FileNotFoundError:
        print("❌ src/gui.py not found!")

def run_tests():
    """Run the test suite."""
    print("\n🧪 Running Tests...")
    print("This will test all project components.")
    print("-" * 30)
    
    try:
        subprocess.run([sys.executable, "test_project.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Tests failed: {e}")
    except FileNotFoundError:
        print("❌ test_project.py not found!")

def show_project_info():
    """Show project information."""
    print("\n📊 PROJECT INFORMATION")
    print("-" * 30)
    print("🌌 Galaxy Classification AI Project")
    print("📅 Version: 1.0")
    print("👨‍💻 Author: Team Error 404")
    print("📚 Purpose: Learn AI and Astronomy")
    print()
    print("📁 Project Structure:")
    print("├── data/          # Data storage")
    print("├── src/           # Source code")
    print("├── demo.py        # Complete demo")
    print("├── train.py       # Training script")
    print("├── gui.py         # GUI interface")
    print("└── README.md      # Documentation")
    print()
    print("🔬 Galaxy Types:")
    print("• Spiral Galaxies (like Milky Way)")
    print("• Elliptical Galaxies (round/oval)")
    print("• Irregular Galaxies (chaotic shapes)")
    print()
    print("🤖 AI Models:")
    print("• Random Forest")
    print("• Support Vector Machine")
    print("• Logistic Regression")
    print("• K-Nearest Neighbors")

def show_help():
    """Show help and instructions."""
    print("\n❓ HELP & INSTRUCTIONS")
    print("-" * 30)
    print("🎯 Getting Started:")
    print("1. First, run the Complete Demo to see everything")
    print("2. Then try training your own models")
    print("3. Use the GUI to classify galaxies interactively")
    print()
    print("📚 Learning Path:")
    print("1. Read README.md for detailed information")
    print("2. Look at the code comments to understand how it works")
    print("3. Experiment with different galaxy features")
    print("4. Try using real Galaxy Zoo data")
    print()
    print("🔧 Troubleshooting:")
    print("• Make sure you've installed requirements: pip install -r requirements.txt")
    print("• Run tests to check if everything is working")
    print("• Check the README.md for detailed instructions")
    print()
    print("📖 Key Files:")
    print("• README.md - Complete documentation")
    print("• demo.py - Complete demonstration")
    print("• src/train.py - Training script")
    print("• src/gui.py - Interactive interface")
    print("• test_project.py - Test suite")

def main():
    """Main function."""
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == "1":
                run_demo()
            elif choice == "2":
                train_models()
            elif choice == "3":
                open_gui()
            elif choice == "4":
                run_tests()
            elif choice == "5":
                show_project_info()
            elif choice == "6":
                show_help()
            elif choice == "7":
                print("\n👋 Thanks for using Galaxy Classification AI!")
                print("Happy galaxy hunting! 🌌✨")
                break
            else:
                print("❌ Invalid choice. Please enter 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

