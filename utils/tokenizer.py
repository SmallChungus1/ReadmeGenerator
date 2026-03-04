import os

def truncate_text(text, token_limit, tokenizer=None, model_name="gpt2"):
    """
    Truncates text to a specific token limit.
    If no tokenizer is provided, it attempts to load one using transformers.
    
    Args:
        text (str): The text to truncate.
        token_limit (int): The maximum number of tokens allowed.
        tokenizer: An optional pre-loaded tokenizer object.
        model_name (str): The model name to use for loading a tokenizer if none is provided.
        
    Returns:
        str: The truncated text.
    """
    if not text or token_limit <= 0:
        return ""

    # If tokenizer is None, try to use transformers to get a proxy tokenizer
    if tokenizer is None:
        try:
            from transformers import AutoTokenizer
            # Use gpt2 as a common proxy if model_name is not provided or fails
            tokenizer = AutoTokenizer.from_pretrained(model_name)
        except Exception as e:
            # Fallback to a rough character-based approximation if transformers is not available
            print(f"Warning: Could not load tokenizer ({e}). Falling back to character-based approximation.")
            chars_per_token = 4 
            char_limit = token_limit * chars_per_token
            return text[:char_limit]

    try:
        # Tokenize
        tokens = tokenizer.encode(text, add_special_tokens=False)
        if len(tokens) <= token_limit:
            return text
        
        # Truncate
        truncated_tokens = tokens[:token_limit]
        
        # Decode back to text
        return tokenizer.decode(truncated_tokens, skip_special_tokens=True)
    except Exception as e:
        print(f"Error during tokenization/truncation: {e}")
        # Final fallback
        chars_per_token = 4
        return text[:token_limit * chars_per_token]
