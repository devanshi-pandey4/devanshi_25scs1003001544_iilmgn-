#!/usr/bin/env python3
"""
Quick test to verify the project runs correctly
"""
import sys
import os

print("=" * 60)
print("Testing Galaxy Classification Project")
print("=" * 60)

# Test 1: Import check
print("\n[1/4] Testing imports...")
try:
    import numpy
    import pandas
    import sklearn
    print("✓ All core packages imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    sys.exit(1)

# Test 2: Module imports
print("\n[2/4] Testing project modules...")
try:
    sys.path.append('src')
    from data_loader import GalaxyDataLoader
    from model import GalaxyClassifier
    print("✓ Project modules imported successfully")
except ImportError as e:
    print(f"✗ Module import error: {e}")
    sys.exit(1)

# Test 3: Data loading
print("\n[3/4] Testing data loading...")
try:
    loader = GalaxyDataLoader()
    data = loader.create_sample_data()
    print(f"✓ Successfully created {len(data)} sample galaxies")
except Exception as e:
    print(f"✗ Data loading error: {e}")
    sys.exit(1)

# Test 4: Data preparation
print("\n[4/4] Testing data preparation...")
try:
    X_train, X_test, y_train, y_test = loader.prepare_data()
    if X_train is not None:
        print(f"✓ Data prepared: {X_train.shape[0]} training, {X_test.shape[0]} test samples")
    else:
        print("✗ Data preparation returned None")
        sys.exit(1)
except Exception as e:
    print(f"✗ Data preparation error: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED!")
print("=" * 60)
print("\nYou can now run:")
print("  - python demo.py          (Complete demo)")
print("  - python simple_demo.py   (Simple demo)")
print("  - python src/train.py     (Training script)")
print("  - python src/gui.py       (GUI interface)")
print("  - python run.py           (Main menu)")
print("=" * 60)
