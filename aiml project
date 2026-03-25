"""
Galaxy Classification AI - Complete Demo

This script demonstrates the entire galaxy classification pipeline.

"""

import os
import sys
import numpy as np
import pandas as pd

# Optional matplotlib import
try:
    import matplotlib.pyplot as plt
    HAS_PLOTTING = True
except ImportError:
    HAS_PLOTTING = False
    print("Note: matplotlib not available. Some visualizations will be skipped.")

# Add src directory to path
sys.path.append('src')

from data_loader import GalaxyDataLoader, ensure_data_dir
from model import GalaxyClassifier

# Optional import for evaluation
try:
    from evaluate import GalaxyModelEvaluator
    HAS_EVALUATOR = True
except ImportError:
    HAS_EVALUATOR = False
    print("Note: GalaxyModelEvaluator not available. Some evaluation features will be skipped.")

def main():
    """
    Complete demonstration of the galaxy classification AI system.
    """
    print("🌌" * 20)
    print("🌌 GALAXY CLASSIFICATION AI DEMO 🌌")
    print("🌌" * 20)
    print("Welcome to the complete demonstration!")
    print("This will show you how AI can classify galaxies.")
    print("=" * 50)
    
    # Step 1: Data Loading and Exploration
    print("\n📊 STEP 1: LOADING AND EXPLORING GALAXY DATA")
    print("-" * 50)
    
    loader = GalaxyDataLoader()
    data = loader.load_data()  # Will automatically use existing CSV files
    
    print(f"\n✅ Loaded {len(data)} galaxies!")
    if 'galaxy_type' in data.columns:
        print(f"Galaxy types: {data['galaxy_type'].value_counts().to_dict()}")
    else:
        print("Note: No galaxy_type column found in the data")
    
    # Step 2: Data Preparation
    print("\n🔧 STEP 2: PREPARING DATA FOR MACHINE LEARNING")
    print("-" * 50)
    
    X_train, X_test, y_train, y_test = loader.prepare_data()
    
    print(f"✅ Training set: {X_train.shape[0]} galaxies")
    print(f"✅ Test set: {X_test.shape[0]} galaxies")
    
    # Step 3: Model Training
    print("\n🤖 STEP 3: TRAINING MACHINE LEARNING MODELS")
    print("-" * 50)
    
    classifier = GalaxyClassifier()
    results = classifier.train_models(X_train, y_train, X_test, y_test, 
                                    loader.get_feature_names())
    
    print(f"\n✅ Best model: {classifier.best_model_name}")
    print(f"✅ Best accuracy: {results[classifier.best_model_name]:.3f}")
    
    # Step 4: Model Evaluation
    print("\n📈 STEP 4: EVALUATING MODEL PERFORMANCE")
    print("-" * 50)
    
    if HAS_EVALUATOR:
        evaluator = GalaxyModelEvaluator(model=classifier.best_model)
        metrics = evaluator.evaluate_model(X_test, y_test, classifier.best_model_name)
        print(f"✅ Final accuracy: {metrics['accuracy']:.3f}")
        
        # Step 5: Error Analysis
        print("\n🔍 STEP 5: ANALYZING ERRORS")
        print("-" * 50)
        evaluator.analyze_errors(X_test, y_test, loader.get_feature_names())
    else:
        print("✅ Model evaluation skipped - evaluator not available")
        print("✅ Error analysis skipped - evaluator not available")
    
    # Step 6: Demo Predictions
    print("\n🔮 STEP 6: DEMO PREDICTIONS")
    print("-" * 50)
    
    demo_predictions(X_test[:5], y_test[:5], classifier)
    
    # Step 7: Save Model
    print("\n💾 STEP 7: SAVING THE MODEL")
    print("-" * 50)
    
    model_path = "data/best_galaxy_model.pkl"
    classifier.save_model(model_path)
    print(f"✅ Model saved to: {model_path}")
    
    # Step 8: Create Sample Data for GUI
    print("\n📁 STEP 8: CREATING SAMPLE DATA FOR GUI")
    print("-" * 50)
    
    create_sample_csv(X_test[:10], y_test[:10], loader.get_feature_names())
    
    # Final Summary
    print("\n🎉 DEMO COMPLETE!")
    print("=" * 50)
    print("What you've learned:")
    print("✅ How to load and explore galaxy data")
    print("✅ How to prepare data for machine learning")
    print("✅ How to train multiple AI models")
    print("✅ How to evaluate model performance")
    print("✅ How to analyze errors and improve models")
    print("✅ How to make predictions on new galaxies")
    print("\nNext steps:")
    print("1. Run 'python src/gui.py' to try the interactive interface")
    print("2. Experiment with different galaxy features")
    print("3. Try training with real Galaxy Zoo data")
    print("4. Learn more about astronomy and machine learning!")
    print("=" * 50)

def demo_predictions(X_sample, y_sample, classifier):
    """Show example predictions."""
    print("Here are some example predictions:")
    print("-" * 30)
    
    for i, (features, true_label) in enumerate(zip(X_sample, y_sample)):
        prediction, confidence = classifier.predict(features)
        
        print(f"Galaxy {i+1}:")
        print(f"  True type: {true_label}")
        print(f"  Predicted: {prediction}")
        if confidence is not None:
            print(f"  Confidence: {confidence:.2f}")
        print(f"  Correct: {'✅' if prediction == true_label else '❌'}")
        print()

def create_sample_csv(X_sample, y_sample, feature_names):
    """Create a sample CSV file for GUI testing."""
    # Create DataFrame
    df = pd.DataFrame(X_sample, columns=feature_names)
    df['true_type'] = y_sample
    
    # Save to CSV
    ensure_data_dir()
    csv_path = "data/sample_galaxies.csv"
    df.to_csv(csv_path, index=False)
    print(f"✅ Sample data saved to: {csv_path}")
    print("You can use this file in the GUI for batch predictions!")

def show_educational_info():
    """Show educational information about galaxies and AI."""
    print("\n📚 EDUCATIONAL INFORMATION")
    print("-" * 50)
    print("🌌 What are galaxies?")
    print("Galaxies are huge collections of stars, gas, and dust.")
    print("Our Milky Way is just one of billions of galaxies!")
    print()
    print("🔬 How do we classify galaxies?")
    print("Astronomers use features like:")
    print("• Shape (spiral, elliptical, irregular)")
    print("• Color (blue = young stars, red = old stars)")
    print("• Size and brightness")
    print("• How concentrated the light is")
    print()
    print("🤖 How does AI help?")
    print("AI can automatically classify thousands of galaxies")
    print("much faster than humans can!")
    print("This helps astronomers study the universe more efficiently.")
    print()
    print("🎓 What you're learning:")
    print("• Machine learning concepts")
    print("• Data science techniques")
    print("• Astronomy and galaxy classification")
    print("• Python programming")
    print("• Data visualization")

if __name__ == "__main__":
    # Show educational info first
    show_educational_info()
    
    # Run the main demo
    main()
