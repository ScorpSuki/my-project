import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import main

def test_main():
    """Негізгі функцияның жұмыс істеуін тексеру"""
    try:
        main()
        assert True
    except Exception as e:
        assert False, f"Қате орын алды: {e}"

def test_import():
    """Қосымшаның импортталуын тексеру"""
    try:
        import app
        assert hasattr(app, 'main')
    except ImportError:
        assert False, "app модулі табылмады"
