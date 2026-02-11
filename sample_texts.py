"""
Sample legal text for testing the Contract Language Simplifier
"""

SAMPLE_CONTRACT = """
TERMS AND CONDITIONS OF SERVICE

1. DEFINITIONS AND INTERPRETATION
In these Terms and Conditions, unless the context otherwise requires, the following expressions 
shall have the following meanings:

"Agreement" means the agreement between the Company and the Client for the provision of Services 
pursuant to these Terms and Conditions;

"Client" means the person, firm, or company who purchases Services from the Company;

"Company" means Contract Language Simplifier Inc., a corporation duly incorporated under the laws 
of the jurisdiction;

"Services" means the services to be provided by the Company to the Client as set forth in the 
applicable Statement of Work;

2. INDEMNIFICATION
The Client agrees to indemnify, defend, and hold harmless the Company, its officers, directors, 
employees, agents, and affiliates from and against any and all claims, damages, obligations, 
losses, liabilities, costs, and expenses (including but not limited to attorney's fees) arising 
from: (i) Client's use of and access to the Services; (ii) Client's violation of any term of 
this Agreement; (iii) Client's violation of any third party right, including without limitation 
any copyright, property, or privacy right.

3. LIMITATION OF LIABILITY
IN NO EVENT SHALL THE COMPANY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, 
OR PUNITIVE DAMAGES, INCLUDING WITHOUT LIMITATION, LOSS OF PROFITS, DATA, USE, GOODWILL, OR 
OTHER INTANGIBLE LOSSES, RESULTING FROM (i) YOUR ACCESS TO OR USE OF OR INABILITY TO ACCESS OR 
USE THE SERVICES; (ii) ANY CONDUCT OR CONTENT OF ANY THIRD PARTY ON THE SERVICES; (iii) ANY 
CONTENT OBTAINED FROM THE SERVICES; AND (iv) UNAUTHORIZED ACCESS, USE, OR ALTERATION OF YOUR 
TRANSMISSIONS OR CONTENT, WHETHER BASED ON WARRANTY, CONTRACT, TORT (INCLUDING NEGLIGENCE), OR 
ANY OTHER LEGAL THEORY.

4. FORCE MAJEURE
Neither party shall be liable for any failure or delay in performing its obligations under this 
Agreement to the extent that such failure or delay is caused by a Force Majeure Event. A "Force 
Majeure Event" means any event beyond a party's reasonable control, including but not limited to 
strikes, lock-outs, or other industrial disputes, failure of a utility service or transport 
network, act of God, war, riot, civil commotion, malicious damage, compliance with any law or 
governmental order, rule, regulation or direction, accident, breakdown of plant or machinery, 
fire, flood, or storm.

5. GOVERNING LAW AND JURISDICTION
This Agreement shall be governed by and construed in accordance with the laws of the jurisdiction, 
without regard to its conflict of law provisions. The parties hereby submit to the exclusive 
jurisdiction of the courts of the jurisdiction for the resolution of any disputes arising out of 
or in connection with this Agreement.

6. SEVERABILITY
If any provision of this Agreement is held to be invalid, illegal, or unenforceable in any respect, 
such invalidity, illegality, or unenforceability shall not affect any other provision hereof, and 
this Agreement shall be construed as if such invalid, illegal, or unenforceable provision had never 
been contained herein.

7. ENTIRE AGREEMENT
This Agreement constitutes the entire agreement between the parties with respect to the subject 
matter hereof and supersedes all prior or contemporaneous understandings, agreements, 
representations, and warranties, both written and oral, with respect to such subject matter.
"""

SAMPLE_PRIVACY_POLICY = """
PRIVACY POLICY

This Privacy Policy describes how we collect, use, and disclose your Personal Information when 
you visit or make a purchase from the Site.

COLLECTING PERSONAL INFORMATION
When you visit the Site, we collect certain information about your device, your interaction with 
the Site, and information necessary to process your purchases. We may also collect additional 
information if you contact us for customer support. In this Privacy Policy, we refer to any 
information that can uniquely identify an individual (including the information below) as 
"Personal Information". See the list below for more information about what Personal Information 
we collect and why.

SHARING PERSONAL INFORMATION
We share your Personal Information with service providers to help us provide our services and 
fulfill our contracts with you, as described above. For example, we use Shopify to power our 
online store. We also use Google Analytics to help us understand how our customers use the Site. 
We may share your Personal Information to comply with applicable laws and regulations, to respond 
to a subpoena, search warrant or other lawful request for information we receive, or to otherwise 
protect our rights.

YOUR RIGHTS
If you are a resident of the European Economic Area, you have the right to access the Personal 
Information we hold about you, to port it to a new service, and to ask that your Personal 
Information be corrected, updated, or erased. If you would like to exercise these rights, please 
contact us through the contact information below.
"""

if __name__ == "__main__":
    print("Sample Legal Texts for Testing")
    print("=" * 60)
    print("\n1. Sample Contract")
    print(f"Length: {len(SAMPLE_CONTRACT)} characters")
    print(f"Preview: {SAMPLE_CONTRACT[:200]}...")
    print("\n2. Sample Privacy Policy")
    print(f"Length: {len(SAMPLE_PRIVACY_POLICY)} characters")
    print(f"Preview: {SAMPLE_PRIVACY_POLICY[:200]}...")
