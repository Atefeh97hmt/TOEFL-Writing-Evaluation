# TOEFL Writing Evaluator

This Python program uses Hugging Face's `transformers` library to provide a mock TOEFL writing evaluation. It scores an English writing sample on key TOEFL criteria.

### Requirements
- Python 3.6+
- `transformers` library (`pip install transformers`)

### How It Works
1. **Initialize Pipeline**: Uses `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis with PyTorch.
2. **Evaluate Writing**: Simulates TOEFL scoring for:
   - **Task Achievement**
   - **Coherence and Cohesion**
   - **Lexical Resource**
   - **Grammatical Range and Accuracy**
3. **Display Results**: Outputs scores based on a mock analysis.

### Usage
Run the program, input your writing sample, and receive feedback based on TOEFL criteria. 

**Note**: This is a mock evaluator and does not reflect official TOEFL scoring.
