
import dill
from sklearn.feature_extraction.text import TfidfVectorizer
#from . import vectorizer_rename as vector



def clean_url(url):
    prefixes = ['http://www.', 'https://www.', 'www.']
    for prefix in prefixes:
        if url.startswith(prefix):
            url = url.replace(prefix, '')
            break
    return url

# Define the makeTokens function
# def makeTokens(url):
#     tkns_BySlash = str(url.encode('utf-8')).split('/')  # make tokens after splitting by slash
#     total_Tokens = []
#     for i in tkns_BySlash:
#         tokens = str(i).split('-')  # make tokens after splitting by dash
#         tkns_ByDot = []
#         for j in range(0, len(tokens)):
#             temp_Tokens = str(tokens[j]).split('.')  # make tokens after splitting by dot
#             tkns_ByDot = tkns_ByDot + temp_Tokens
#         total_Tokens = total_Tokens + tokens + tkns_ByDot
#     total_Tokens = list(set(total_Tokens))  # remove redundant tokens
#     if 'com' in total_Tokens:
#         total_Tokens.remove('com')  # removing .com since it occurs a lot of times and it should not be included in our features
#     return total_Tokens

# def makeTokens(url):
#     if not url:
#         return []

#     tkns_BySlash = str(url.encode('utf-8')).split('/')  # make tokens after splitting by slash
#     total_Tokens = []

#     for i in tkns_BySlash:  # Check if tkns_BySlash is non-empty
#         if i:  # Ensure `i` is not empty
#             tokens = str(i).split('-')  # make tokens after splitting by dash
#             tkns_ByDot = []
#             for j in range(len(tokens)):
#                 if tokens[j]:  # Ensure token is not empty
#                     temp_Tokens = str(tokens[j]).split('.')  # make tokens after splitting by dot
#                     tkns_ByDot += temp_Tokens
#             total_Tokens += tokens + tkns_ByDot
    
#     # Remove redundant tokens
#     total_Tokens = list(set(total_Tokens))

#     # Handle common tokens like 'com'
#     if 'com' in total_Tokens:
#         total_Ttokens.remove('com')

#     return total_Tokens


# def makeTokens(url):
#     print(f"Original URL: {url}")

#     if not url:
#         print("URL is empty.")
#         return []

#     tkns_BySlash = str(url.encode('utf-8')).split('/')
#     print(f"Tokens by slash: {tkns_BySlash}")

#     total_Tokens = []
#     for i in tkns_BySlash:
#         if i:
#             print(f"Processing token: {i}")
#             tokens = str(i).split('-')
#             tkns_ByDot = []
#             for j in range(len(tokens)):
#                 if tokens[j]:
#                     temp_Tokens = str(tokens[j]).split('.')
#                     tkns_ByDot += temp_Tokens
#             total_Tokens += tokens + tkns_ByDot

#     print(f"Final tokens before removing redundancy: {total_Tokens}")
    
#     total_Tokens = list(set(total_Tokens))
    
#     if 'com' in total_Tokens:
#         total_Tokens.remove('com')

#     print(f"Final tokens: {total_Tokens}")
#     return total_Tokens



# def makeTokens(url):
#     try:
#         # Encode the URL to UTF-8 and convert to string, but handle it more carefully
#         tkns_BySlash = str(url).split('/')  # Split by slash

#         total_Tokens = []
#         for i in tkns_BySlash:
#             print(f"Token from slash: {i}")  # Debugging print

#             tokens = str(i).split('-')  # Split by dash
#             tkns_ByDot = []
#             for j in range(0, len(tokens)):
#                 temp_Tokens = str(tokens[j]).split('.')  # Split by dot
#                 tkns_ByDot = tkns_ByDot + temp_Tokens
#             total_Tokens = total_Tokens + tokens + tkns_ByDot

#         total_Tokens = list(set(total_Tokens))  # Remove redundant tokens

#         if 'com' in total_Tokens:
#             total_TTokens.remove('com')  # Remove '.com'
        
#         print(f"Final tokens: {total_Tokens}")  # Debugging print

#         return total_Tokens

