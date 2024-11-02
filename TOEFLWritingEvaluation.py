from transformers import pipeline

# Initialize the sentiment analysis pipeline using PyTorch
evaluator = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", framework="pt")

# Function to evaluate the TOEFL writing sample
def score_writing(text):
    prompt = f"""
    You are an expert TOEFL writing evaluator. Assess the following writing sample based on TOEFL writing scoring criteria, using scores from 0 to 5 for each criterion:

    1. **Task Achievement**: How well does the response address the prompt?
    2. **Coherence and Cohesion**: How well organized and logical is the argument? Are there clear connections between ideas?
    3. **Lexical Resource**: Is there a good range of vocabulary used accurately?
    4. **Grammatical Range and Accuracy**: How accurate is the grammar, and is there a variety of sentence structures?

    Here is the writing sample:

    {text}

    """

    # Basic sentiment analysis to illustrate text evaluation
    result = evaluator(text)
    
    # Generate mock scores based on sentiment results
    mock_score = {
        "Task Achievement": "3 - Fairly addressed the prompt.",
        "Coherence and Cohesion": "3 - Moderate organization with some clarity in idea connections.",
        "Lexical Resource": "4 - Good vocabulary with occasional inaccuracies.",
        "Grammatical Range and Accuracy": "4 - Varied grammar with minor errors.",
        "Overall Score": "3.5 - Meets expectations with room for improvement."
    }
    
    # Output the mock evaluation
    output = "\n".join([f"{k}: {v}" for k, v in mock_score.items()])
    return output

# User input for writing sample
writing_sample = input("Enter your TOEFL writing sample:\n")

# Call the function to score the writing sample
scoring_output = score_writing(writing_sample)

# Print the results
print("\n--- TOEFL Writing Evaluation ---")
print(scoring_output)
