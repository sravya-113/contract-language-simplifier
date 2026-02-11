"""
Glossary and Term Highlighting Service
Identifies and highlights legal terms with explanations
"""

import re
from typing import List, Dict, Set
from models import db, Glossary


class GlossaryService:
    """Handles legal term identification and highlighting"""
    
    # Common legal terms (default glossary)
    DEFAULT_LEGAL_TERMS = {
        'plaintiff': 'The person or party who brings a lawsuit to court',
        'defendant': 'The person or party being sued or accused in a court case',
        'jurisdiction': 'The official power to make legal decisions and judgments',
        'liability': 'Legal responsibility for something, especially for damages or debt',
        'indemnify': 'To compensate someone for harm or loss',
        'arbitration': 'The use of an arbitrator to settle a dispute outside of court',
        'breach': 'A violation or breaking of a law, obligation, or agreement',
        'covenant': 'A formal agreement or promise in a contract',
        'damages': 'Money claimed by or awarded to a person in compensation for loss or injury',
        'force majeure': 'Unforeseeable circumstances that prevent someone from fulfilling a contract',
        'indemnification': 'Security or protection against a loss or other financial burden',
        'injunction': 'A court order requiring someone to do or stop doing something',
        'lien': 'A legal right to keep possession of property until a debt is paid',
        'litigation': 'The process of taking legal action through the courts',
        'negligence': 'Failure to take proper care in doing something',
        'precedent': 'An earlier event or action used as an example or guide',
        'remedy': 'A means of legal reparation',
        'statute': 'A written law passed by a legislative body',
        'tort': 'A wrongful act or infringement of a right leading to legal liability',
        'warranty': 'A written guarantee promising to repair or replace a product',
        'affidavit': 'A written statement confirmed by oath for use as evidence in court',
        'allegation': 'A claim that someone has done something illegal or wrong',
        'appellant': 'A person who applies to a higher court for a reversal of a decision',
        'bailiff': 'An officer in a court of law who keeps order',
        'certiorari': 'A writ by which a higher court reviews a decision of a lower court',
        'consideration': 'Something of value exchanged between parties in a contract',
        'deposition': 'The process of giving sworn evidence',
        'estoppel': 'A principle that prevents someone from contradicting previous statements',
        'fiduciary': 'A person who holds a legal or ethical relationship of trust',
        'garnishment': 'A legal process for collecting a debt by taking money from wages',
        'hearsay': 'Information received from others that cannot be substantiated',
        'intestate': 'Having made no valid will',
        'jurisprudence': 'The theory or philosophy of law',
        'malfeasance': 'Wrongdoing, especially by a public official',
        'notary': 'A person authorized to perform certain legal formalities',
        'ordinance': 'A piece of legislation enacted by a municipal authority',
        'perjury': 'The offense of willfully telling an untruth in court',
        'probate': 'The official proving of a will',
        'subpoena': 'A writ ordering a person to attend a court',
        'testator': 'A person who has made a will',
        'venue': 'The place where a trial or other legal proceeding is held'
    }
    
    def __init__(self):
        """Initialize glossary service"""
        self.default_terms = self.DEFAULT_LEGAL_TERMS
    
    def get_all_terms(self) -> Dict[str, str]:
        """
        Get all terms from database and default glossary
        
        Returns:
            Dictionary of terms and their explanations
        """
        terms = self.default_terms.copy()
        
        # Add terms from database
        try:
            db_terms = Glossary.query.all()
            for term_obj in db_terms:
                terms[term_obj.term.lower()] = term_obj.simplified_explanation
        except Exception as e:
            print(f"Error fetching glossary from database: {e}")
        
        return terms
    
    def identify_terms(self, text: str) -> List[Dict[str, any]]:
        """
        Identify legal terms in text
        
        Args:
            text: Input text
            
        Returns:
            List of identified terms with positions and explanations
        """
        terms = self.get_all_terms()
        identified = []
        text_lower = text.lower()
        
        for term, explanation in terms.items():
            # Find all occurrences of the term
            pattern = r'\b' + re.escape(term) + r'\b'
            matches = re.finditer(pattern, text_lower, re.IGNORECASE)
            
            for match in matches:
                identified.append({
                    'term': text[match.start():match.end()],  # Preserve original case
                    'explanation': explanation,
                    'start': match.start(),
                    'end': match.end()
                })
        
        # Sort by position
        identified.sort(key=lambda x: x['start'])
        
        return identified
    
    def highlight_terms(self, text: str, identified_terms: List[Dict[str, any]] = None) -> str:
        """
        Highlight legal terms in HTML
        
        Args:
            text: Input text
            identified_terms: Pre-identified terms (optional)
            
        Returns:
            HTML with highlighted terms
        """
        if identified_terms is None:
            identified_terms = self.identify_terms(text)
        
        if not identified_terms:
            return text
        
        # Build HTML with highlights
        result = []
        last_pos = 0
        
        for term_info in identified_terms:
            # Add text before term
            result.append(text[last_pos:term_info['start']])
            
            # Add highlighted term with tooltip
            term_html = (
                f'<span class="legal-term" '
                f'data-toggle="tooltip" '
                f'title="{term_info["explanation"]}">'
                f'{term_info["term"]}'
                f'</span>'
            )
            result.append(term_html)
            
            last_pos = term_info['end']
        
        # Add remaining text
        result.append(text[last_pos:])
        
        return ''.join(result)
    
    def add_term(self, term: str, explanation: str, user_id: int, category: str = None) -> Glossary:
        """
        Add new term to glossary database
        
        Args:
            term: Legal term
            explanation: Simplified explanation
            user_id: ID of user adding the term
            category: Optional category
            
        Returns:
            Created Glossary object
        """
        glossary_entry = Glossary(
            term=term.lower(),
            simplified_explanation=explanation,
            created_by=user_id,
            category=category
        )
        
        db.session.add(glossary_entry)
        db.session.commit()
        
        return glossary_entry
    
    def update_term(self, term_id: int, explanation: str = None, category: str = None) -> Glossary:
        """
        Update existing glossary term
        
        Args:
            term_id: ID of term to update
            explanation: New explanation (optional)
            category: New category (optional)
            
        Returns:
            Updated Glossary object
        """
        term = Glossary.query.get(term_id)
        
        if not term:
            raise ValueError(f"Term with ID {term_id} not found")
        
        if explanation:
            term.simplified_explanation = explanation
        if category:
            term.category = category
        
        db.session.commit()
        
        return term
    
    def delete_term(self, term_id: int) -> bool:
        """
        Delete term from glossary
        
        Args:
            term_id: ID of term to delete
            
        Returns:
            True if deleted successfully
        """
        term = Glossary.query.get(term_id)
        
        if not term:
            return False
        
        db.session.delete(term)
        db.session.commit()
        
        return True
    
    def search_terms(self, query: str) -> List[Glossary]:
        """
        Search for terms in glossary
        
        Args:
            query: Search query
            
        Returns:
            List of matching Glossary objects
        """
        return Glossary.query.filter(
            Glossary.term.ilike(f'%{query}%')
        ).all()


# Singleton instance
_glossary_service = None

def get_glossary_service() -> GlossaryService:
    """Get or create singleton glossary service instance"""
    global _glossary_service
    if _glossary_service is None:
        _glossary_service = GlossaryService()
    return _glossary_service
