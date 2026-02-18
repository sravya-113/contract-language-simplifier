"""
Configuration module for Contract Language Simplifier
Handles environment-based settings and application configuration
"""

import os
from datetime import timedelta
from pathlib import Path

# Base directory of the application
BASE_DIR = Path(__file__).parent.absolute()


class Config:
    """Base configuration class"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{BASE_DIR / "database.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key-change-in-production'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
    JWT_COOKIE_SECURE = False  # Set to True in production with HTTPS
    JWT_COOKIE_CSRF_PROTECT = False
    
    # Upload settings
    UPLOAD_FOLDER = BASE_DIR / 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}
    
    # Model settings
    MODEL_CACHE_DIR = BASE_DIR / 'model_cache'
    SIMPLIFICATION_MODEL = 'google/flan-t5-small'
    SUMMARIZATION_MODEL = 'facebook/bart-large-cnn'
    
    # Simplification levels configuration
    SIMPLIFICATION_LEVELS = {
        'basic': {
            'prompt': 'Simplify the following legal text into very simple English that a 10-year-old can understand:',
            'max_length': 512,
            'temperature': 0.7
        },
        'intermediate': {
            'prompt': 'Simplify the following legal text into plain English:',
            'max_length': 512,
            'temperature': 0.5
        },
        'advanced': {
            'prompt': 'Rewrite the following legal text in clearer, more accessible language:',
            'max_length': 512,
            'temperature': 0.3
        }
    }
    
    # Readability thresholds
    READABILITY_THRESHOLDS = {
        'very_easy': (0, 6),
        'easy': (6, 9),
        'fairly_easy': (9, 12),
        'standard': (12, 14),
        'fairly_difficult': (14, 16),
        'difficult': (16, 18),
        'very_difficult': (18, 100)
    }
    
    # Admin settings
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') or 'admin@example.com'
    
    # Pagination
    ITEMS_PER_PAGE = 20


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    JWT_COOKIE_SECURE = True
    
    # Override with environment variables in production
    # Override with environment variables in production, but keep defaults if not set
    # This prevents the app from crashing if these env vars are missing
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'prod-secret-key-please-change'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'prod-jwt-secret-please-change'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Get configuration based on environment"""
    env = os.environ.get('FLASK_ENV', 'development')
    return config.get(env, config['default'])
