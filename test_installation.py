"""
Test script for Contract Language Simplifier
Run this to verify the installation and basic functionality
"""

import sys
import os

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    
    try:
        import flask
        print("✓ Flask installed")
    except ImportError:
        print("✗ Flask not installed")
        return False
    
    try:
        import transformers
        print("✓ Transformers installed")
    except ImportError:
        print("✗ Transformers not installed")
        return False
    
    try:
        import spacy
        print("✓ spaCy installed")
    except ImportError:
        print("✗ spaCy not installed")
        return False
    
    try:
        import nltk
        print("✓ NLTK installed")
    except ImportError:
        print("✗ NLTK not installed")
        return False
    
    try:
        import textstat
        print("✓ textstat installed")
    except ImportError:
        print("✗ textstat not installed")
        return False
    
    return True


def test_spacy_model():
    """Test if spaCy model is downloaded"""
    print("\nTesting spaCy model...")
    
    try:
        import spacy
        nlp = spacy.load('en_core_web_sm')
        print("✓ spaCy model 'en_core_web_sm' loaded successfully")
        return True
    except OSError:
        print("✗ spaCy model 'en_core_web_sm' not found")
        print("  Run: python -m spacy download en_core_web_sm")
        return False


def test_nltk_data():
    """Test if NLTK data is downloaded"""
    print("\nTesting NLTK data...")
    
    try:
        import nltk
        nltk.data.find('tokenizers/punkt')
        print("✓ NLTK 'punkt' data found")
        return True
    except LookupError:
        print("✗ NLTK 'punkt' data not found")
        print("  Run: python -c \"import nltk; nltk.download('punkt')\"")
        return False


def test_database():
    """Test database creation"""
    print("\nTesting database...")
    
    try:
        from app import app, db
        with app.app_context():
            db.create_all()
        print("✓ Database tables created successfully")
        return True
    except Exception as e:
        print(f"✗ Database error: {e}")
        return False


def test_services():
    """Test NLP services"""
    print("\nTesting NLP services...")
    
    try:
        from services.preprocessing import get_preprocessor
        preprocessor = get_preprocessor()
        print("✓ Preprocessing service initialized")
    except Exception as e:
        print(f"✗ Preprocessing service error: {e}")
        return False
    
    try:
        from services.readability import get_readability_analyzer
        analyzer = get_readability_analyzer()
        print("✓ Readability analyzer initialized")
    except Exception as e:
        print(f"✗ Readability analyzer error: {e}")
        return False
    
    try:
        from services.glossary import get_glossary_service
        glossary = get_glossary_service()
        print("✓ Glossary service initialized")
    except Exception as e:
        print(f"✗ Glossary service error: {e}")
        return False
    
    return True


def test_sample_text():
    """Test with sample legal text"""
    print("\nTesting with sample text...")
    
    sample_text = """
    The party of the first part hereby agrees to indemnify and hold harmless 
    the party of the second part from any and all claims, damages, losses, 
    and expenses arising out of or resulting from the performance of this agreement.
    """
    
    try:
        from services.preprocessing import get_preprocessor
        from services.readability import get_readability_analyzer
        
        preprocessor = get_preprocessor()
        analyzer = get_readability_analyzer()
        
        # Preprocess
        result = preprocessor.preprocess(sample_text)
        print(f"  Word count: {result['word_count']}")
        print(f"  Sentence count: {result['sentence_count']}")
        
        # Readability
        readability = analyzer.analyze(sample_text)
        print(f"  Flesch-Kincaid Grade: {readability['flesch_kincaid_grade']}")
        print(f"  Interpretation: {readability['grade_interpretation']}")
        
        print("✓ Sample text processing successful")
        return True
        
    except Exception as e:
        print(f"✗ Sample text processing error: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("Contract Language Simplifier - Installation Test")
    print("=" * 60)
    
    tests = [
        ("Package Imports", test_imports),
        ("spaCy Model", test_spacy_model),
        ("NLTK Data", test_nltk_data),
        ("Database", test_database),
        ("NLP Services", test_services),
        ("Sample Processing", test_sample_text),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ {name} failed with error: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nPassed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! Your installation is ready.")
        print("Run 'python app.py' to start the application.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