#     except Exception as e:
#         print(f"Error in makeTokens function: {e}")
#         return []  # Return an empty list if an error occurs

# def makeTokens(url):
#     try:
#         # Ensure the input is treated as a string
#         url_str = str(url)
#         tkns_BySlash = url_str.split('/')  # Split by slash
        
#         total_Tokens = []

#         for i in tkns_BySlash:
#             if not i:  # Skip if `i` is None or empty
#                 continue

#             print(f"Token from slash: {i}")  # Debugging print

#             tokens = str(i).split('-')  # Split by dash
            
#             tkns_ByDot = []
#             for j in range(len(tokens)):
#                 if not tokens[j]:  # Skip if `tokens[j]` is None or empty
#                     continue

#                 temp_Tokens = str(tokens[j]).split('.')  # Split by dot
#                 tkns_ByDot.extend(temp_Tokens)  # Collect the dot tokens

#             total_Tokens.extend(tokens + tkns_ByDot)  # Combine the tokens

#         total_Tokens = list(set(total_Tokens))  # Remove redundant tokens

#         if 'com' in total_Tokens:
#             total_TTokens.remove('com')  # Remove '.com'

#         print(f"Final tokens: {total_Tokens}")  # Debugging print

#         return total_Tokens

#     except Exception as e:
#         print(f"Error in makeTokens function: {e}")
#         return []  # Return an empty list if an error occurs


# def makeTokens(url):
#     try:
#         # Ensure the input is treated as a string
#         url_str = str(url)
#         tkns_BySlash = url_str.split('/')  # Split by slash
        
#         total_Tokens = []

#         for i in tkns_BySlash:
#             if not i:  # Skip if `i` is None or empty
#                 print("Skipping empty 'i' from slash")
#                 continue

#             print(f"Processing token from slash: {i}")  # Debugging print

#             tokens = str(i).split('-')  # Split by dash
#             tkns_ByDot = []

#             for j in range(len(tokens)):
#                 if not tokens[j]:  # Skip if `tokens[j]` is None or empty
#                     print(f"Skipping empty token from dash at index {j}")
#                     continue

#                 temp_Tokens = str(tokens[j]).split('.')  # Split by dot
#                 print(f"Processing dot token: {temp_Tokens}")

#                 # Safely extend tokens, handle if temp_Tokens is empty
#                 tkns_ByDot.extend(temp_Tokens if temp_Tokens else [])
            
#             # Safely extend total tokens
#             total_Tokens.extend(tokens if tokens else [])
#             total_Tokens.extend(tkns_ByDot)

#         total_Tokens = list(set(total_Tokens))  # Remove redundant tokens

#         if 'com' in total_Tokens:
#             total_TTokens.remove('com')  # Remove '.com'

#         print(f"Final tokens: {total_Tokens}")  # Debugging print

#         return total_Tokens

#     except Exception as e:
#         print(f"Error in makeTokens function: {e}")
#         return []  # Return an empty list if an error occurs

# def makeTokens(url):
#     try:
#         url_str = str(url)
#         tkns_BySlash = url_str.split('/')  # Split by slash
#         total_Tokens = []

#         # Loop through tokens created by slash
#         for f in tkns_BySlash:
#             print(f"Current value of i (slash): {f}")  # Log i from the first loop

#             if not f:  # Skip if `f` is None or empty
#                 continue

#             tokens = str(f).split('-')  # Split by dash
#             tkns_ByDot = []

#             # Loop through tokens created by dash
#             for j in range(len(tokens)):
#                 print(f"Current value of j (dash): {tokens[j]}")  # Log j from the second loop

#                 if not tokens[j]:  # Skip if `tokens[j]` is None or empty
#                     continue

#                 temp_Tokens = str(tokens[j]).split('.')  # Split by dot
#                 print(f"Tokens from dot: {temp_Tokens}")  # Log dot-split tokens

#                 tkns_ByDot.extend(temp_Tokens)  # Collect the dot tokens

#             total_Tokens.extend(tokens + tkns_ByDot)  # Combine the tokens

