"""
Readability Scoring Service
Calculates various readability metrics for text analysis
"""

import textstat
from typing import Dict


class ReadabilityAnalyzer:
    """Analyzes text readability using multiple metrics"""
    
    def __init__(self):
        """Initialize readability analyzer"""
        textstat.set_lang('en')
    
    def flesch_kincaid_grade(self, text: str) -> float:
        """
        Calculate Flesch-Kincaid Grade Level
        Indicates the US school grade level required to understand the text
        
        Args:
            text: Input text
            
        Returns:
            Grade level (e.g., 12.5 means 12th grade)
        """
        try:
            return textstat.flesch_kincaid_grade(text)
        except Exception:
            return 0.0
    
    def gunning_fog_index(self, text: str) -> float:
        """
        Calculate Gunning Fog Index
        Estimates years of formal education needed to understand text
        
        Args:
            text: Input text
            
        Returns:
            Fog index score
        """
        try:
            return textstat.gunning_fog(text)
        except Exception:
            return 0.0
    
    def flesch_reading_ease(self, text: str) -> float:
        """
        Calculate Flesch Reading Ease score
        Higher scores indicate easier readability (0-100 scale)
        
        Args:
            text: Input text
            
        Returns:
            Reading ease score (0-100)
        """
        try:
            return textstat.flesch_reading_ease(text)
        except Exception:
            return 0.0
    
    def smog_index(self, text: str) -> float:
        """
        Calculate SMOG (Simple Measure of Gobbledygook) Index
        
        Args:
            text: Input text
            
        Returns:
            SMOG index score
        """
        try:
            return textstat.smog_index(text)
        except Exception:
            return 0.0
    
    def automated_readability_index(self, text: str) -> float:
        """
        Calculate Automated Readability Index (ARI)
        
        Args:
            text: Input text
            
        Returns:
            ARI score
        """
        try:
            return textstat.automated_readability_index(text)
        except Exception:
            return 0.0
    
    def coleman_liau_index(self, text: str) -> float:
        """
        Calculate Coleman-Liau Index
        
        Args:
            text: Input text
            
        Returns:
            Coleman-Liau score
        """
        try:
            return textstat.coleman_liau_index(text)
        except Exception:
            return 0.0
    
    def interpret_grade_level(self, grade: float) -> str:
        """
        Interpret grade level into human-readable description
        
        Args:
            grade: Grade level score
            
        Returns:
            Interpretation string
        """
        if grade < 6:
            return "Very Easy (Elementary School)"
        elif grade < 9:
            return "Easy (Middle School)"
        elif grade < 12:
            return "Fairly Easy (High School)"
        elif grade < 14:
            return "Standard (College Freshman)"
        elif grade < 16:
            return "Fairly Difficult (College)"
        elif grade < 18:
            return "Difficult (College Graduate)"
        else:
            return "Very Difficult (Professional/Academic)"
    
    def interpret_reading_ease(self, score: float) -> str:
        """
        Interpret Flesch Reading Ease score
        
        Args:
            score: Reading ease score (0-100)
            
        Returns:
            Interpretation string
        """
        if score >= 90:
            return "Very Easy (5th grade)"
        elif score >= 80:
            return "Easy (6th grade)"
        elif score >= 70:
            return "Fairly Easy (7th grade)"
        elif score >= 60:
            return "Standard (8th-9th grade)"
        elif score >= 50:
            return "Fairly Difficult (10th-12th grade)"
        elif score >= 30:
            return "Difficult (College)"
        else:
            return "Very Difficult (College Graduate)"
    
    def analyze(self, text: str) -> Dict[str, any]:
        """
        Perform complete readability analysis
        
        Args:
            text: Input text
            
        Returns:
            Dictionary with all readability metrics and interpretations
        """
        if not text or len(text.strip()) < 10:
            return {
                'flesch_kincaid_grade': 0.0,
                'gunning_fog': 0.0,
                'flesch_reading_ease': 0.0,
                'smog_index': 0.0,
                'automated_readability_index': 0.0,
                'coleman_liau_index': 0.0,
                'grade_interpretation': 'Text too short to analyze',
                'ease_interpretation': 'Text too short to analyze'
            }
        
        fk_grade = self.flesch_kincaid_grade(text)
        fog = self.gunning_fog_index(text)
        ease = self.flesch_reading_ease(text)
        smog = self.smog_index(text)
        ari = self.automated_readability_index(text)
        cli = self.coleman_liau_index(text)
        
        return {
            'flesch_kincaid_grade': round(fk_grade, 2),
            'gunning_fog': round(fog, 2),
            'flesch_reading_ease': round(ease, 2),
            'smog_index': round(smog, 2),
            'automated_readability_index': round(ari, 2),
            'coleman_liau_index': round(cli, 2),
            'grade_interpretation': self.interpret_grade_level(fk_grade),
            'ease_interpretation': self.interpret_reading_ease(ease)
        }


# Singleton instance
_analyzer = None

def get_readability_analyzer() -> ReadabilityAnalyzer:
    """Get or create singleton analyzer instance"""
    global _analyzer
    if _analyzer is None:
        _analyzer = ReadabilityAnalyzer()
    return _analyzer
