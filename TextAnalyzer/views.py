from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   if request.method == "POST":
      text_input = request.POST.get("text-input")
      text_input = str(text_input)

      # if text_input == "":
      #    print("Khaali hai")

   # Count Words in input
      words = len(text_input.split())

   # creating reuired variables
      chars = 0
      uppercase = 0
      lowercase = 0
      spaces = 0
      chars_with_spaces = 0
      numbers = 0
      dot = 0

   # For loop for counting
      for i in text_input:

         # counting characters
         if i.isalpha():
            chars = chars + 1

         # counting spaces
         elif i.isspace():
            spaces = spaces + 1

         # counting digits
         elif i.isdigit():
            numbers = numbers + 1
      
         # Couting Punctuations

      var_list = {"words":words, "chars":chars, "spaces":spaces, "numbers":numbers} 
      return render(request, "index.html", var_list)
   return render(request, "index.html")