#         total_Tokens = list(set(total_Tokens))  # Remove redundant tokens

#         if 'com' in total_Tokens:
#             total_TTokens.remove('com')  # Remove '.com'

#         print(f"Final tokens: {total_Tokens}")  # Final tokens log
#         return total_Tokens

#     except Exception as e:
#         print(f"Error in makeTokens function: {e}")
#         return []


def makeTokens(url):
    try:
        url_str = str(url)
        tkns_BySlash = url_str.split('/')  # Split by slash
        total_Tokens = []

        # Loop through tokens created by slash
        for f in tkns_BySlash:  # Changed i to f
            if not f:  # Skip empty tokens
                continue

            tokens = str(f).split('-')  # Split by dash
            tkns_ByDot = []

            # Loop through tokens created by dash
            for j in range(len(tokens)):
                if not tokens[j]:  # Skip empty tokens
                    continue

                temp_Tokens = str(tokens[j]).split('.')  # Split by dot
                tkns_ByDot.extend(temp_Tokens)  # Collect the dot tokens

            total_Tokens.extend(tokens + tkns_ByDot)  # Combine the tokens

        total_Tokens = list(set(total_Tokens))  # Remove redundant tokens

        if 'com' in total_Tokens:
            total_Tokens.remove('com')  # Remove '.com'

        return total_Tokens

    except Exception as e:
        print(f"Error in makeTokens function: {e}")
        return []  # Return an empty list if there's an error




# Save the vectorizer using dill
def save_vectorizer(vectorizer, filename):
    with open(filename, 'wb') as file:
        dill.dump(vectorizer, file)

# Initialize TfidfVectorizer with custom tokenizer and save it
def initialize_and_save_vectorizer():
    vectorizer = TfidfVectorizer(tokenizer=makeTokens)
    save_vectorizer(vectorizer, 'vectorizer_dill.pkl')

# Function to load model and vectorizer
def load_model_and_vectorizer():
    with open('logit_model.pkl', 'rb') as file:
        model = dill.load(file)
    with open('vectorizer_dill.pkl', 'rb') as file:
        vectorizer = dill.load(file)
    return model, vectorizer

def predict_url_category(url, model, vectorizer):
    prediction = model.predict(vectorizer.transform(url))
    if prediction == 'good':
        return 'The URL is safe'
    else:
        return "URL APPEARS TO BE MALICIOUS"





# def clean_url(url):
#     prefixes = ['http://www.', 'https://www.', 'www.']
#     for prefix in prefixes:
#         if url.startswith(prefix):
#             url = url.replace(prefix, '')
#             break
#     return url



# # Define the makeTokens function
# def makeTokens(f):
#     tkns_BySlash = str(f.encode('utf-8')).split('/')    # make tokens after splitting by slash
#     total_Tokens = []
#     for i in tkns_BySlash:
#         tokens = str(i).split('-')    # make tokens after splitting by dash
#         tkns_ByDot = []
#         for j in range(0, len(tokens)):
#             temp_Tokens = str(tokens[j]).split('.')    # make tokens after splitting by dot
#             tkns_ByDot = tkns_ByDot + temp_Tokens
#         total_Tokens = total_Tokens + tokens + tkns_ByDot
#     total_Tokens = list(set(total_Tokens))    # remove redundant tokens
#     if 'com' in total_Tokens:
#         total_Tokens.remove('com')    # removing .com since it occurs a lot of times and it should not be included in our features
#     return total_Tokens

# # Initialize TfidfVectorizer with custom tokenizer
# #vectorizer = TfidfVectorizer(tokenizer=makeTokens)




# def load_model_and_vectorizer():
#     with open('logit_model.pkl', 'rb') as file:
#         model = pickle.load(file)
#     with open('vectorizer_dill.pkl', 'rb') as file:
#         vectorizer = dill.load(file)
#     return model, vectorizer

# def predict_url_category(url, model,vectorizer):
       
#     prediction = model.predict(vectorizer.transform(url))
#     if prediction == 'good':
#         return 'The URL is safe'
#     else:
#         return "URL APPEARS TO BE MALICIOUS"


