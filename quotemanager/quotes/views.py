from django.shortcuts import render, get_object_or_404, redirect
from .models import Quote
from .forms import QuoteForm

def quote_list(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    if query:
        # Search by author or quote text
        quotes_by_author = Quote.objects.filter(author__icontains=query)
        quotes_by_text = Quote.objects.filter(text__icontains=query)
        quotes = list(quotes_by_author) + list(quotes_by_text)
        quotes = list({quote.pk: quote for quote in quotes}.values())  # Remove duplicates
    else:
        quotes = Quote.objects.all()

    context = {
        'quotes': quotes,
        'query': query,
    }
    return render(request, 'quotes/quote_list.html', context)

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm()
    return render(request, 'quotes/quote_form.html', {'form': form, 'title': 'Add Quote'})

def edit_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_list')
    else:
        form = QuoteForm(instance=quote)
    return render(request, 'quotes/quote_form.html', {'form': form, 'title': 'Edit Quote'})

def delete_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    if request.method == 'POST':
        quote.delete()
        return redirect('quote_list')
    return render(request, 'quotes/quote_confirm_delete.html', {'quote': quote})