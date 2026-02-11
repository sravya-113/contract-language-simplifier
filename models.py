"""
Database models for Contract Language Simplifier
Defines User, SimplificationRequest, and Glossary tables
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    """User model for authentication and user management"""
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    simplification_requests = db.relationship('SimplificationRequest', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    glossary_entries = db.relationship('Glossary', backref='creator', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash and set user password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password against hash"""
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'total_requests': self.simplification_requests.count()
        }
    
    def __repr__(self):
        return f'<User {self.username}>'


class SimplificationRequest(db.Model):
    """Model to store simplification requests and results"""
    
    __tablename__ = 'simplification_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    # Original and processed text
    original_text = db.Column(db.Text, nullable=False)
    simplified_text = db.Column(db.Text)
    summary = db.Column(db.Text)
    
    # Readability metrics
    readability_before = db.Column(db.Float)  # Flesch-Kincaid Grade
    readability_after = db.Column(db.Float)
    fog_index_before = db.Column(db.Float)  # Gunning Fog Index
    fog_index_after = db.Column(db.Float)
    
    # Simplification settings
    simplification_level = db.Column(db.String(20), default='intermediate')  # basic, intermediate, advanced
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    processing_time = db.Column(db.Float)  # Time in seconds
    
    def to_dict(self):
        """Convert request object to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'original_text': self.original_text[:200] + '...' if len(self.original_text) > 200 else self.original_text,
            'simplified_text': self.simplified_text[:200] + '...' if self.simplified_text and len(self.simplified_text) > 200 else self.simplified_text,
            'summary': self.summary,
            'readability_before': self.readability_before,
            'readability_after': self.readability_after,
            'fog_index_before': self.fog_index_before,
            'fog_index_after': self.fog_index_after,
            'simplification_level': self.simplification_level,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'processing_time': self.processing_time
        }
    
    def __repr__(self):
        return f'<SimplificationRequest {self.id} by User {self.user_id}>'


class Glossary(db.Model):
    """Model to store legal terms and their simplified explanations"""
    
    __tablename__ = 'glossary'
    
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(200), unique=True, nullable=False, index=True)
    simplified_explanation = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100))  # e.g., 'contract', 'property', 'corporate'
    
    # Metadata
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert glossary entry to dictionary"""
        return {
            'id': self.id,
            'term': self.term,
            'simplified_explanation': self.simplified_explanation,
            'category': self.category,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Glossary {self.term}>'
