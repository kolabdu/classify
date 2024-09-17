# # # # # views.py   


# from django.http import HttpResponse
# from django.shortcuts import render
# from .utils import load_model_and_vectorizer, predict_url_category,clean_url

# def index(request):
#     return render(request, 'index.html')

# def predict_category(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('url_input')

#         if not user_input:
#             return render(request, 'index.html', {'error': 'Please enter a URL'})

#         cleaned_input = [clean_url(user_input)]

#         try:
#             # Load model and vectorizer
#             model, vectorizer = load_model_and_vectorizer()
#             print("Form submitted. Input URL:", cleaned_input)

#             # Get prediction
#             prediction = predict_url_category(cleaned_input, model, vectorizer)
#             print("Predicted category:", prediction)

#             # Return the prediction result
#             return render(request, 'index.html', {'prediction': prediction})

#         except Exception as e:
#             print(f"Error occurred: {e}")
#             return render(request, 'index.html', {'error': 'An error occurred while processing the URL. Please try again later.'})

#     # If the request method is not POST (e.g., GET), render the index page
#     return render(request, 'index.html')


# # def makeTokens(url):
# #     tkns_BySlash = str(url.encode('utf-8')).split('/')  # make tokens after splitting by slash
# #     total_Tokens = []
# #     for i in tkns_BySlash:
# #         tokens = str(i).split('-')  # make tokens after splitting by dash
# #         tkns_ByDot = []
# #         for j in range(0, len(tokens)):
# #             temp_Tokens = str(tokens[j]).split('.')  # make tokens after splitting by dot
# #             tkns_ByDot = tkns_ByDot + temp_Tokens
# #         total_Tokens = total_Tokens + tokens + tkns_ByDot
# #     total_Tokens = list(set(total_Tokens))  # remove redundant tokens
# #     if 'com' in total_Tokens:
# #         total_Tokens.remove('com')  # removing .com since it occurs a lot of times and it should not be included in our features
# #     return total_Tokens

# # def index(request):
# #     return render(request, 'index.html')

# # def predict_category(request):
# #     if request.method == 'POST':
# #         user_input = request.POST.get('url_input')
# #         cleaned_input = [clean_url(user_input)]
        

# #     # Using Custom Tokenizer
        
# #         model,vectorizer = load_model_and_vectorizer()
# #         print("Form submitted. Input URL:", cleaned_input)  # Add print statement
# #         prediction = predict_url_category(cleaned_input, model,vectorizer)
# #         print("Predicted category:", prediction)  # Add print statement
# #         ##########
# #         #return render(request, 'result.html', {'prediction': prediction})
# #         return render(request, 'index.html', {'prediction': prediction})
# #     #If the request method is not POST (e.g., GET), render the index page
# #     return render(request, 'index.html')



from django.http import HttpResponse
from django.shortcuts import render
from .utils import load_model_and_vectorizer, predict_url_category, clean_url

def index(request):
    return render(request, 'index.html')

def predict_category(request):
    if request.method == 'POST':
        user_input = request.POST.get('url_input')

        if not user_input:
            return render(request, 'index.html', {'error': 'Please enter a URL'})

        cleaned_input = [clean_url(user_input)]

        try:
            # Load model and vectorizer
            model, vectorizer = load_model_and_vectorizer()
            print("Form submitted. Input URL:", cleaned_input)
            
            # Print the tokenizer to check if it's correctly loaded
            if hasattr(vectorizer, 'tokenizer'):
                print("Tokenizer found:", vectorizer.tokenizer)
            else:
                print("Tokenizer not found in the vectorizer")

            # Get prediction
            prediction = predict_url_category(cleaned_input, model, vectorizer)
            print("Predicted category:", prediction)

            # Return the prediction result
            return render(request, 'index.html', {'prediction': prediction})

        except Exception as e:
            print(f"Error occurred: {e}")
            return render(request, 'index.html', {'error': 'An error occurred while processing the URL. Please try again later.'})

    # If the request method is not POST (e.g., GET), render the index page
    return render(request, 'index.html')
