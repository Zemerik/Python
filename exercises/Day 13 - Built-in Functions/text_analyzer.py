"""
Exercise 2: Text Analyzer
Build a text analyzer that:
- Uses map to capitalize words
- Uses filter to remove stopwords
- Uses reduce to find longest word
"""

from functools import reduce
import re

class TextAnalyzer:
    """Text analyzer using functional programming tools"""
    
    def __init__(self):
        """Initialize the text analyzer"""
        self.text = ""
        self.words = []
        self.stopwords = {
            'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
            'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
            'to', 'was', 'will', 'with', 'the', 'this', 'but', 'they', 'have',
            'had', 'what', 'said', 'each', 'which', 'she', 'do', 'how', 'their',
            'if', 'up', 'out', 'many', 'then', 'them', 'these', 'so', 'some',
            'her', 'would', 'make', 'like', 'into', 'him', 'time', 'two',
            'more', 'go', 'no', 'way', 'could', 'my', 'than', 'first', 'been',
            'call', 'who', 'oil', 'sit', 'now', 'find', 'down', 'day', 'did',
            'get', 'come', 'made', 'may', 'part', 'over', 'new', 'sound',
            'take', 'only', 'little', 'work', 'know', 'place', 'year', 'live',
            'me', 'back', 'give', 'most', 'very', 'after', 'thing', 'our',
            'just', 'name', 'good', 'sentence', 'man', 'think', 'say', 'great',
            'where', 'help', 'through', 'much', 'before', 'line', 'right',
            'too', 'mean', 'old', 'any', 'same', 'tell', 'boy', 'follow',
            'came', 'want', 'show', 'also', 'around', 'form', 'three',
            'small', 'set', 'put', 'end', 'does', 'another', 'well', 'large',
            'must', 'big', 'even', 'such', 'because', 'turn', 'here', 'why',
            'ask', 'went', 'men', 'read', 'need', 'land', 'different', 'home',
            'us', 'move', 'try', 'kind', 'hand', 'picture', 'again', 'change',
            'off', 'play', 'spell', 'air', 'away', 'animal', 'house', 'point',
            'page', 'letter', 'mother', 'answer', 'found', 'study', 'still',
            'learn', 'should', 'America', 'world', 'high', 'every', 'near',
            'add', 'food', 'between', 'own', 'below', 'country', 'plant',
            'last', 'school', 'father', 'keep', 'tree', 'never', 'start',
            'city', 'earth', 'eye', 'light', 'thought', 'head', 'under',
            'story', 'saw', 'left', 'don\'t', 'few', 'while', 'along',
            'might', 'close', 'something', 'seem', 'next', 'hard', 'open',
            'example', 'begin', 'life', 'always', 'those', 'both', 'paper',
            'together', 'got', 'group', 'often', 'run', 'important', 'until',
            'children', 'side', 'feet', 'car', 'mile', 'night', 'walk',
            'white', 'sea', 'began', 'grow', 'took', 'river', 'four',
            'carry', 'state', 'once', 'book', 'hear', 'stop', 'without',
            'second', 'late', 'miss', 'idea', 'enough', 'eat', 'face',
            'watch', 'far', 'Indian', 'really', 'almost', 'let', 'above',
            'girl', 'sometimes', 'mountain', 'cut', 'young', 'talk', 'soon',
            'list', 'song', 'being', 'leave', 'family', 'it\'s'
        }
    
    def load_text(self, text):
        """Load text for analysis"""
        self.text = text
        # Split text into words and clean them
        self.words = re.findall(r'\b\w+\b', text.lower())
        print(f"Loaded text with {len(self.words)} words")
    
    def load_sample_text(self):
        """Load sample text for demonstration"""
        sample_text = """
        The quick brown fox jumps over the lazy dog. This is a sample text 
        that contains various words of different lengths. We will use this 
        text to demonstrate functional programming concepts like map, filter, 
        and reduce. The text includes common words and some longer words 
        to show the capabilities of our text analyzer.
        """
        self.load_text(sample_text)
    
    def capitalize_words(self, word):
        """Capitalize a word"""
        return word.capitalize()
    
    def is_not_stopword(self, word):
        """Check if word is not a stopword"""
        return word.lower() not in self.stopwords
    
    def find_longer_word(self, word1, word2):
        """Find the longer of two words"""
        return word1 if len(word1) > len(word2) else word2
    
    def analyze_text(self):
        """Analyze text using functional programming tools"""
        if not self.words:
            print("No text loaded. Load text first.")
            return
        
        print("\n=== Text Analysis Using Functional Programming ===")
        
        # Step 1: Capitalize words using map
        print("1. Capitalizing words using map():")
        capitalized_words = list(map(self.capitalize_words, self.words))
        print(f"   Original: {self.words[:10]}...")
        print(f"   Capitalized: {capitalized_words[:10]}...")
        
        # Step 2: Remove stopwords using filter
        print("\n2. Removing stopwords using filter():")
        filtered_words = list(filter(self.is_not_stopword, self.words))
        print(f"   Original words: {len(self.words)}")
        print(f"   After filtering: {len(filtered_words)}")
        print(f"   Removed {len(self.words) - len(filtered_words)} stopwords")
        print(f"   Sample filtered words: {filtered_words[:10]}...")
        
        # Step 3: Find longest word using reduce
        print("\n3. Finding longest word using reduce():")
        if filtered_words:
            longest_word = reduce(self.find_longer_word, filtered_words)
            print(f"   Longest word: '{longest_word}' ({len(longest_word)} characters)")
        else:
            print("   No words after filtering")
        
        # Store analysis results
        self.analysis_results = {
            'original_words': self.words,
            'capitalized_words': capitalized_words,
            'filtered_words': filtered_words,
            'longest_word': longest_word if filtered_words else None,
            'word_count': len(self.words),
            'filtered_count': len(filtered_words),
            'stopwords_removed': len(self.words) - len(filtered_words)
        }
        
        return self.analysis_results
    
    def demonstrate_lambda_functions(self):
        """Demonstrate lambda functions with text analysis"""
        if not self.words:
            print("No text loaded. Load text first.")
            return
        
        print("\n=== Lambda Function Demonstrations ===")
        
        # Lambda with map - convert to uppercase
        print("1. Lambda with map() - Convert to uppercase:")
        uppercase_words = list(map(lambda word: word.upper(), self.words[:10]))
        print(f"   Uppercase: {uppercase_words}")
        
        # Lambda with filter - find words longer than 5 characters
        print("\n2. Lambda with filter() - Words longer than 5 characters:")
        long_words = list(filter(lambda word: len(word) > 5, self.words))
        print(f"   Long words: {long_words[:10]}...")
        print(f"   Count: {len(long_words)}")
        
        # Lambda with reduce - find shortest word
        print("\n3. Lambda with reduce() - Find shortest word:")
        if self.words:
            shortest_word = reduce(lambda a, b: a if len(a) < len(b) else b, self.words)
            print(f"   Shortest word: '{shortest_word}' ({len(shortest_word)} characters)")
        
        # Complex lambda operations
        print("\n4. Complex lambda operations:")
        # Filter long words, capitalize them, then find the longest
        long_capitalized = list(map(lambda word: word.capitalize(), 
                                  filter(lambda word: len(word) > 5, self.words)))
        if long_capitalized:
            longest_capitalized = reduce(lambda a, b: a if len(a) > len(b) else b, long_capitalized)
            print(f"   Longest capitalized long word: '{longest_capitalized}'")
    
    def word_frequency_analysis(self):
        """Analyze word frequencies using functional programming"""
        if not self.words:
            print("No text loaded. Load text first.")
            return
        
        print("\n=== Word Frequency Analysis ===")
        
        # Get unique words
        unique_words = list(set(self.words))
        print(f"Unique words: {len(unique_words)}")
        
        # Count word frequencies using functional approach
        word_counts = {}
        for word in unique_words:
            count = len(list(filter(lambda w: w == word, self.words)))
            word_counts[word] = count
        
        # Find most frequent words
        most_frequent = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        print("\nMost frequent words:")
        for word, count in most_frequent:
            print(f"   '{word}': {count} times")
        
        # Find words with specific lengths
        print("\nWords by length:")
        for length in range(1, 11):
            words_of_length = list(filter(lambda word: len(word) == length, unique_words))
            if words_of_length:
                print(f"   {length} letters: {len(words_of_length)} words")
    
    def compare_with_list_comprehensions(self):
        """Compare functional programming with list comprehensions"""
        if not self.words:
            print("No text loaded. Load text first.")
            return
        
        print("\n=== Functional vs List Comprehension Comparison ===")
        
        # Map vs List Comprehension
        print("1. Capitalizing words:")
        # Functional approach
        capitalized_func = list(map(self.capitalize_words, self.words))
        # List comprehension approach
        capitalized_comp = [word.capitalize() for word in self.words]
        print(f"   Functional (map): {capitalized_func[:5]}")
        print(f"   List comprehension: {capitalized_comp[:5]}")
        print(f"   Results match: {capitalized_func == capitalized_comp}")
        
        # Filter vs List Comprehension
        print("\n2. Filtering stopwords:")
        # Functional approach
        filtered_func = list(filter(self.is_not_stopword, self.words))
        # List comprehension approach
        filtered_comp = [word for word in self.words if word.lower() not in self.stopwords]
        print(f"   Functional (filter): {filtered_func[:5]}")
        print(f"   List comprehension: {filtered_comp[:5]}")
        print(f"   Results match: {filtered_func == filtered_comp}")
        
        # Reduce vs max()
        print("\n3. Finding longest word:")
        # Functional approach
        longest_func = reduce(self.find_longer_word, self.words)
        # Built-in max approach
        longest_builtin = max(self.words, key=len)
        print(f"   Functional (reduce): '{longest_func}'")
        print(f"   Built-in max(): '{longest_builtin}'")
        print(f"   Results match: {longest_func == longest_builtin}")
    
    def display_statistics(self):
        """Display comprehensive text statistics"""
        if not hasattr(self, 'analysis_results'):
            print("No analysis results available. Run analyze_text() first.")
            return
        
        results = self.analysis_results
        
        print("\n=== Text Analysis Statistics ===")
        print(f"Total words: {results['word_count']}")
        print(f"Unique words: {len(set(results['original_words']))}")
        print(f"Words after filtering: {results['filtered_count']}")
        print(f"Stopwords removed: {results['stopwords_removed']}")
        
        if results['longest_word']:
            print(f"Longest word: '{results['longest_word']}' ({len(results['longest_word'])} chars)")
        
        # Word length distribution
        word_lengths = [len(word) for word in results['original_words']]
        if word_lengths:
            avg_length = sum(word_lengths) / len(word_lengths)
            print(f"Average word length: {avg_length:.1f} characters")
            print(f"Shortest word: {min(word_lengths)} characters")
            print(f"Longest word: {max(word_lengths)} characters")

def main():
    """Main function to demonstrate the text analyzer"""
    print("=== Functional Programming Text Analyzer ===")
    analyzer = TextAnalyzer()
    
    while True:
        print("\nChoose an option:")
        print("1. Load sample text")
        print("2. Load custom text")
        print("3. Analyze text")
        print("4. Demonstrate lambda functions")
        print("5. Word frequency analysis")
        print("6. Compare with list comprehensions")
        print("7. Display statistics")
        print("8. Exit")
        
        try:
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                analyzer.load_sample_text()
            
            elif choice == '2':
                text = input("Enter your text: ")
                analyzer.load_text(text)
            
            elif choice == '3':
                analyzer.analyze_text()
            
            elif choice == '4':
                analyzer.demonstrate_lambda_functions()
            
            elif choice == '5':
                analyzer.word_frequency_analysis()
            
            elif choice == '6':
                analyzer.compare_with_list_comprehensions()
            
            elif choice == '7':
                analyzer.display_statistics()
            
            elif choice == '8':
                print("Goodbye!")
                break
            
            else:
                print("Please enter a number between 1 and 8.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main() 